#!/usr/bin/env python3
"""
Generate the full-size printable CAD package for the Arduino delivery robot.

The models are intentionally parametric and conservative: slots are used where
commodity module hole patterns vary, while the critical envelopes match the
Arduino Mega, BTS7960 modules, encoder 37D gearmotors, 120 mm wheels,
Raspberry Pi companion computer, front/rear cameras, and lid-lock hardware
listed in the build guide.
"""

from __future__ import annotations

import json
import math
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw
import trimesh


ROOT = Path(__file__).resolve().parents[2]
CAD_ROOT = ROOT / "cad"
OUT = CAD_ROOT / "print-ready"
RENDER_OUT = CAD_ROOT / "renders"


@dataclass(frozen=True)
class Dims:
    # Overall printed chassis footprint follows the existing four STL quadrants.
    base_len: float = 322.0
    base_w: float = 328.0
    base_t: float = 8.0
    wheel_d: float = 120.0
    wheel_w: float = 60.0
    motor_d: float = 37.0
    motor_len: float = 68.0
    motor_shaft_d: float = 6.0
    motor_shaft_len: float = 16.0
    motor_x: float = 108.0
    motor_y: float = 185.0
    motor_z: float = 46.0
    body_len: float = 300.0
    body_w: float = 230.0
    body_h: float = 155.0
    panel_t: float = 3.0
    post_size: float = 18.0
    lid_t: float = 4.0
    cargo_floor_len: float = 272.0
    cargo_floor_w: float = 216.0
    cargo_floor_t: float = 4.0
    cargo_floor_z: float = 66.0
    cargo_support_hole_z: float = 60.0
    cargo_rail_h: float = 16.0
    max_food_box_len: float = 205.0
    max_food_box_w: float = 145.0
    max_food_box_h: float = 70.0
    camera_mount_w: float = 64.0
    camera_mount_h: float = 42.0
    camera_mount_t: float = 3.0
    pi_tray_len: float = 104.0
    pi_tray_w: float = 76.0
    lte_tray_len: float = 96.0
    lte_tray_w: float = 42.0


D = Dims()


def ensure_dirs() -> None:
    for p in [
        OUT / "full-size",
        OUT / "chassis",
        OUT / "body",
        OUT / "cargo",
        OUT / "electronics",
        OUT / "accessories",
        RENDER_OUT,
    ]:
        p.mkdir(parents=True, exist_ok=True)


def box(size: tuple[float, float, float], center: tuple[float, float, float]) -> trimesh.Trimesh:
    mesh = trimesh.creation.box(extents=size)
    mesh.apply_translation(center)
    return mesh


def cyl_z(radius: float, height: float, center: tuple[float, float, float], sections: int = 48) -> trimesh.Trimesh:
    mesh = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    mesh.apply_translation(center)
    return mesh


def cyl_axis(
    axis: str,
    radius: float,
    length: float,
    center: tuple[float, float, float],
    sections: int = 48,
) -> trimesh.Trimesh:
    mesh = trimesh.creation.cylinder(radius=radius, height=length, sections=sections)
    if axis == "x":
        mesh.apply_transform(trimesh.transformations.rotation_matrix(math.pi / 2, [0, 1, 0]))
    elif axis == "y":
        mesh.apply_transform(trimesh.transformations.rotation_matrix(math.pi / 2, [1, 0, 0]))
    elif axis != "z":
        raise ValueError(axis)
    mesh.apply_translation(center)
    return mesh


def combine(meshes: Iterable[trimesh.Trimesh]) -> trimesh.Trimesh:
    return trimesh.util.concatenate([m for m in meshes if m is not None])


def union(meshes: Iterable[trimesh.Trimesh]) -> trimesh.Trimesh:
    solids = [m for m in meshes if m is not None]
    if len(solids) == 1:
        return solids[0]
    result = trimesh.boolean.union(solids, engine="manifold")
    result.merge_vertices()
    result.remove_unreferenced_vertices()
    return result


def difference(mesh: trimesh.Trimesh, cutters: list[trimesh.Trimesh]) -> trimesh.Trimesh:
    if not cutters:
        return mesh
    result = trimesh.boolean.difference([mesh, *cutters], engine="manifold")
    result.merge_vertices()
    result.remove_unreferenced_vertices()
    return result


def intersection(mesh: trimesh.Trimesh, cutter: trimesh.Trimesh) -> trimesh.Trimesh:
    result = trimesh.boolean.intersection([mesh, cutter], engine="manifold")
    result.merge_vertices()
    result.remove_unreferenced_vertices()
    return result


def export(mesh: trimesh.Trimesh, rel: str) -> Path:
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    mesh.export(path)
    return path


def slot_cut_z(x: float, y: float, sx: float, sy: float, z: float, h: float) -> trimesh.Trimesh:
    return box((sx, sy, h), (x, y, z))


def hole_grid_z(points: Iterable[tuple[float, float]], diameter: float, z: float, h: float) -> list[trimesh.Trimesh]:
    return [cyl_z(diameter / 2, h, (x, y, z), 32) for x, y in points]


def base_plate_full() -> trimesh.Trimesh:
    plate = box((D.base_len, D.base_w, D.base_t), (0, 0, D.base_t / 2))

    cutters: list[trimesh.Trimesh] = []

    # Body post and lid fastener holes.
    post_x = D.body_len / 2 - D.post_size / 2
    post_y = D.body_w / 2 - D.post_size / 2
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            cutters.append(cyl_z(1.7, D.base_t + 4, (sx * post_x, sy * post_y, D.base_t / 2), 32))

    # Joining holes across both split seams, sized for M3 clearance screws.
    seam_points = []
    for x in [-120, -80, -40, 40, 80, 120]:
        seam_points.append((x, -7))
        seam_points.append((x, 7))
    for y in [-125, -85, -45, 45, 85, 125]:
        seam_points.append((-7, y))
        seam_points.append((7, y))
    cutters.extend(hole_grid_z(seam_points, 3.4, D.base_t / 2, D.base_t + 4))

    # Pololu 37D bracket mounting area. Slots absorb bracket/vendor variation.
    # One motor bracket sits at each corner, shaft pointing outwards.
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            cx = sx * D.motor_x
            cy = sy * 119
            for dx in [-22, 22]:
                cutters.append(slot_cut_z(cx + dx, cy, 8, 28, D.base_t / 2, D.base_t + 4))
            cutters.append(slot_cut_z(cx, sy * 92, 22, 8, D.base_t / 2, D.base_t + 4))
            cutters.append(slot_cut_z(cx, sy * 141, 22, 8, D.base_t / 2, D.base_t + 4))

    # Battery strap and main cable pass-through slots.
    for x in [-48, 48]:
        cutters.append(slot_cut_z(x, -28, 8, 46, D.base_t / 2, D.base_t + 4))
        cutters.append(slot_cut_z(x, 28, 8, 46, D.base_t / 2, D.base_t + 4))
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            cutters.append(slot_cut_z(sx * 122, sy * 70, 18, 10, D.base_t / 2, D.base_t + 4))

    return difference(plate, cutters)


def split_base(full: trimesh.Trimesh) -> dict[str, trimesh.Trimesh]:
    margin = 2
    zc = D.base_t / 2
    specs = {
        "base_plate_front_left.stl": ((D.base_len / 4, D.base_w / 4, zc), (D.base_len / 2 + margin, D.base_w / 2 + margin, D.base_t + 4)),
        "base_plate_front_right.stl": ((D.base_len / 4, -D.base_w / 4, zc), (D.base_len / 2 + margin, D.base_w / 2 + margin, D.base_t + 4)),
        "base_plate_rear_left.stl": ((-D.base_len / 4, D.base_w / 4, zc), (D.base_len / 2 + margin, D.base_w / 2 + margin, D.base_t + 4)),
        "base_plate_rear_right.stl": ((-D.base_len / 4, -D.base_w / 4, zc), (D.base_len / 2 + margin, D.base_w / 2 + margin, D.base_t + 4)),
    }
    return {name: intersection(full, box(size, center)) for name, (center, size) in specs.items()}


def seam_joiner(length: float, name: str) -> trimesh.Trimesh:
    mesh = box((length, 20, 5), (0, 0, 2.5))
    points = [(x, -7) for x in np.linspace(-length / 2 + 15, length / 2 - 15, 4)]
    points += [(x, 7) for x in np.linspace(-length / 2 + 15, length / 2 - 15, 4)]
    return difference(mesh, hole_grid_z(points, 3.4, 2.5, 9))


def electronics_tray(size: tuple[float, float], bosses: list[tuple[float, float]], slots: list[tuple[float, float, float, float]]) -> trimesh.Trimesh:
    sx, sy = size
    parts: list[trimesh.Trimesh] = [box((sx, sy, 4), (0, 0, 2))]
    for x, y in bosses:
        parts.append(cyl_z(4.5, 8, (x, y, 8), 32))
    mesh = union(parts)
    cutters = hole_grid_z(bosses, 3.0, 7, 16)
    for x, y, lx, ly in slots:
        cutters.append(slot_cut_z(x, y, lx, ly, 3, 12))
    return difference(mesh, cutters)


def battery_sled() -> trimesh.Trimesh:
    base = box((155, 64, 5), (0, 0, 2.5))
    rails = [
        box((155, 4, 11), (0, 29, 5.5)),
        box((155, 4, 11), (0, -29, 5.5)),
        box((4, 56, 11), (-75, 0, 5.5)),
    ]
    mesh = union([base, *rails])
    cutters = []
    for x in [-45, 45]:
        cutters.append(slot_cut_z(x, 0, 8, 52, 3, 12))
    for x in [-67, 67]:
        cutters.append(cyl_z(1.7, 12, (x, 22, 3), 24))
        cutters.append(cyl_z(1.7, 12, (x, -22, 3), 24))
    return difference(mesh, cutters)


def pi_companion_tray() -> trimesh.Trimesh:
    """Tray for a Raspberry Pi 4/5-size companion computer footprint."""
    bosses = [(-29, -24.5), (29, -24.5), (-29, 24.5), (29, 24.5)]
    slots = [(-42, 0, 7, 56), (42, 0, 7, 56), (0, -33, 78, 6), (0, 33, 78, 6)]
    tray = electronics_tray((D.pi_tray_len, D.pi_tray_w), bosses, slots)
    fence = [
        box((D.pi_tray_len, 4, 9), (0, D.pi_tray_w / 2 - 2, 6.5)),
        box((D.pi_tray_len, 4, 9), (0, -D.pi_tray_w / 2 + 2, 6.5)),
    ]
    return union([tray, *fence])


def lte_modem_tray() -> trimesh.Trimesh:
    base = box((D.lte_tray_len, D.lte_tray_w, 4), (0, 0, 2))
    rails = [
        box((D.lte_tray_len, 4, 9), (0, D.lte_tray_w / 2 - 2, 6.5)),
        box((D.lte_tray_len, 4, 9), (0, -D.lte_tray_w / 2 + 2, 6.5)),
        box((4, D.lte_tray_w - 6, 9), (-D.lte_tray_len / 2 + 2, 0, 6.5)),
    ]
    cutters = [
        slot_cut_z(-28, 0, 7, D.lte_tray_w - 10, 3, 12),
        slot_cut_z(28, 0, 7, D.lte_tray_w - 10, 3, 12),
        cyl_z(1.7, 10, (-40, 14, 3), 24),
        cyl_z(1.7, 10, (-40, -14, 3), 24),
        cyl_z(1.7, 10, (40, 14, 3), 24),
        cyl_z(1.7, 10, (40, -14, 3), 24),
    ]
    return difference(union([base, *rails]), cutters)


def telemetry_sensor_plate() -> trimesh.Trimesh:
    plate = box((82, 50, 4), (0, 0, 2))
    label_rail = [
        box((82, 3, 5), (0, 23.5, 6.5)),
        box((82, 3, 5), (0, -23.5, 6.5)),
    ]
    cutters = [
        # Pololu ACS724 mounting holes and generic divider-board tie slots.
        cyl_z(1.35, 10, (-24, -12, 3), 24),
        cyl_z(1.35, 10, (-24, 12, 3), 24),
        cyl_z(1.35, 10, (24, -12, 3), 24),
        cyl_z(1.35, 10, (24, 12, 3), 24),
        slot_cut_z(0, 0, 56, 6, 3, 12),
        slot_cut_z(-35, 0, 6, 34, 3, 12),
        slot_cut_z(35, 0, 6, 34, 3, 12),
    ]
    return difference(union([plate, *label_rail]), cutters)


def buck_converter_plate() -> trimesh.Trimesh:
    plate = box((72, 42, 4), (0, 0, 2))
    cutters = [
        cyl_z(1.7, 10, (-28, -14, 3), 24),
        cyl_z(1.7, 10, (-28, 14, 3), 24),
        cyl_z(1.7, 10, (28, -14, 3), 24),
        cyl_z(1.7, 10, (28, 14, 3), 24),
        slot_cut_z(0, 0, 52, 6, 3, 12),
    ]
    return difference(plate, cutters)


def cargo_floor_full() -> trimesh.Trimesh:
    floor = box((D.cargo_floor_len, D.cargo_floor_w, D.cargo_floor_t), (0, 0, D.cargo_floor_t / 2))
    cutters: list[trimesh.Trimesh] = []

    # Screws down into the four shelf support blocks.
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            cutters.append(cyl_z(1.7, D.cargo_floor_t + 4, (sx * 127, sy * 100, D.cargo_floor_t / 2), 24))
            cutters.append(slot_cut_z(sx * 134, sy * 102.5, 8, 18, D.cargo_floor_t / 2, D.cargo_floor_t + 4))

    # Retainer-rail mounting holes around the food-safe box footprint.
    for sy in [-1, 1]:
        for x in [-88, 0, 88]:
            cutters.append(cyl_z(1.7, D.cargo_floor_t + 4, (x, sy * 82, D.cargo_floor_t / 2), 24))
    for sx in [-1, 1]:
        for y in [-58, 58]:
            cutters.append(cyl_z(1.7, D.cargo_floor_t + 4, (sx * 114, y, D.cargo_floor_t / 2), 24))

    return difference(floor, cutters)


def split_cargo_floor(full: trimesh.Trimesh) -> dict[str, trimesh.Trimesh]:
    margin = 2
    zc = D.cargo_floor_t / 2
    specs = {
        "cargo_floor_front_left.stl": (
            (D.cargo_floor_len / 4, D.cargo_floor_w / 4, zc),
            (D.cargo_floor_len / 2 + margin, D.cargo_floor_w / 2 + margin, D.cargo_floor_t + 4),
        ),
        "cargo_floor_front_right.stl": (
            (D.cargo_floor_len / 4, -D.cargo_floor_w / 4, zc),
            (D.cargo_floor_len / 2 + margin, D.cargo_floor_w / 2 + margin, D.cargo_floor_t + 4),
        ),
        "cargo_floor_rear_left.stl": (
            (-D.cargo_floor_len / 4, D.cargo_floor_w / 4, zc),
            (D.cargo_floor_len / 2 + margin, D.cargo_floor_w / 2 + margin, D.cargo_floor_t + 4),
        ),
        "cargo_floor_rear_right.stl": (
            (-D.cargo_floor_len / 4, -D.cargo_floor_w / 4, zc),
            (D.cargo_floor_len / 2 + margin, D.cargo_floor_w / 2 + margin, D.cargo_floor_t + 4),
        ),
    }
    return {name: intersection(full, box(size, center)) for name, (center, size) in specs.items()}


def cargo_shelf_support_block() -> trimesh.Trimesh:
    block = box((28, 22, 12), (0, 0, 6))
    cutters = [
        cyl_z(1.7, 16, (0, 0, 6), 24),
        cyl_axis("x", 1.7, 34, (0, 0, 6), 24),
        cyl_axis("y", 1.7, 30, (0, 0, 6), 24),
    ]
    return difference(block, cutters)


def cargo_retainer_long_rail() -> trimesh.Trimesh:
    rail = box((224, 8, D.cargo_rail_h), (0, 0, D.cargo_rail_h / 2))
    cutters = [cyl_z(1.7, D.cargo_rail_h + 4, (x, 0, D.cargo_rail_h / 2), 24) for x in [-88, 0, 88]]
    return difference(rail, cutters)


def cargo_retainer_short_rail() -> trimesh.Trimesh:
    rail = box((8, 156, D.cargo_rail_h), (0, 0, D.cargo_rail_h / 2))
    cutters = [cyl_z(1.7, D.cargo_rail_h + 4, (0, y, D.cargo_rail_h / 2), 24) for y in [-58, 58]]
    return difference(rail, cutters)


def food_box_placeholder() -> trimesh.Trimesh:
    return box((D.max_food_box_len, D.max_food_box_w, D.max_food_box_h), (0, 0, D.max_food_box_h / 2))


def side_panel(half: str) -> trimesh.Trimesh:
    panel = box((150, D.body_h, D.panel_t), (0, D.body_h / 2, D.panel_t / 2))
    ribs = [
        box((142, 5, 3), (0, 48, D.panel_t + 1.5)),
        box((132, 5, 3), (0, 88, D.panel_t + 1.5)),
    ]
    mesh = union([panel, *ribs])
    holes = []
    x_edge = -65 if half == "front" else 65
    for x in [x_edge, -x_edge]:
        for y in [22, 80, 137]:
            holes.append(cyl_z(1.7, D.panel_t + 8, (x, y, D.panel_t / 2), 24))
    return difference(mesh, holes)


def front_rear_panel(front: bool, side: str) -> trimesh.Trimesh:
    panel = box((115, D.body_h, D.panel_t), (0, D.body_h / 2, D.panel_t / 2))
    lip = box((105, 5, 3), (0, D.body_h - 18, D.panel_t + 1.5))
    mesh = union([panel, lip])
    cutters: list[trimesh.Trimesh] = []
    for x in [-48, 48]:
        for y in [22, 80, 137]:
            cutters.append(cyl_z(1.7, D.panel_t + 8, (x, y, D.panel_t / 2), 24))
    # Center seam holes.
    seam_x = 53 if side == "left" else -53
    for y in [28, 78, 128]:
        cutters.append(cyl_z(1.7, D.panel_t + 8, (seam_x, y, D.panel_t / 2), 24))
    if front:
        # HC-SR04 openings: two transducer holes and two small module screws.
        sensor_x = -14 if side == "left" else 14
        for dx in [-13, 13]:
            cutters.append(cyl_z(8.5, D.panel_t + 8, (sensor_x + dx, 72, D.panel_t / 2), 48))
        for dx in [-23, 23]:
            cutters.append(cyl_z(1.35, D.panel_t + 8, (sensor_x + dx, 93, D.panel_t / 2), 24))
        # Front LED diffuser slot, split across the two front panels.
        cutters.append(slot_cut_z(0, 126, 96, 8, D.panel_t / 2, D.panel_t + 8))
        # Camera mount holes are split across the front panel halves.
        for x in [-34, 34]:
            cutters.append(cyl_z(1.7, D.panel_t + 8, (x, 112, D.panel_t / 2), 24))
    else:
        # Rear camera mount holes.
        for x in [-34, 34]:
            cutters.append(cyl_z(1.7, D.panel_t + 8, (x, 112, D.panel_t / 2), 24))
    return difference(mesh, cutters)


def corner_post() -> trimesh.Trimesh:
    post = box((D.post_size, D.post_size, D.body_h), (0, 0, D.body_h / 2))
    cutters: list[trimesh.Trimesh] = []
    for z in [22, 80, 137]:
        cutters.append(cyl_axis("x", 1.7, D.post_size + 8, (0, 0, z), 24))
        cutters.append(cyl_axis("y", 1.7, D.post_size + 8, (0, 0, z), 24))
    for offset in [-6, 6]:
        cutters.append(cyl_axis("x", 1.7, D.post_size + 8, (0, offset, D.cargo_support_hole_z), 24))
        cutters.append(cyl_axis("y", 1.7, D.post_size + 8, (offset, 0, D.cargo_support_hole_z), 24))
    cutters.append(cyl_z(1.45, D.body_h + 4, (0, 0, D.body_h / 2), 24))
    return difference(post, cutters)


def panel_joiner() -> trimesh.Trimesh:
    bar = box((20, D.body_h, 4), (0, D.body_h / 2, 2))
    cutters = [cyl_z(1.7, 10, (0, y, 2), 24) for y in [28, 78, 128]]
    return difference(bar, cutters)


def lid_quadrant() -> trimesh.Trimesh:
    lid = box((D.body_len / 2, D.body_w / 2, D.lid_t), (0, 0, D.lid_t / 2))
    rim = [
        box((D.body_len / 2, 5, 6), (0, D.body_w / 4 - 2.5, D.lid_t + 3)),
        box((5, D.body_w / 2, 6), (D.body_len / 4 - 2.5, 0, D.lid_t + 3)),
    ]
    mesh = union([lid, *rim])
    holes = [
        cyl_z(1.7, 12, (D.body_len / 4 - 14, D.body_w / 4 - 14, D.lid_t / 2), 24),
        cyl_z(1.7, 12, (-D.body_len / 4 + 14, D.body_w / 4 - 14, D.lid_t / 2), 24),
        cyl_z(1.7, 12, (D.body_len / 4 - 14, -D.body_w / 4 + 14, D.lid_t / 2), 24),
    ]
    return difference(mesh, holes)


def camera_module_mount() -> trimesh.Trimesh:
    plate = box((D.camera_mount_w, D.camera_mount_h, D.camera_mount_t), (0, 0, D.camera_mount_t / 2))
    shade = box((D.camera_mount_w, 8, 9), (0, D.camera_mount_h / 2 - 4, D.camera_mount_t + 4.5))
    side_lips = [
        box((5, D.camera_mount_h, 7), (D.camera_mount_w / 2 - 2.5, 0, D.camera_mount_t + 3.5)),
        box((5, D.camera_mount_h, 7), (-D.camera_mount_w / 2 + 2.5, 0, D.camera_mount_t + 3.5)),
    ]
    mesh = union([plate, shade, *side_lips])
    cutters = [
        cyl_z(8.5, D.camera_mount_t + 16, (0, 0, D.camera_mount_t / 2), 48),
        cyl_z(1.2, D.camera_mount_t + 16, (-10.5, -10.5, D.camera_mount_t / 2), 24),
        cyl_z(1.2, D.camera_mount_t + 16, (10.5, -10.5, D.camera_mount_t / 2), 24),
        cyl_z(1.2, D.camera_mount_t + 16, (-10.5, 10.5, D.camera_mount_t / 2), 24),
        cyl_z(1.2, D.camera_mount_t + 16, (10.5, 10.5, D.camera_mount_t / 2), 24),
        cyl_z(1.7, D.camera_mount_t + 16, (-26, 15, D.camera_mount_t / 2), 24),
        cyl_z(1.7, D.camera_mount_t + 16, (26, 15, D.camera_mount_t / 2), 24),
        cyl_z(1.7, D.camera_mount_t + 16, (-26, -15, D.camera_mount_t / 2), 24),
        cyl_z(1.7, D.camera_mount_t + 16, (26, -15, D.camera_mount_t / 2), 24),
        slot_cut_z(-20, 0, 4, 30, D.camera_mount_t / 2, D.camera_mount_t + 16),
        slot_cut_z(20, 0, 4, 30, D.camera_mount_t / 2, D.camera_mount_t + 16),
    ]
    return difference(mesh, cutters)


def micro_servo_lid_lock_mount() -> trimesh.Trimesh:
    # Flat cradle for an MG90S/SG90-size servo. Zip ties wrap through the slots.
    base = box((56, 36, 4), (0, 0, 2))
    side_rails = [
        box((56, 4, 15), (0, 16, 9.5)),
        box((56, 4, 15), (0, -16, 9.5)),
        box((4, 28, 15), (-26, 0, 9.5)),
    ]
    boss = box((16, 28, 8), (24, 0, 8))
    mesh = union([base, *side_rails, boss])
    cutters = [
        slot_cut_z(-12, 0, 7, 28, 3, 12),
        slot_cut_z(10, 0, 7, 28, 3, 12),
        cyl_z(1.7, 10, (-22, -12, 3), 24),
        cyl_z(1.7, 10, (-22, 12, 3), 24),
        cyl_z(1.7, 10, (22, -12, 3), 24),
        cyl_z(1.7, 10, (22, 12, 3), 24),
    ]
    return difference(mesh, cutters)


def lid_lock_cam() -> trimesh.Trimesh:
    cam = union(
        [
            cyl_z(9, 4, (0, 0, 2), 48),
            box((38, 10, 4), (16, 0, 2)),
        ]
    )
    cutters = [
        cyl_z(1.2, 8, (0, 0, 2), 24),
        cyl_z(1.0, 8, (5, 0, 2), 16),
        cyl_z(1.0, 8, (-5, 0, 2), 16),
    ]
    return difference(cam, cutters)


def lid_lock_keeper() -> trimesh.Trimesh:
    plate = box((70, 18, 4), (0, 0, 2))
    catch_lip = box((42, 5, 8), (0, -6.5, 8))
    mesh = union([plate, catch_lip])
    cutters = [
        cyl_z(1.7, 14, (-25, 0, 3), 24),
        cyl_z(1.7, 14, (25, 0, 3), 24),
        slot_cut_z(0, 3, 30, 7, 4, 16),
    ]
    return difference(mesh, cutters)


def wheel_cap() -> trimesh.Trimesh:
    cap = cyl_z(50, 4, (0, 0, 2), 96)
    hub_recess = cyl_z(13, 8, (0, 0, 2), 64)
    screw_holes = []
    for a in np.linspace(0, math.tau, 6, endpoint=False):
        screw_holes.append(cyl_z(1.7, 10, (12 * math.cos(a), 12 * math.sin(a), 2), 24))
    return difference(cap, [hub_recess, *screw_holes])


def led_diffuser() -> trimesh.Trimesh:
    # Print in clear/translucent PETG or natural PLA.
    bar = box((230, 6, 2.4), (0, 0, 1.2))
    return bar


def motor_spacer() -> trimesh.Trimesh:
    block = box((62, 18, 8), (0, 0, 4))
    cutters = [slot_cut_z(x, 0, 8, 14, 4, 12) for x in [-22, 22]]
    cutters.append(cyl_axis("y", 19, 28, (0, 0, 4), 64))
    return difference(block, cutters)


def load_existing_original_base() -> trimesh.Trimesh | None:
    parts = sorted((ROOT / "3D Prints").glob("*.stl"))
    if not parts:
        return None
    meshes = [trimesh.load_mesh(p) for p in parts]
    merged = combine(meshes)
    merged.merge_vertices()
    merged.remove_unreferenced_vertices()
    return merged


def transform_copy(mesh: trimesh.Trimesh, translation=(0, 0, 0), rotation=None) -> trimesh.Trimesh:
    m = mesh.copy()
    if rotation is not None:
        angle, axis = rotation
        m.apply_transform(trimesh.transformations.rotation_matrix(angle, axis))
    m.apply_translation(translation)
    return m


def add_cargo_bay_parts(parts: list[trimesh.Trimesh], include_food_box: bool) -> None:
    support = cargo_shelf_support_block()
    support_z = D.base_t + D.cargo_floor_z - 12
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            parts.append(transform_copy(support, (sx * 127, sy * 100, support_z)))

    cargo_floor = cargo_floor_full()
    floor_z = D.base_t + D.cargo_floor_z
    floor_top = floor_z + D.cargo_floor_t
    parts.append(transform_copy(cargo_floor, (0, 0, floor_z)))

    long_rail = cargo_retainer_long_rail()
    short_rail = cargo_retainer_short_rail()
    for sy in [-1, 1]:
        parts.append(transform_copy(long_rail, (0, sy * 82, floor_top)))
    for sx in [-1, 1]:
        parts.append(transform_copy(short_rail, (sx * 114, 0, floor_top)))

    if include_food_box:
        parts.append(transform_copy(food_box_placeholder(), (0, 0, floor_top + 2)))


def add_v2_feature_mounts(parts: list[trimesh.Trimesh]) -> None:
    camera = camera_module_mount()
    front_camera = transform_copy(camera, rotation=(math.pi / 2, [0, 1, 0]))
    front_camera.apply_translation((D.body_len / 2 + 8, 0, D.base_t + 118))
    rear_camera = transform_copy(camera, rotation=(-math.pi / 2, [0, 1, 0]))
    rear_camera.apply_translation((-D.body_len / 2 - 8, 0, D.base_t + 118))
    parts.extend([front_camera, rear_camera])

    servo = transform_copy(micro_servo_lid_lock_mount(), rotation=(math.pi / 2, [0, 1, 0]))
    servo.apply_translation((-D.body_len / 2 + 20, 0, D.base_t + D.body_h - 34))
    keeper = transform_copy(lid_lock_keeper(), rotation=(math.pi / 2, [0, 1, 0]))
    keeper.apply_translation((-D.body_len / 2 + 4, 0, D.base_t + D.body_h - 10))
    cam = transform_copy(lid_lock_cam(), rotation=(math.pi / 2, [0, 1, 0]))
    cam.apply_translation((-D.body_len / 2 + 2, 0, D.base_t + D.body_h - 30))
    parts.extend([servo, keeper, cam])


def electronics_layout_assembly(base: trimesh.Trimesh) -> trimesh.Trimesh:
    parts: list[trimesh.Trimesh] = [base]
    parts.append(transform_copy(battery_sled(), (-66, 0, D.base_t)))
    parts.append(transform_copy(pi_companion_tray(), (58, 58, D.base_t)))
    parts.append(transform_copy(electronics_tray((145, 92), [(-52, -28), (45, -28), (-52, 26), (45, 26)], [(-5, -40, 92, 6), (-5, 39, 92, 6)]), (54, -64, D.base_t)))
    parts.append(transform_copy(lte_modem_tray(), (-90, 72, D.base_t)))
    parts.append(transform_copy(telemetry_sensor_plate(), (-92, -56, D.base_t)))
    parts.append(transform_copy(buck_converter_plate(), (-8, 0, D.base_t)))
    return combine(parts)


def reference_assembly(base: trimesh.Trimesh, include_lid: bool = True, include_food_box: bool = True) -> trimesh.Trimesh:
    parts: list[trimesh.Trimesh] = [base]

    # Visual placeholders for motors and wheels.
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            parts.append(cyl_axis("y", D.motor_d / 2, D.motor_len, (sx * D.motor_x, sy * 156, D.motor_z), 64))
            parts.append(cyl_axis("y", D.motor_shaft_d / 2, D.motor_shaft_len, (sx * D.motor_x, sy * 190, D.motor_z), 32))
            parts.append(cyl_axis("y", D.wheel_d / 2, D.wheel_w, (sx * D.motor_x, sy * 226, D.motor_z), 96))

    # Body posts.
    post = corner_post()
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            parts.append(transform_copy(post, (sx * (D.body_len / 2 - 9), sy * (D.body_w / 2 - 9), D.base_t)))

    # Body panels placed vertical around the posts.
    side = side_panel("front")
    for sy in [-1, 1]:
        for sx, xoff in [(1, 75), (-1, -75)]:
            panel = transform_copy(side, rotation=(math.pi / 2, [1, 0, 0]))
            panel.apply_translation((xoff, sy * (D.body_w / 2 + D.panel_t / 2), D.base_t))
            parts.append(panel)

    front_l = front_rear_panel(True, "left")
    front_r = front_rear_panel(True, "right")
    rear_l = front_rear_panel(False, "left")
    rear_r = front_rear_panel(False, "right")
    for front, meshes in [(1, [front_l, front_r]), (-1, [rear_l, rear_r])]:
        for sy_idx, mesh in enumerate(meshes):
            yoff = 57.5 if sy_idx == 0 else -57.5
            p = transform_copy(mesh, rotation=(math.pi / 2, [1, 0, 0]))
            p.apply_transform(trimesh.transformations.rotation_matrix(math.pi / 2, [0, 0, 1]))
            p.apply_translation((front * (D.body_len / 2 + D.panel_t / 2), yoff, D.base_t))
            parts.append(p)

    # Internal cargo shelf: food rides above this; battery and electronics stay below it.
    add_cargo_bay_parts(parts, include_food_box)

    # Lid quadrants.
    if include_lid:
        lid = lid_quadrant()
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                p = transform_copy(lid, (sx * D.body_len / 4, sy * D.body_w / 4, D.base_t + D.body_h))
                parts.append(p)

    add_v2_feature_mounts(parts)

    return combine(parts)


def render_meshes(
    meshes: list[trimesh.Trimesh],
    out_path: Path,
    title: str,
    size=(1400, 1000),
    yaw_deg: float = 38,
    pitch_deg: float = 24,
) -> None:
    # Lightweight software isometric renderer. It intentionally avoids OpenGL so
    # this script works in headless CI and on a fresh laptop.
    verts_all = []
    faces_payload = []
    offset = 0
    for idx, mesh in enumerate(meshes):
        verts = np.asarray(mesh.vertices)
        faces = np.asarray(mesh.faces)
        verts_all.append(verts)
        faces_payload.append((faces + offset, idx))
        offset += len(verts)
    vertices = np.vstack(verts_all)
    center = vertices.mean(axis=0)
    vertices = vertices - center

    yaw = math.radians(yaw_deg)
    pitch = math.radians(pitch_deg)
    rz = np.array(
        [
            [math.cos(yaw), -math.sin(yaw), 0],
            [math.sin(yaw), math.cos(yaw), 0],
            [0, 0, 1],
        ]
    )
    rx = np.array(
        [
            [1, 0, 0],
            [0, math.cos(pitch), -math.sin(pitch)],
            [0, math.sin(pitch), math.cos(pitch)],
        ]
    )
    camera = vertices @ rz.T @ rx.T
    xy = camera[:, :2]
    span = np.ptp(xy, axis=0).max()
    scale = min(size) * 0.78 / span
    xy = xy * scale
    xy[:, 0] += size[0] / 2
    xy[:, 1] = size[1] / 2 - xy[:, 1]

    img = Image.new("RGB", size, "#f6f7f8")
    draw = ImageDraw.Draw(img)
    light = np.array([0.35, -0.55, 0.75])
    light = light / np.linalg.norm(light)
    colors = [
        np.array([235, 238, 240]),
        np.array([70, 76, 84]),
        np.array([245, 245, 245]),
        np.array([200, 210, 222]),
    ]

    triangles = []
    for faces, idx in faces_payload:
        for f in faces:
            pts3 = camera[f]
            depth = pts3[:, 2].mean()
            normal = np.cross(pts3[1] - pts3[0], pts3[2] - pts3[0])
            n_norm = np.linalg.norm(normal)
            if n_norm == 0:
                continue
            normal = normal / n_norm
            shade = 0.45 + 0.55 * max(0, float(np.dot(normal, light)))
            color = np.clip(colors[idx % len(colors)] * shade, 0, 255).astype(int)
            triangles.append((depth, f, tuple(color.tolist())))
    for _, f, color in sorted(triangles, key=lambda item: item[0]):
        pts = [tuple(xy[i]) for i in f]
        draw.polygon(pts, fill=color)
        draw.line(pts + [pts[0]], fill="#c9cdd2", width=1)
    draw.text((24, 22), title, fill="#1f2933")
    img.save(out_path)


def write_manifest(paths: list[Path]) -> None:
    payload = {
        "units": "millimeters",
        "coordinate_system": "assembled reference uses X=front/rear, Y=left/right, Z=up; print files are already laid flat where practical",
        "generated_files": [str(p.relative_to(ROOT)) for p in paths],
        "critical_dimensions": D.__dict__,
    }
    (CAD_ROOT / "source" / "generated_manifest.json").write_text(json.dumps(payload, indent=2) + "\n")


def main() -> None:
    ensure_dirs()
    generated: list[Path] = []

    original = load_existing_original_base()
    if original is not None:
        generated.append(export(original, "full-size/original_four_piece_base_merged_full_size.stl"))

    base = base_plate_full()
    generated.append(export(base, "full-size/v2_base_plate_full_size.stl"))
    for name, mesh in split_base(base).items():
        generated.append(export(mesh, f"chassis/{name}"))

    generated.append(export(seam_joiner(155, "long"), "chassis/base_seam_joiner_long_print_2.stl"))
    generated.append(export(seam_joiner(145, "short"), "chassis/base_seam_joiner_short_print_2.stl"))
    generated.append(export(motor_spacer(), "chassis/printed_37d_motor_spacer_print_4.stl"))

    generated.append(
        export(
            electronics_tray(
                (145, 92),
                [(-52, -28), (45, -28), (-52, 26), (45, 26)],
                [(-5, -40, 92, 6), (-5, 39, 92, 6)],
            ),
            "electronics/arduino_mega_controller_tray.stl",
        )
    )
    driver_bosses = [(-48, -25), (-2, -25), (48, -25), (-48, 25), (-2, 25), (48, 25)]
    generated.append(
        export(
            electronics_tray((136, 72), driver_bosses, [(0, 0, 118, 6)]),
            "electronics/bts7960_dual_driver_tray_print_2.stl",
        )
    )
    generated.append(export(battery_sled(), "electronics/3s_lipo_battery_sled.stl"))
    generated.append(export(pi_companion_tray(), "electronics/raspberry_pi_companion_tray.stl"))
    generated.append(export(lte_modem_tray(), "electronics/usb_lte_modem_tray.stl"))
    generated.append(export(telemetry_sensor_plate(), "electronics/battery_telemetry_sensor_plate.stl"))
    generated.append(export(buck_converter_plate(), "electronics/buck_converter_plate_print_2.stl"))

    cargo_floor = cargo_floor_full()
    for name, mesh in split_cargo_floor(cargo_floor).items():
        generated.append(export(mesh, f"cargo/{name}"))
    generated.append(export(cargo_shelf_support_block(), "cargo/cargo_shelf_support_block_print_4.stl"))
    generated.append(export(cargo_retainer_long_rail(), "cargo/cargo_retainer_long_rail_print_2.stl"))
    generated.append(export(cargo_retainer_short_rail(), "cargo/cargo_retainer_short_rail_print_2.stl"))

    generated.append(export(side_panel("front"), "body/side_panel_front_half_print_2.stl"))
    generated.append(export(side_panel("rear"), "body/side_panel_rear_half_print_2.stl"))
    generated.append(export(front_rear_panel(True, "left"), "body/front_panel_left_hcsr04_led.stl"))
    generated.append(export(front_rear_panel(True, "right"), "body/front_panel_right_hcsr04_led.stl"))
    generated.append(export(front_rear_panel(False, "left"), "body/rear_panel_left.stl"))
    generated.append(export(front_rear_panel(False, "right"), "body/rear_panel_right.stl"))
    generated.append(export(corner_post(), "body/corner_post_print_4.stl"))
    generated.append(export(panel_joiner(), "body/panel_center_joiner_print_4.stl"))
    generated.append(export(lid_quadrant(), "body/lid_quadrant_print_4.stl"))
    generated.append(export(camera_module_mount(), "body/camera_module_mount_print_2.stl"))
    generated.append(export(micro_servo_lid_lock_mount(), "body/micro_servo_lid_lock_mount.stl"))
    generated.append(export(lid_lock_cam(), "body/lid_lock_servo_cam.stl"))
    generated.append(export(lid_lock_keeper(), "body/lid_lock_keeper_plate.stl"))

    generated.append(export(wheel_cap(), "accessories/wheel_white_cap_print_4.stl"))
    generated.append(export(led_diffuser(), "accessories/front_led_diffuser_clear_print_1.stl"))

    assembly = reference_assembly(base)
    generated.append(export(assembly, "full-size/v2_robot_complete_reference_not_for_print.stl"))
    cargo_open = reference_assembly(base, include_lid=False)
    electronics_layout = electronics_layout_assembly(base)

    render_meshes([assembly], RENDER_OUT / "checkpoint_2_complete_robot_iso.png", "Checkpoint 2: v2.2 complete robot reference")
    render_meshes(
        [assembly],
        RENDER_OUT / "checkpoint_2_complete_robot_low_angle.png",
        "Checkpoint 2: v2.2 low angle wheel/body clearance",
        yaw_deg=18,
        pitch_deg=8,
    )
    render_meshes(
        [cargo_open],
        RENDER_OUT / "checkpoint_3_cargo_bay_lid_removed.png",
        "Checkpoint 3: v2.2 lid removed, lock and cargo bay visible",
        yaw_deg=32,
        pitch_deg=34,
    )
    render_meshes([base], RENDER_OUT / "checkpoint_2_base_top.png", "Checkpoint 2: chassis base top")
    render_meshes(
        [electronics_layout],
        RENDER_OUT / "checkpoint_4_electronics_layout.png",
        "Checkpoint 4: v2.2 electronics layout with Pi, LTE, telemetry",
        yaw_deg=34,
        pitch_deg=36,
    )
    sample_parts = [
        transform_copy(front_rear_panel(True, "left"), (-180, 0, 0)),
        transform_copy(front_rear_panel(True, "right"), (-55, 0, 0)),
        transform_copy(side_panel("front"), (85, 0, 0)),
        transform_copy(lid_quadrant(), (250, 20, 0)),
        transform_copy(camera_module_mount(), (360, 0, 0)),
        transform_copy(micro_servo_lid_lock_mount(), (455, 0, 0)),
    ]
    render_meshes(sample_parts, RENDER_OUT / "checkpoint_2_printed_panel_samples.png", "Checkpoint 2: v2.2 representative print parts")
    cargo_parts = [
        cargo_floor,
        transform_copy(cargo_retainer_long_rail(), (0, 82, D.cargo_floor_t)),
        transform_copy(cargo_retainer_long_rail(), (0, -82, D.cargo_floor_t)),
        transform_copy(cargo_retainer_short_rail(), (114, 0, D.cargo_floor_t)),
        transform_copy(cargo_retainer_short_rail(), (-114, 0, D.cargo_floor_t)),
        transform_copy(food_box_placeholder(), (0, 0, D.cargo_floor_t + 2)),
    ]
    render_meshes(cargo_parts, RENDER_OUT / "checkpoint_3_cargo_shelf_and_food_box.png", "Checkpoint 3: cargo shelf and max food box")

    write_manifest(generated)
    print(f"Generated {len(generated)} STL files")
    for path in generated:
        print(path.relative_to(ROOT))
    print(f"Rendered previews in {RENDER_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

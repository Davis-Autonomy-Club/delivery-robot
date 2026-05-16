# View The Whole Robot

Open this file to inspect the assembled minimum robot:

`OPEN_ME_complete_robot_reference.stl`

This is an assembly/reference model only. Do not slice this file for printing. Use the individual STL files in `cad/print-ready/` when printing parts.

The reference model should show the split chassis, four-wheel drivetrain envelope, simple body, upper cargo shelf, max-size food-box placeholder, and removable lid. It should not include Pi/LTE/camera/servo-lock hardware in the baseline. The outdoor underbody splash sheet is intentionally hand-cut from flat sheet stock and is not shown in this STL.

Also included:

`OPEN_ME_full_base_plate_reference.stl`

This shows the complete one-piece base plate. Most printers should still print the four split base pieces from `cad/print-ready/chassis/`.

## Recommended Viewers

- PrusaSlicer, OrcaSlicer, Bambu Studio, Cura: drag the STL into the build plate to orbit around it.
- FreeCAD or MeshLab: open the STL for a more CAD-like model viewer.
- macOS: Quick Look may preview the STL, but a slicer or FreeCAD gives better orbit/zoom controls.

# Raking Light

Raking Light is an open-source digital studio for designing artistic relief
wall panels that can be manufactured efficiently on a CNC router.

The intended workflow is:

```text
commercial and artistic references
-> original parametric surface studies
-> Blender lighting and material previews
-> manufacturability and cutting-effort review
-> verified machine instructions
```

The project is currently building a cheap digital feedback loop. Its first
studies recreate the geometric principles behind existing routed wall-panel
products in Blender, then deliberately vary them into original designs. The
goal is to learn which forms look good under raking light while remaining fast
to machine.

## Current boundary

- Blender is the first digital studio and renderer.
- Reference products are studied for geometry, repetition, lighting behaviour,
  and manufacturing strategy; their exact decorative patterns are not copied.
- Designs must be plausible for three-axis routing from sheet or panel stock.
- Each study records likely tool choice, pass count, tool changes, and a rough
  cutting-effort class alongside the render.
- Simple repeated geometry is a feature when it produces a strong result with
  less machine time.
- G-code, LinuxCNC integration, and production feeds and speeds remain deferred
  until a design family is worth physically testing.
- The dual-image lighting idea is parked, not deleted. Its source brief and
  decisions remain as research history.

Digital studies are disposable research artifacts. Their implementation does
not constrain the eventual product architecture.

## Documents

- [Source brief](docs/source-brief.md)
- [Product decisions](docs/product-decisions.md)

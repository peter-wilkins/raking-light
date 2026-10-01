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
- Designs describe one composition across a whole wall. Sheet boundaries are a
  manufacturing constraint, not a reason to repeat the same panel pattern.
- Designs must be plausible for three-axis routing from sheet or panel stock.
- Each study records likely tool choice, pass count, tool changes, and a rough
  cutting-effort class alongside the render.
- Simple cutting logic is a feature when it produces a strong result with less
  machine time, but the resulting wall composition need not repeat.
- G-code, LinuxCNC integration, and production feeds and speeds remain deferred
  until a design family is worth physically testing.
- The dual-image lighting idea is parked, not deleted. Its source brief and
  decisions remain as research history.

Digital studies are disposable research artifacts. Their implementation does
not constrain the eventual product architecture.

## Run on Windows

1. Install [Blender 4.5 LTS](https://www.blender.org/download/lts/4-5/).
2. Download or clone this repository into a writable folder.
3. Double-click `run-studio.cmd`.

The launcher renders three lighting studies and opens the generated Blender
model. Outputs are saved in `artifacts/botanical-vbit-study/`. No separate Python
installation is required: the script runs inside Blender with its bundled NumPy.

For a portable Blender installation, run this in PowerShell from the project:

```powershell
.\scripts\run-studio.ps1 -BlenderPath 'C:\Tools\Blender\blender.exe'
```

Add `-RenderOnly` to generate the files without opening Blender. The Windows
launcher has been reviewed here but requires its first execution on Windows;
the underlying script has been rendered successfully on Linux with Blender 4.5.

## Documents

- [Source brief](docs/source-brief.md)
- [Product decisions](docs/product-decisions.md)
- [Wall-panel reference survey](docs/wall-panel-reference-survey.md)

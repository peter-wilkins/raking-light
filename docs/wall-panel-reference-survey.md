# Wall-Panel Reference Survey

## Purpose

Identify product families that can teach us how geometry, material, and raking
light create strong wall panels without committing to slow machining. These are
references for geometric principles, not patterns to reproduce for sale.

Manufacturing notes below are hypotheses to test in Blender and later CAM. They
are not claims about how the referenced manufacturers make each product.

## Reference families

### Linear grooves and louvers

Examples:

- [CoreBOO Groove panels](https://www.sustainablematerials.com/product/groove-panels/)
- [Caulfield CNC panelling](https://caulfieldcomposites.com/panelling.html)

Why study them:

- Strong shadow response from very simple repeated geometry.
- Plausible with one profile cutter and long continuous passes.
- Useful baseline for measuring how much visual value each minute of routing
  adds.

Likely effort: low.

### Faceted and pleated fields

Examples:

- [Plyboo Futura and related collections](https://www.plyboo.com/)
- [Plyboo Reveal collection](https://www.plyboo.com/products/walls/reveal-collection/)

Why study them:

- Angled faces create large tonal changes under raking light.
- Repetition, mirroring, and rotation can produce compositions from a small
  vocabulary of cuts.
- A V-bit or form cutter may create useful families without finish-machining
  every square millimetre.

Likely effort: low to medium, depending on whether facets can be expressed as
continuous cuts rather than individually pocketed cells.

### Continuous waves and topographic reliefs

Examples:

- [Craftsncreation parametric wave panel](https://www.craftsncreation.in/parametric-wave-panel-cnc-carving)
- [Designpanels Feather panel](https://designpanels.com/en-us/Products-en/Details-en-US/catid/992/eid/278)

Why study them:

- Visually fluid and clearly sculptural.
- A useful upper-bound comparison for surface quality.

Likely effort: high. Smooth freeform surfaces commonly imply close-spaced
ball-nose finishing passes across most of the sheet.

### Layer-revealing carved panels

Example:

- [Plyboo Reveal collection](https://www.plyboo.com/products/walls/reveal-collection/)

Why study them:

- The cut exposes a contrasting core, so material construction contributes to
  the image without paint or separate parts.
- Suggests future experiments with plywood, laminated colour, or waste composite
  sheet rather than treating geometry and material as independent.

Likely effort: medium to high and material-dependent.

## Recommended first Blender study

Build an original **whole-wall composition** whose relief can be represented by
straight continuous V-bit cuts. Start with stylised botanical or landscape
linework rather than a repeated panel cell. Render it under adjustable raking
light, then vary:

- line position, spacing, width, and depth;
- cut direction;
- the density used to describe focal and quiet areas;
- continuity across eventual sheet boundaries;
- wall aspect ratio and viewing distance;
- material colour and roughness.

This tests whether simple machining can carry an intentional wall-sized image.
The composition lives in wall coordinates; panel tiling is deferred until the
design has visual value.

## Comparison record for every study

Capture:

1. Render under neutral frontal light.
2. Render under raking light from at least two directions.
3. Panel dimensions and maximum relief depth.
4. Assumed stock and cutter.
5. Number and total length of conceptual cut lines.
6. Tool changes and assumed passes per line.
7. Relative routing effort: low, medium, or high.
8. What principle was learned from the reference.
9. What makes the resulting design original.

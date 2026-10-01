# Botanical V-bit Study 001

## Result

The Blender script successfully generated real recessed relief geometry and
rendered neutral, top-raking, and left-raking lighting states.

- Wall: 4.8 m x 2.4 m
- Material: painted 18 mm MDF
- Tool assumption: one 90-degree V-bit
- Conceptual paths: 24
- Total conceptual cut length: 36.56 m
- Naive cutting estimate at 3000 mm/min: 13.4 minutes
- Maximum depth: 9 mm
- Blender peak memory: approximately 212 MB
- Three-render run time: approximately 21 seconds

Generated artifacts are deliberately ignored by Git and live under
`artifacts/botanical-vbit-study/`.

## Verdict

The deterministic geometry-to-render loop is viable on the current laptop.
Raking light makes the cuts clear, but the composition reads as enlarged line
engraving rather than a sculptural wall panel. That is useful negative evidence.

The next study should accept editable vector paths and explore at least one of:

1. varying groove depth and width within a stroke;
2. paired cuts that create broad planar facets;
3. sparse filled or terraced regions among linework;
4. line-density fields that create large tonal masses at viewing distance.

Do not add G-code yet. First make the rendered wall desirable.

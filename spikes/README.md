# Disposable Spikes

These scripts answer design questions. They are not the product architecture.

## Botanical V-bit study

Generate a wall-sized botanical relief and render three lighting states:

```bash
blender --background \
  --python spikes/botanical_vbit_study.py \
  -- --output-dir artifacts/botanical-vbit-study
```

The study assumes a painted 18 mm MDF wall, one 90-degree V-bit, continuous
line cuts, and no tool changes. It creates geometry and manufacturing metadata,
but deliberately does not create G-code.


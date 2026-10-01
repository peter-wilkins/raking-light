# Raking Light

Raking Light is an open-source experiment in making relief panels that reveal
different images when illuminated from above or below.

The intended workflow is:

```text
two source images
-> one physical surface description
-> lighting simulation
-> verified machine instructions
```

The project is currently in product and optical-feasibility discovery. It does
not yet generate production-ready G-code.

## MVP boundary

- The viewer remains approximately in front of the panel.
- The installation changes illumination between an upper and lower light.
- Viewing-angle or lenticular effects are out of scope.
- The simulator and eventual machine-path generator must consume the same
  explicit surface geometry.
- Production G-code waits until a small physical coupon agrees with the
  simulation closely enough to be useful.

## Documents

- [Source brief](docs/source-brief.md)
- [Product decisions](docs/product-decisions.md)


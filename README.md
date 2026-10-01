# Raking Light

Raking Light is an open-source experiment in making relief panels that reveal
different images when illuminated from above or below.

The eventual intended workflow is:

```text
two source images
-> one physical surface description
-> lighting simulation
-> verified machine instructions
```

The project is currently testing optical feasibility. Its first software slice
only constructs one candidate relief and renders two still images of that same
surface under upper and lower illumination. It does not generate video or
G-code.

## MVP boundary

- The viewer remains approximately in front of the panel.
- The installation uses specified upper and lower light fixtures in fixed,
  repeatable positions.
- The installation changes illumination between those two fixtures.
- Viewing-angle or lenticular effects are out of scope.
- The first inputs are two simple black-and-white symbols or silhouettes.
- The first outputs are two still renders, one for each lighting state.
- Image information is encoded only in surface geometry. The renderer uses one
  uniform matte material and does not apply either source image as a texture.
- Video and machine-path generation are explicitly deferred.
- Production G-code waits until a small physical coupon agrees with the
  simulation closely enough to be useful.

The feasibility spike is disposable research code. Its implementation does not
constrain the eventual product architecture.

## Documents

- [Source brief](docs/source-brief.md)
- [Product decisions](docs/product-decisions.md)

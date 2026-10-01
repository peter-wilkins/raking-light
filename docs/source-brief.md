# Source Brief

## Status

This is a distilled version of a Gemini-generated proposal. It is input to the
design process, not an approved implementation specification.

## Product idea

Take two images and encode them into opposing faces of a repeated relief. A
light from above should reveal one image; a light from below should reveal the
other. Generate a credible preview before manufacturing, then eventually
generate LinuxCNC-compatible machine instructions.

## Desired outputs

1. A simulation showing the upper and lower lighting states and a transition
   between them.
2. A machine-readable surface or toolpath after the optical model has been
   validated physically.
3. Checks and estimates that make manufacturing failures less likely.

## Unverified implementation suggestions

The source proposal suggested Python, NumPy, OpenCV, trimesh/Open3D, a headless
renderer, FFmpeg, horizontal V-grooves, micro-offset dual passes, fixed tool
angles, and LinuxCNC-specific feeds and path blending.

None of those choices is accepted yet. In particular, tool geometry, groove
orientation, surface encoding, lighting model, material response, feeds,
speeds, path blending, and the claim that opposing slopes can independently
reproduce continuous-tone images all require proof.

## Main unknown

Can a manufacturable shallow relief produce two sufficiently distinct and
recognisable lighting responses under controlled illumination?


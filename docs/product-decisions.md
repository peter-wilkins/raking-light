# Product Decisions

## D-001: Illumination reveals the images

- **Date:** 2026-10-01
- **Status:** Accepted for MVP
- **Decision:** Keep the observer approximately in front of the panel and
  reveal the two images by switching illumination between above and below.
- **Reason:** The installation can control lighting but cannot control where a
  viewer stands. Mixing illumination and viewing-angle effects would make the
  geometry and validation ambiguous.
- **Consequence:** Viewing-angle and lenticular behaviour are out of scope. The
  first simulator and physical test need only model two controlled lighting
  states from a frontal camera position.

## D-002: Lighting is part of the optical system

- **Date:** 2026-10-01
- **Status:** Accepted for MVP
- **Decision:** Specify upper and lower light fixtures in fixed positions as
  part of the installation.
- **Reason:** Light angle, beam spread, source size, and distance affect the
  visible result. Unspecified ambient or customer-positioned lighting would
  make simulation and physical validation incomparable.
- **Consequence:** A panel design must refer to a lighting configuration. The
  prototype may use adjustable fixtures while finding good values, but a
  validated design records and reproduces those values.

## D-003: Start with binary source images

- **Date:** 2026-10-01
- **Status:** Accepted for first proof
- **Decision:** Use two simple black-and-white symbols or silhouettes.
- **Reason:** This tests whether the two lighting states can reveal distinct
  information without mixing optical feasibility with continuous-tone mapping.
- **Consequence:** Grayscale, photographs, dithering, and tone calibration are
  later experiments, not first-slice requirements.

## D-004: First software slice produces two still renders only

- **Date:** 2026-10-01
- **Status:** Accepted for first proof
- **Decision:** Construct one candidate relief surface and render it once under
  the upper light and once under the lower light.
- **Reason:** The first risk is whether the optical idea is plausible. Video and
  LinuxCNC output cannot answer that question and would delay feedback.
- **Consequence:** No animation, MP4, G-code, machine-time estimate, or
  LinuxCNC-specific settings belong in the first implementation.

## D-005: Geometry alone carries the images

- **Date:** 2026-10-01
- **Status:** Accepted for first proof
- **Decision:** Use one uniform matte material, one fixed frontal camera, and
  one shared relief surface. Only the light position changes between renders.
- **Reason:** Textures, pigmentation, and image-shaped projected lights could
  reproduce the inputs without proving the relief principle.
- **Consequence:** Source images may influence mesh geometry only. They must not
  be passed to material, texture, compositing, or lighting stages.

## D-006: Treat optical validation as a disposable spike

- **Date:** 2026-10-01
- **Status:** Accepted
- **Decision:** Build the smallest credible experiment needed to assess the
  optical idea, without treating its dependencies or code structure as the
  eventual application architecture.
- **Reason:** There is no value in designing production software before showing
  that one manufacturable surface can produce two distinct lighting responses.
- **Consequence:** Prefer an established renderer and throwaway script. Capture
  the experiment and verdict, then separately design product software only if
  the result warrants it.

## D-007: Park the dual-image concept

- **Date:** 2026-10-01
- **Status:** Parked
- **Decision:** Stop active work on encoding two source images into one relief.
- **Reason:** The research examples solve a recognisable but different problem:
  they encode images using dense surface detail. The intended product is still
  artistically amorphous and should be led by sculptural form, light, and the
  capabilities of the routing table. Minimising cutting time is an advantage,
  not a secondary optimisation.
- **Consequence:** Keep D-001 through D-006 as historical constraints for a
  possible later experiment. Do not build the proposed two-image renderer,
  video pipeline, or G-code generator now.

## D-008: Use Blender as a digital wall-panel studio

- **Date:** 2026-10-01
- **Status:** Accepted for discovery
- **Decision:** Recreate the geometric and manufacturing principles of selected
  wall-panel products in Blender, then vary those principles into original
  designs.
- **Reason:** Existing products provide concrete visual targets and known market
  context. Blender allows cheap iteration over geometry, materials, scale, and
  lighting before consuming stock or routing time.
- **Consequence:** Early studies should pair rendered appearance with simple
  manufacturing metadata: likely cutter, number of passes, tool changes, and
  relative cutting effort. Exact proprietary decorative patterns are reference
  material, not production assets.

## D-009: Constrain the first study to one simple cutting operation

- **Date:** 2026-10-01
- **Status:** Accepted for first study
- **Decision:** Design the first faceted pleat field for one V-bit, straight
  continuous cuts, and no tool changes.
- **Reason:** This makes routing efficiency intrinsic to the design experiment.
  A visually successful result under this constraint has a credible path to
  fast manufacture.
- **Consequence:** Curved toolpaths, pockets, raster finishing, and secondary
  cutters are out of scope for the first study. Blender parameters should map
  visibly to conceptual cut lines and cut depth.

## D-010: Design the wall; manufacture it as panels

- **Date:** 2026-10-01
- **Status:** Accepted
- **Decision:** Treat the artwork as one composition in wall coordinates. Split
  it into sheet-sized panels only for manufacture, transport, and installation.
- **Reason:** The product distinction is a designed whole wall rather than a
  repeating decorative panel. Botanical forms, line art, and landscapes can
  develop across the complete space.
- **Consequence:** Panel seams and registration belong to a later manufacturing
  stage. The design model must not reset or repeat at sheet boundaries.

## D-011: Start with painted MDF

- **Date:** 2026-10-01
- **Status:** Accepted for first study
- **Decision:** Model the first design as a painted 18 mm MDF wall.
- **Reason:** MDF is inexpensive and consistent. A uniform painted finish lets
  us judge whether geometry and raking light carry the design before adding
  wood grain or exposed laminate layers.
- **Consequence:** Use a uniform matte material in the first Blender study.
  Plywood, bamboo, laminates, and contrasting cores remain later material
  experiments.

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

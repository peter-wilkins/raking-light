"""Disposable Blender study for a wall-sized, V-bit-routed botanical mural."""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector


WALL_WIDTH_M = 4.8
WALL_HEIGHT_M = 2.4
MDF_THICKNESS_M = 0.018
V_BIT_ANGLE_DEG = 90.0
ASSUMED_FEED_MM_MIN = 3000.0
GRID_X = 1001
GRID_Z = 501


@dataclass
class CutPath:
    name: str
    points: np.ndarray
    depth_m: float
    kind: str

    @property
    def length_m(self) -> float:
        return float(np.linalg.norm(np.diff(self.points, axis=0), axis=1).sum())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("artifacts/botanical-vbit-study"),
    )
    blender_args = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    return parser.parse_args(blender_args)


def cubic_bezier(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    samples: int = 40,
) -> np.ndarray:
    t = np.linspace(0.0, 1.0, samples, dtype=np.float32)[:, None]
    p0a, p1a, p2a, p3a = (np.asarray(p, dtype=np.float32) for p in (p0, p1, p2, p3))
    return (
        ((1.0 - t) ** 3) * p0a
        + 3.0 * ((1.0 - t) ** 2) * t * p1a
        + 3.0 * (1.0 - t) * (t**2) * p2a
        + (t**3) * p3a
    )


def leaf_outline(
    center: tuple[float, float],
    angle_deg: float,
    length_m: float,
    width_m: float,
    samples_per_side: int = 18,
) -> np.ndarray:
    angle = math.radians(angle_deg)
    direction = np.array([math.cos(angle), math.sin(angle)], dtype=np.float32)
    normal = np.array([-direction[1], direction[0]], dtype=np.float32)
    base = np.asarray(center, dtype=np.float32) - direction * length_m * 0.28
    t = np.linspace(0.0, 1.0, samples_per_side, dtype=np.float32)
    spine = base[None, :] + t[:, None] * direction[None, :] * length_m
    bulge = np.clip(np.sin(np.pi * t), 0.0, None) ** 0.78
    first = spine + bulge[:, None] * normal[None, :] * width_m * 0.5
    second = spine[::-1] - bulge[::-1, None] * normal[None, :] * width_m * 0.5
    return np.vstack([first, second, first[:1]])


def flower_outline(
    center: tuple[float, float],
    radius_m: float,
    petals: int,
    rotation_deg: float,
    samples: int = 96,
) -> np.ndarray:
    theta = np.linspace(0.0, 2.0 * np.pi, samples, endpoint=True, dtype=np.float32)
    rotation = math.radians(rotation_deg)
    radius = radius_m * (0.70 + 0.30 * np.cos(petals * theta))
    x = center[0] + radius * np.cos(theta + rotation)
    z = center[1] + radius * np.sin(theta + rotation)
    return np.column_stack([x, z]).astype(np.float32)


def build_composition() -> list[CutPath]:
    paths: list[CutPath] = []

    stems = [
        (
            "main-stem",
            cubic_bezier((-2.25, 0.02), (-1.55, 0.45), (0.35, 1.38), (1.95, 2.30), 64),
            0.009,
        ),
        (
            "lower-branch",
            cubic_bezier((-1.35, 0.48), (-0.35, 0.55), (0.62, 0.85), (1.75, 1.38), 52),
            0.0075,
        ),
        (
            "upper-branch",
            cubic_bezier((-0.45, 1.02), (-0.92, 1.47), (-1.42, 1.75), (-2.08, 2.08), 44),
            0.0075,
        ),
        (
            "rising-stem",
            cubic_bezier((0.32, 0.03), (0.45, 0.62), (0.72, 1.20), (1.22, 1.88), 48),
            0.008,
        ),
    ]
    for name, points, depth in stems:
        paths.append(CutPath(name, points, depth, "stem"))

    leaves = [
        ((-1.82, 0.33), 156, 0.48, 0.20),
        ((-1.48, 0.55), 26, 0.54, 0.22),
        ((-1.06, 0.76), 154, 0.58, 0.24),
        ((-0.62, 0.98), 24, 0.63, 0.25),
        ((-0.08, 1.24), 154, 0.58, 0.23),
        ((0.46, 1.51), 28, 0.62, 0.25),
        ((0.98, 1.80), 158, 0.55, 0.22),
        ((-0.76, 0.60), 112, 0.45, 0.18),
        ((-0.22, 0.69), 52, 0.46, 0.19),
        ((0.34, 0.83), 128, 0.48, 0.20),
        ((0.86, 1.02), 46, 0.44, 0.18),
        ((-0.74, 1.36), 206, 0.46, 0.19),
        ((-1.18, 1.67), 32, 0.43, 0.18),
        ((0.47, 0.53), 168, 0.48, 0.20),
        ((0.69, 1.00), 8, 0.52, 0.21),
        ((0.92, 1.42), 176, 0.46, 0.18),
    ]
    for index, (center, angle, length, width) in enumerate(leaves, start=1):
        paths.append(
            CutPath(
                f"leaf-{index:02d}",
                leaf_outline(center, angle, length, width),
                0.006,
                "leaf",
            )
        )

    flowers = [
        ((1.93, 2.24), 0.25, 5, 12),
        ((1.77, 1.38), 0.20, 6, 0),
        ((-2.04, 2.07), 0.18, 5, 18),
        ((1.21, 1.88), 0.16, 6, 8),
    ]
    for index, (center, radius, petals, rotation) in enumerate(flowers, start=1):
        paths.append(
            CutPath(
                f"flower-{index:02d}",
                flower_outline(center, radius, petals, rotation),
                0.0065,
                "flower",
            )
        )

    return paths


def rasterize_v_grooves(paths: list[CutPath]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xs = np.linspace(-WALL_WIDTH_M / 2.0, WALL_WIDTH_M / 2.0, GRID_X, dtype=np.float32)
    zs = np.linspace(0.0, WALL_HEIGHT_M, GRID_Z, dtype=np.float32)
    depth_map = np.zeros((GRID_Z, GRID_X), dtype=np.float32)
    dx = float(xs[1] - xs[0])
    dz = float(zs[1] - zs[0])
    slope = math.tan(math.radians(V_BIT_ANGLE_DEG / 2.0))

    for path in paths:
        influence = path.depth_m * slope
        for start, end in zip(path.points[:-1], path.points[1:]):
            segment = end - start
            segment_length_sq = float(np.dot(segment, segment))
            if segment_length_sq == 0.0:
                continue

            x0 = max(0, int(math.floor((min(start[0], end[0]) - influence - xs[0]) / dx)))
            x1 = min(GRID_X, int(math.ceil((max(start[0], end[0]) + influence - xs[0]) / dx)) + 1)
            z0 = max(0, int(math.floor((min(start[1], end[1]) - influence - zs[0]) / dz)))
            z1 = min(GRID_Z, int(math.ceil((max(start[1], end[1]) + influence - zs[0]) / dz)) + 1)
            if x0 >= x1 or z0 >= z1:
                continue

            local_x, local_z = np.meshgrid(xs[x0:x1], zs[z0:z1])
            rel_x = local_x - start[0]
            rel_z = local_z - start[1]
            projection = np.clip(
                (rel_x * segment[0] + rel_z * segment[1]) / segment_length_sq,
                0.0,
                1.0,
            )
            closest_x = start[0] + projection * segment[0]
            closest_z = start[1] + projection * segment[1]
            distance = np.sqrt((local_x - closest_x) ** 2 + (local_z - closest_z) ** 2)
            groove = np.clip(path.depth_m - distance / slope, 0.0, path.depth_m)
            local = depth_map[z0:z1, x0:x1]
            np.maximum(local, groove, out=local)

    return xs, zs, depth_map


def reset_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for data_collection in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for block in list(data_collection):
            if block.users == 0:
                data_collection.remove(block)


def material(name: str, colour: tuple[float, float, float, float], roughness: float) -> bpy.types.Material:
    result = bpy.data.materials.new(name)
    result.diffuse_color = colour
    result.use_nodes = True
    principled = result.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = colour
    principled.inputs["Roughness"].default_value = roughness
    return result


def create_relief_mesh(xs: np.ndarray, zs: np.ndarray, depth_map: np.ndarray) -> bpy.types.Object:
    xx, zz = np.meshgrid(xs, zs)
    vertices = np.column_stack([xx.ravel(), depth_map.ravel(), zz.ravel()]).tolist()
    faces = []
    for row in range(GRID_Z - 1):
        offset = row * GRID_X
        next_offset = (row + 1) * GRID_X
        faces.extend(
            (offset + col, offset + col + 1, next_offset + col + 1, next_offset + col)
            for col in range(GRID_X - 1)
        )

    mesh = bpy.data.meshes.new("Botanical V-groove surface")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    relief = bpy.data.objects.new("Botanical V-groove surface", mesh)
    bpy.context.collection.objects.link(relief)
    relief.data.materials.append(material("Warm matte paint", (0.72, 0.66, 0.54, 1.0), 0.82))
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return relief


def create_backing() -> None:
    bpy.ops.mesh.primitive_cube_add(
        location=(0.0, MDF_THICKNESS_M / 2.0 + 0.0105, WALL_HEIGHT_M / 2.0),
        scale=(WALL_WIDTH_M / 2.0, MDF_THICKNESS_M / 2.0, WALL_HEIGHT_M / 2.0),
    )
    backing = bpy.context.object
    backing.name = "MDF backing"
    backing.data.materials.append(bpy.data.materials["Warm matte paint"])

    bpy.ops.mesh.primitive_plane_add(size=20.0, location=(0.0, 0.12, WALL_HEIGHT_M / 2.0))
    surround = bpy.context.object
    surround.name = "Gallery wall"
    surround.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    surround.data.materials.append(material("Gallery wall paint", (0.12, 0.13, 0.14, 1.0), 0.9))


def point_at(obj: bpy.types.Object, target: tuple[float, float, float]) -> None:
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def create_camera() -> bpy.types.Object:
    camera_data = bpy.data.cameras.new("Studio camera")
    camera = bpy.data.objects.new("Studio camera", camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = (0.0, -6.35, 1.28)
    camera_data.lens = 52.0
    point_at(camera, (0.0, 0.0, 1.20))
    bpy.context.scene.camera = camera
    return camera


def create_area_light(name: str) -> bpy.types.Object:
    light_data = bpy.data.lights.new(name, type="AREA")
    light_data.energy = 1100.0
    light_data.shape = "RECTANGLE"
    light_data.size = 2.0
    light_data.size_y = 0.75
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    return light


def configure_render(output_dir: Path) -> None:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.filepath = str(output_dir / "placeholder.png")
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.world.color = (0.015, 0.018, 0.022)


def render_studies(output_dir: Path, light: bpy.types.Object) -> None:
    states = [
        ("neutral", (0.0, -3.8, 3.2), 1250.0, 3.8, 2.5),
        ("top-raking", (0.0, -0.65, 3.55), 1450.0, 2.8, 0.55),
        ("left-raking", (-3.3, -0.72, 1.55), 1300.0, 1.8, 0.65),
    ]
    for name, location, energy, size, size_y in states:
        light.location = location
        light.data.energy = energy
        light.data.size = size
        light.data.size_y = size_y
        point_at(light, (0.0, 0.0, 1.2))
        bpy.context.scene.render.filepath = str(output_dir / f"botanical-{name}.png")
        bpy.ops.render.render(write_still=True)


def write_metadata(output_dir: Path, paths: list[CutPath], depth_map: np.ndarray) -> None:
    total_length_m = sum(path.length_m for path in paths)
    cutting_minutes = total_length_m * 1000.0 / ASSUMED_FEED_MM_MIN
    handling_minutes = len(paths) * 3.0 / 60.0
    payload = {
        "study": "botanical-vbit-study-001",
        "status": "visual hypothesis; not CAM",
        "wall": {
            "width_m": WALL_WIDTH_M,
            "height_m": WALL_HEIGHT_M,
            "material": "painted MDF",
            "thickness_mm": MDF_THICKNESS_M * 1000.0,
        },
        "cutting_assumptions": {
            "tool": f"{V_BIT_ANGLE_DEG:g}-degree V-bit",
            "tool_changes": 0,
            "conceptual_paths": len(paths),
            "total_path_length_m": round(total_length_m, 2),
            "maximum_depth_mm": round(float(depth_map.max()) * 1000.0, 2),
            "feed_mm_min": ASSUMED_FEED_MM_MIN,
            "rough_time_minutes": round(cutting_minutes + handling_minutes, 1),
            "warning": "Excludes rapids, acceleration limits, setup, seam strategy, and finishing.",
        },
        "paths": [
            {
                "name": path.name,
                "kind": path.kind,
                "length_m": round(path.length_m, 3),
                "depth_mm": round(path.depth_m * 1000.0, 2),
            }
            for path in paths
        ],
        "mesh": {"samples_x": GRID_X, "samples_z": GRID_Z},
    }
    (output_dir / "study.json").write_text(json.dumps(payload, indent=2) + "\n")


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = build_composition()
    xs, zs, depth_map = rasterize_v_grooves(paths)
    reset_scene()
    create_relief_mesh(xs, zs, depth_map)
    create_backing()
    create_camera()
    light = create_area_light("Study light")
    configure_render(output_dir)
    render_studies(output_dir, light)
    write_metadata(output_dir, paths, depth_map)
    bpy.ops.wm.save_as_mainfile(filepath=str(output_dir / "botanical-vbit-study.blend"))


if __name__ == "__main__":
    main()

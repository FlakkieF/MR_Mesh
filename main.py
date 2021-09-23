
import trimesh
import pyrender


def main():

    tm = trimesh.load("psb_v1/benchmark/db/1/m110/m110.off")

    display_mesh = pyrender.Mesh.from_trimesh(tm, smooth=False)

    wireframe_mesh = pyrender.Mesh.from_trimesh(tm, wireframe=True)

    scene = pyrender.Scene()

    scene.add(display_mesh)
    scene.add(wireframe_mesh)

    pyrender.Viewer(scene, use_raymond_lighting=True)


if __name__ == '__main__':
    main()


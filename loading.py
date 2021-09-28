from trimesh import load


def load_mesh_from_number(str_n):

    stem = ""

    if len(str_n) == 3:
        stem = str_n[0]
        pass

    elif len(str_n) == 4:
        stem = str_n[0:1]

    path = "psb_v1/benchmark/db/{stem}/m{full}/m{full}.off".format(stem=stem, full=str_n)

    return load(path)
# end

from trimesh import load
import numpy as np
import pandas as pd


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


def load_class_labels(cla_file, debug=False):

    labeled_models = []

    with open(cla_file, "r") as file:

        print(file.readline().strip())

        args = [int(x) for x in file.readline().split()]

        if debug:
            print("{} classes and {} models".format(args[0], args[1]))
            print("-"*50)

        for _ in range(args[0]):

            # occasional double blank line, wait for non blank
            line = file.readline().split()
            while not line:
                line = file.readline().split()

            model_class = line[0]
            parent_class = line[1]
            n = int(line[2])

            if debug:
                print("{} modles with {} class and {} parent class".format(n, model_class, parent_class))

            for _ in range(int(n)):
                model = file.readline().strip()
                labeled_models.append([model, model_class, parent_class])

    labeled_models = np.array(labeled_models)

    return labeled_models


if __name__ == "__main__":
    stuff = load_class_labels("psb_v1/benchmark/classification/v1/base/train.cla")
    # load_class_labels("psb_v1/benchmark/classification/v1/base/test.cla")

    df = pd.DataFrame(stuff, columns=["model", "class", "parent_class"])

    print(df.head())
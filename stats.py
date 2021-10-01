import loading
import numpy as np
import pandas as pd
import trimesh
import matplotlib.pyplot as plt

def get_num_faces(model):
    return len(model.faces)


def get_num_vertices(model):
    return len(model.faces)


def get_database_stats(models):

    v_num_faces = np.vectorize(get_num_faces)

    v_num_vertices = np.vectorize(get_num_vertices)

    details = np.transpose(np.array([v_num_faces(models), v_num_vertices(models)]))

    return details


if __name__ == "__main__":

    class_file = "reduced_coarse1Train.cla"

    #model = loading.load_mesh_from_number("1488")
    #print(model.bounds)

    labels, models = loading.load_labeled_models(class_file)

    mesh_details = get_database_stats(models)

    plt.hist(mesh_details[:, 1], bins=100)
    plt.show()

    print(mesh_details[1, :])

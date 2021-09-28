from trimesh import load, Trimesh
import numpy as np
import pandas as pd
from time import time




def load_mesh_from_number(str_n):
    """"
        Loads and returns a Trimesh model based on the model number.
        Assumes data set is in the same directory as the script.
    """

    stem = ""


    # 3 digits
    if len(str_n) == 3:
        stem = str_n[0]
    # 4 digits
    elif len(str_n) == 4:
        stem = str_n[0:2]
    # else it should be zero, none with 5 or more digits
    else:
        stem = "0"

    path = "psb_v1/benchmark/db/{stem}/m{full}/m{full}.off".format(stem=stem, full=str_n)

    return load(path)
# end def


def load_class_labels(cla_file, debug=False):
    """
    Parses the class label file and finds labels for the models

    :param cla_file: the file containing the model class labels
    :param debug: print debug text
    :return: numpy array of the model numbers and their associated classes
    """


    labeled_models = []

    with open(cla_file, "r") as file:

        print(file.readline().strip())

        num_classes, num_models = [int(x) for x in file.readline().split()]

        if debug:
            print("{} classes and {} models".format(num_classes, num_models))
            print("-"*50)

        for _ in range(num_classes):

            # wait for non blank line
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

    # convert to numpy array
    labeled_models = np.array(labeled_models)

    return labeled_models
# end def

def load_labeled_models(cla_file):
    """
    Loads the Triemsh models and their labels

    :param cla_file: the file containing the model class labels
    :return: numpy array of class labels and array of Trimesh model meshes
    """

    elapsed = time()

    # get the class labels
    class_labels = load_class_labels(cla_file)

    # create vectorized version of load_mesh_from_number
    vectorized_load_mesh = np.vectorize(load_mesh_from_number)

    # load models with numbers from
    trimesh_models = vectorized_load_mesh(class_labels[:, 0])

    elapsed = time() - elapsed

    print("Imported {} out of {} models in {:.2f} seconds.".format(len(trimesh_models), len(class_labels), elapsed))

    return class_labels, trimesh_models
# end def

if __name__ == "__main__":

    # load_class_labels("psb_v1/benchmark/classification/v1/base/test.cla")
    # stuff = load_class_labels("psb_v1/benchmark/classification/v1/base/train.cla")


    #print(stuff[:,0])
    # df = pd.DataFrame(stuff, columns=["model", "class", "parent_class"])

    labels, models = load_labeled_models("psb_v1/benchmark/classification/v1/base/train.cla")



import csv
import math
import os

import numpy as np


def csv_2np(directory, n_steps=60, n_predictions=10):
    file_list = os.listdir(directory)
    file_list.sort()
    data = []
    for csv_file in file_list:
        filename = os.path.join(directory, csv_file)
        with open(filename, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            for n, row in enumerate(csv_reader):
                if n == 0 or n == 1:
                    pass
                else:
                    price = float(row[-2])
                    volume = float(row[-1])
                    data.append([price, volume])
    return np.array(data)


def dataset(data, series=[], n_steps=60, n_predictions=10):

    N = math.floor(len(data) / n_steps)

    for n in range(N):
        series.append(data[n * n_steps : ((n + 1) * n_steps) + n_predictions, :])

    series = np.array(series)
    np.random.shuffle(series)
    Y = np.empty((N, n_steps, n_predictions))
    X = series[:, :n_steps, :]

    for step_ahead in range(1, n_predictions + 1):
        Y[..., step_ahead - 1] = series[..., step_ahead : step_ahead + n_steps, 0]
    return series, X, Y


if __name__ == "__main__":
    directory = "./Minute_BTC"
    n_steps = 60
    n_predictions = 10
    data = csv_2np(directory, n_steps, n_predictions)
    _, X, Y = dataset(data, n_steps=n_steps, n_predictions=n_predictions)
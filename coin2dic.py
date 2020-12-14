import csv
import os


def coin2dic(filename):
    with open(filename, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        coin_name = os.path.basename(filename)
        coin_name = os.path.splitext(coin_name)[0]
        coin = {"Name": coin_name}
        for row in csv_reader:
            name = row[0]
            row.pop(0)
            row.reverse()
            coin[name] = [float(value) for value in row]
        return coin

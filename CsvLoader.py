import csv


def load_csv(path):
    with open(path) as csvfile:
        loader = csv.reader(csvfile, delimiter=';')
        loader = list(loader)
    loader.pop(0)
    loader.pop()
    return loader

import csv
import numpy as np

def get_csv():
    with open('./words.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = [d[0] for d in data]
    return data[1:]

def get_txt():
    with open("./words.txt", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = [d[0] for d in data]
    return data

def shuffle(words):
    words_copy = np.array(words)
    np.random.shuffle(words_copy)
    return words_copy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_data(file_name, title, x_label, y_label):
    data = pd.read_csv(file_name)
    x = data["x"]
    y = data["y"]

    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

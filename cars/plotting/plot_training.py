# ------------------------------------------------------- #
# Author: William Svea-Lochert
# Date written: 16.02.2020
# Plot training & validation accuracy & loss values
# ------------------------------------------------------- #
import matplotlib.pyplot as plt


# Plot the given model via history object from training
def plot_model(history, metric, name, save_location):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_' + metric])
    plt.title(name + ' ' + metric)
    plt.ylabel(metric)
    plt.xlabel('Epoch')
    plt.legend(['Train', 'val'], loc='upper left')
    plt.savefig(save_location)
    plt.show()



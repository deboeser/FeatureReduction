import matplotlib.pyplot as plt
import numpy as np


def plot_faces(images, h, w, scaling=1.0, n_row=2, n_col=8, suptitle=""):
    """ Plots images into a grid
    
    Parameters:
        images: Images to be printed
        h (int): Height of one image in px
        w (int): Width of one image in px
        scaling: Value between 0.0 and 1.0, scales the images
        n_row (int): Number of rows
        n_col (int): Number of columns
        suptitle (str): Title for the plot
    
    """
    plt.figure(figsize=(1.8 * n_col * scaling, 2.4 * n_row * scaling))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=(0.85 if len(suptitle) > 0 else 0.9), hspace=.20)
    if len(suptitle) > 0:
        plt.suptitle(suptitle, fontsize=18)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.xticks(())
        plt.yticks(())


def plot_faces_compare(images1, images2, h, w, scaling=1.0, n=8, suptitle=""):
    """Plots images to compare them, first row images1, second row images2
    
    Parameters:
        images1: Images for the first row
        images2: Images for the second row
        h (int): Height of one image in px
        w (int): Witdht of one image in px
        scaling: Value between 0.0 and 1.0, scales the images
        n (int): Iumber of image pairs
        suptitle (str): Title for the plot

    """
    plt.figure(figsize=(1.8 * n * scaling, 2.4 * 2 * scaling))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=(0.85 if len(suptitle) > 0 else 0.9), hspace=.20)
    if len(suptitle) > 0:
        plt.suptitle(suptitle, fontsize=18)
    for i in range(n):
        plt.subplot(2, n, i + 1)
        plt.imshow(images1[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.xticks(())
        plt.yticks(())
        plt.subplot(2, n, i + 1 + n)
        plt.imshow(images2[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.xticks(())
        plt.yticks(())

        
def plot_variance_retention(eig_retention, var_retain):
    """Plots variance retention curve
    
    Parameters:
        eig_retention: Arrays normalized eigenvalues (sum(eig_retention)==1)
        var_retain (double): Variance retention level to mark
    
    """
    U_n = np.where(eig_retention >= var_retain)[0][0] - 1
    plt.figure(figsize=(12, 4))
    plt.title("Variance Retention over number of Eigenvectors")
    plt.plot(np.arange(0, len(eig_retention), 1), eig_retention)
    plt.scatter(x=[U_n], y=[eig_retention[U_n]])
    
    y_tick_range = np.arange(0, 1.1, 0.05)
    plt.yticks(y_tick_range, ["{:.0f}%".format(x*100) for x in y_tick_range])
    plt.ylabel("Variance Retained")
    plt.xlabel("Number of Eigenvectors")
    plt.ylim(0.8, 1.01)
    plt.grid()
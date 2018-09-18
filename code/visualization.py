import pandas as pd
import matplotlib as mpls
import matplotlib.pyplot as plt
import seaborn as sns
import os



def plot_sensitivity( img, sens_grads, backprop_grads, category, name):
    fig = plt.figure(figsize=(20, 6))
    fig.suptitle("Predicted category: " + category)
    ax = plt.subplot(131)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(img)
    plt.title("Image")
    ax = plt.subplot(132)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(sens_grads,cmap=plt.get_cmap('bwr'), vmin = -1.0, vmax = 1.0)

    plt.title("Sensitivity")
    ax = plt.subplot(133)
    plt.imshow(backprop_grads,cmap=plt.get_cmap('bwr'), vmin = -1.0, vmax = 1.0)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.title("Guided Backprop")
  
    plt.show()
def plot_cam( img, sens_grads, category, name):
    fig = plt.figure(figsize=(12, 6))
    fig.suptitle("Predicted category: " + category)
    ax = plt.subplot(121)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(img)
    plt.title("Image")
    ax = plt.subplot(122)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(sens_grads,cmap=plt.get_cmap('jet'), vmin = -1.0, vmax = 1.0)

    plt.title("GradCAM")

   
    plt.show()
def plot_lime( img, sens_grads, category, name):
    fig = plt.figure(figsize=(12, 6))
    fig.suptitle("Predicted category: " + category)
    ax = plt.subplot(121)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(img)
    plt.title("Image")
    ax = plt.subplot(122)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.imshow(sens_grads)

    plt.title("LIME")

    plt.show()

import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 10), clear=True)

    size = 255  # size of array
    horizontal_gradient1 = np.zeros([size, size])  # zero filling array
    w = horizontal_gradient1.shape[1]  # width
    h = horizontal_gradient1.shape[0]  # height
    for i in range(h):  # changing values of array
        for j in range(w):
            horizontal_gradient1[i][j] = j
    cv2.imwrite('../Data/Intro to Numpy/resualt1.jpg', horizontal_gradient1)  # saving

    ax1 = fig.add_subplot(2, 2, 1) # output
    ax1.imshow(horizontal_gradient1)
    ax1.set(title='horizontal gradient 1')
    ax1.set_yticks([])
    ax1.set_xticks([])

    horizontal_gradient2 = np.zeros([size, size])  # zero filling array
    w = horizontal_gradient2.shape[1]  # width
    h = horizontal_gradient2.shape[0]  # height
    for i in range(h):  # changing values of array
        for j in range(w):
            horizontal_gradient2[i][j] = w - j - 1
    cv2.imwrite('../Data/Intro to Numpy/resualt2.jpg', horizontal_gradient2)  # saving

    ax2 = fig.add_subplot(2, 2, 2)  # output
    ax2.imshow(horizontal_gradient2)
    ax2.set(title='horizontal gradient 2')
    ax2.set_yticks([])
    ax2.set_xticks([])

    vertical_gradient1 = np.zeros([size, size])  # zero filling array
    w = vertical_gradient1.shape[1]  # width
    h = vertical_gradient1.shape[0]  # height
    for i in range(h):  # changing values of array
        for j in range(w):
            vertical_gradient1[i][j] = i
    cv2.imwrite('../Data/Intro to Numpy/resualt3.jpg', vertical_gradient1)  # saving

    ax3 = fig.add_subplot(2, 2, 3) # output
    ax3.imshow(vertical_gradient1)
    ax3.set(title='vertical gradient 1')
    ax3.set_yticks([])
    ax3.set_xticks([])

    vertical_gradient2 = np.zeros([size, size])  # zero filling array
    w = vertical_gradient2.shape[1]  # width
    h = vertical_gradient2.shape[0]  # height
    for i in range(h):  # changing values of array
        for j in range(w):
            vertical_gradient2[i][j] = h - i - 1
    cv2.imwrite('../Data/Intro to Numpy/resualt4.jpg', vertical_gradient2)  # saving

    ax4 = fig.add_subplot(2, 2, 4) # output
    ax4.imshow(vertical_gradient2)
    ax4.set(title='vertical gradient 2')
    ax4.set_yticks([])
    ax4.set_xticks([])
    plt.show()

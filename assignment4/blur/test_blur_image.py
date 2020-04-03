#!/usr/bin/env python3

from .blur_image import blur_image
import os
import numpy as np
import cv2


def test_blur_decrease():
    np.random.seed(0)  # Fix the random seed
    img = np.random.rand(100, 100, 3) * 255

    cv2.imwrite("test.jpg", img)
    dst = blur_image("test.jpg")
    os.remove("test.jpg")
    assert np.amax(dst) < np.amax(img)


def test_blur_average():
    np.random.seed(0)  # Fix the random seed
    img = np.random.rand(100, 100, 3) * 255

    cv2.imwrite("test.jpg", img)
    dst = blur_image("test.jpg")
    os.remove("test.jpg")

    i = np.random.randint(0, img.shape[0])
    j = np.random.randint(0, img.shape[1])
    k = np.random.randint(0, img.shape[2])

    img = np.pad(img, ((1, 1), (1, 1), (0, 0)), mode='edge')
    average = img[i, j, k] / 9 + img[i-1, j, k] / 9 + img[i+1, j, k] / 9 \
        + img[i, j-1, k] / 9 + img[i, j+1, k] / 9 \
        + img[i-1, j-1, k] / 9 + img[i+1, j+1, k] / 9 \
        + img[i-1, j+1, k] / 9 + img[i+1, j-1, k] / 9

    assert abs(average - dst[i, j, k]) < 1e-14

#!/usr/bin/env python3

import numpy as np
import cv2


def blur(filename):
    src = cv2.imread(filename)

    src = src.astype("uint32")  # Prevent overloading when using uint8
    src = np.pad(src, ((1, 1), (1, 1), (0, 0)), mode='edge')

    # Calculate average of pixels nearby, creates blur effect
    dst = (src[1:-1, 1:-1, :] + src[:-2, 1:-1, :] + src[2:, 1:-1, :]
           + src[1:-1, :-2, :] + src[1:-1, 2:, :] + src[:-2, :-2, :]
           + src[2:, 2:, :] + src[:-2, 2:, :] + src[2:, :-2, :])/9

    dst = dst.astype("uint8")  # Round to nearest integer
    cv2.imwrite(f"blurred_{filename.split('.')[0]}_2.jpg", dst)


if __name__ == "__main__":
    blur("beatles.jpg")

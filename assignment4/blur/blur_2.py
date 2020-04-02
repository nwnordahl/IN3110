#!/usr/bin/env python3

import numpy as np
import cv2


def blur_2(infile, outfile):
    src = cv2.imread(infile)

    src = src.astype("uint32")  # Prevent overloading when using uint8
    src = np.pad(src, ((1, 1), (1, 1), (0, 0)), mode='edge')

    # Calculate average of pixels nearby, creates blur effect
    dst = (src[1:-1, 1:-1, :] + src[:-2, 1:-1, :] + src[2:, 1:-1, :]
           + src[1:-1, :-2, :] + src[1:-1, 2:, :] + src[:-2, :-2, :]
           + src[2:, 2:, :] + src[:-2, 2:, :] + src[2:, :-2, :])/9

    dst = dst.astype("uint8")  # Round to nearest integer
    cv2.imwrite(outfile, dst)


if __name__ == "__main__":
    blur_2("../images/beatles.jpg", "../images/blurred_beatles_2.jpg")

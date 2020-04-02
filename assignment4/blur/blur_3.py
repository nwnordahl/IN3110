#!/usr/bin/env python3

import numpy as np
import cv2
from numba import jit


@jit
def blur_3(infile, outfile):
    src = cv2.imread(infile)
    dst = cv2.imread(infile)

    src = src.astype("uint32")  # Prevent overloading when using uint8
    src = np.pad(src, ((1, 1), (1, 1), (0, 0)), mode='edge')

    # Calculate average of pixels nearby, creates blur effect
    for h in range(1, src.shape[0] - 1):
        for w in range(1, src.shape[1] - 1):
            for c in range(src.shape[2]):
                dst[h-1, w-1, c] = (src[h, w, c]
                                    + src[h-1, w, c] + src[h+1, w, c]
                                    + src[h, w-1, c] + src[h, w+1, c]
                                    + src[h-1, w-1, c] + src[h+1, w+1, c]
                                    + src[h-1, w+1, c] + src[h+1, w-1, c])/9

    dst = dst.astype("uint8")  # Round to nearest integer
    cv2.imwrite(outfile, dst)


if __name__ == "__main__":
    blur_3("../images/beatles.jpg", "../images/blurred_beatles_3.jpg")

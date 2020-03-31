#!/usr/bin/env python3

import numpy as np
import cv2


def blur(filename):
    src = cv2.imread(filename)
    dst = cv2.imread(filename)

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
    cv2.imwrite(f"blurred_{filename.split('.')[0]}_1.jpg", dst)


if __name__ == "__main__":
    blur("beatles.jpg")

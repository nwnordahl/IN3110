#!/usr/bin/env python3

import numpy as np
import cv2


def blur(filename):
    src = cv2.imread(filename)
    dst = cv2.imread(filename)

    src = src.astype("uint32")  # Prevent overloading when using uint8
    src = np.pad(src, ((1, 1), (1, 1), (0, 0)), mode='edge')
    print(src.shape)
    for h in range(1, src.shape[0] - 2):
        for w in range(1, src.shape[1] - 2):
            for c in range(src.shape[2]):
                dst[h, w, c] = (src[h, w, c] + src[h-1, w, c] + src[h+1, w, c]
                                + src[h, w-1, c] + src[h, w+1, c]
                                + src[h-1, w-1, c] + src[h-1, w+1, c]
                                + src[h+1, w-1, c] + src[h+1, w+1, c])/9

    dst = dst.astype("uint8")
    cv2.imwrite(f"blurred_{filename.split('.')[0]}.jpg", dst)


if __name__ == "__main__":
    blur("beatles.jpg")

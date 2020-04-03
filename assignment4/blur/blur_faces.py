#!/usr/bin/env python3

import numpy as np
import cv2


def blur_faces(infile, outfile, faces):
    src = cv2.imread(infile)
    dst = cv2.imread(infile)

    src = src.astype("uint32")
    src = np.pad(src, ((1, 1), (1, 1), (0, 0)), mode='edge')

    for (y, x, w, h) in faces:
        for i in range(h):
            for j in range(w):
                dst[x+i-1, y+j-1, :] = (src[x+i, y+j, :]
                                        + src[x+i-1, y+j, :] + src[x+i+1, y+j, :]
                                        + src[x+i, y+j-1, :] + src[x+i, y+j+1, :]
                                        + src[x+i-1, y+j-1, :] + src[x+i+1, y+j+1, :]
                                        + src[x+i-1, y+j+1, :] + src[x+i+1, y+j-1, :])/9

    dst = dst.astype("uint8")
    cv2.imwrite(outfile, dst)
    return outfile


def face_detector(infile, outfile):
    image = cv2.imread(infile)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.025,
        minNeighbors=5,
        minSize=(30, 30)
    )
    print(f"Found {len(faces)} faces!")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(outfile, image)
    return outfile, faces


if __name__ == "__main__":
    infile, faces = face_detector("../images/beatles.jpg",
                                  "../images/facedetection.jpg")
    infile = blur_faces(infile, "../images/blur_faces.jpg", faces)

    infile, faces = face_detector(infile, "../images/facedetection_2.jpg")
    infile = blur_faces(infile, "../images/blur_faces_2.jpg", faces)

    infile, faces = face_detector(infile, "../images/facedetection_3.jpg")
    infile = blur_faces(infile, "../images/blur_faces_3.jpg", faces)

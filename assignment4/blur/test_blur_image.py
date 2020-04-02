#!/usr/bin/env python3

from blur_image import blur_image
import numpy as np


def test_blur():
    blur_image("../images/beatles.jpg")
    assert True

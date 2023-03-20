#!/usr/bin/env python3
import argparse
import sys
import multiprocessing
import json

import skimage.io
import skimage.color
import skvideo.measure
import scipy

# fix for old skvideo version
import numpy as np
import PIL
from PIL import Image


def imresize(image, factor, interp="nearest", mode=None):
    """
    resize an image with a specified resizing factor, this factor can also be
    the target shape of the resized image specified as tuple.
    """
    interp_methods = {
        "nearest": PIL.Image.NEAREST,
        "bicubic": PIL.Image.BICUBIC,
        "bilinear": PIL.Image.BILINEAR,
    }
    assert interp in interp_methods

    if type(factor) != tuple:
        new_shape = (int(factor * image.shape[0]), int(factor * image.shape[1]))
    else:
        assert len(factor) == 2
        new_shape = factor

    h, w = new_shape
    return np.array(
        Image.fromarray(image, mode=mode).resize(
            (w, h), resample=interp_methods[interp.lower()]
        )
    )


scipy.misc.imresize = imresize
# fix end


def extract_niqe(image):
    """extract niqe score for a given image

    Args:
        image (image): image

    Returns:
        dict: imagename and predicted niqe score
    """
    img = skimage.io.imread(image)

    gray = skimage.color.rgb2gray(img)
    niqe = skvideo.measure.niqe(gray)
    print(f"{image} done")
    return {"image": image, "niqe": float(niqe[0])}


def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(
        description="extract niqe feature",
        epilog="stg7 2020",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("image", nargs="+", type=str, help="image to be used")
    parser.add_argument(
        "--cpu_count",
        type=int,
        default=multiprocessing.cpu_count() // 2,
        help="thread/cpu count",
    )
    parser.add_argument(
        "--report_file", type=str, default="niqe.json", help="file to store predictions"
    )

    a = vars(parser.parse_args())

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    results = pool.map(extract_niqe, a["image"])
    with open(a["report_file"], "w") as xfp:
        json.dump(results, xfp, indent=4)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

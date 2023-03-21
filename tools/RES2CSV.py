#!/usr/bin/env python3
"""
Created on Sat Oct 15 11:51:27 2022

@author: Rasmus Merten
"""
# first python libs
import os
import argparse
import glob

# then external dependencies
import pandas as pd

# then own imports


def res_2_csv(filepath, csvfilename="all.csv"):
    result = []
    for folder in glob.glob(filepath + "/*/"):
        for file in glob.glob(folder + "/*.res"):

            modelname = os.path.basename(file).split(".")[0]
            metric = os.path.basename(file).split(".")[1]

            with open(file, "r") as f:
                for line in f:
                    img_id = line.split("\t")[0]
                    quality_score = float(line.split("\t")[1])
                    result.append(
                        {
                            "model": modelname,
                            "metric": metric,
                            "img_id": img_id,
                            "quality_score": quality_score
                        }
                    )
    df = pd.DataFrame(result)
    df.to_csv(
        path_or_buf= csvfilename,
        index = False
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="res2csv", epilog="Rasmus 2022",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--results", default="iqa_models", type=str,
        help="folder in which subfolders with results for each model are stored"
    )
    parser.add_argument(
        "--csvfilename", default="iqa_models/iqa.csv", type=str,
        help="csv to store all aggregated scores"
    )
    a = vars(parser.parse_args())
    res_2_csv(a["results"], a["csvfilename"])
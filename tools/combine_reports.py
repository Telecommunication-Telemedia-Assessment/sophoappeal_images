#!/usr/bin/env python3

import glob
import json


def combine(reports, resultreport):
    print(reports)
    result = []
    for r in reports:
        db = r.split("_nima")[0]
        with open(r) as rfp:
            j = json.load(rfp)
            for i in j:
                i["db"] = db
                result.append(i)
    with open(resultreport, "w") as rfp:
        json.dump(result, rfp, indent=4)



combine(list(glob.glob("*_appeal.json")), "../nima_appeal.json")
combine(list(glob.glob("*_quality.json")), "../nima_quality.json")

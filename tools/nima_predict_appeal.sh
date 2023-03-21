#!/bin/bash
cd image-quality-assessment

for d in $(pwd)/../../*/images; do

    dd=$(realpath $d)
    db=$(basename $(dirname $dd))
    echo $db


    ./predict  \
        --docker-image nima-cpu \
        --base-model-name MobileNet \
        --weights-file $(pwd)/models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5 \
        --image-source $dd | grep -v "step" > ./../"$db"_nima_prediction_appeal.json
done



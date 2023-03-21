#!/bin/bash
cd visual-sentiment-analysis
source venv/bin/activate
pip3 install -r requirements.txt
find ../../../images/*/images  -type f > images_list.txt

python3 predict.py images_list.txt --model vgg19_finetuned_all --batch-size 64 --results ../../visual_sentiment.csv

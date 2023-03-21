# Tools

Some of the tools are not part of this repository, because they are externally.

* NIMA score calculation: https://github.com/idealo/image-quality-assessment
    * will be properly configued using `./prepare.sh`, requires docker to be re-run
* Visual sentiment calculation: https://github.com/fabiocarrara/visual-sentiment-analysis
    * needs some adaptions to store the results for batch processing, requires downloading of the models

* `combine_reports.py` will combine the NIMA per sub-dataset scrores to one file.
* for image quality estimation use: `iqa_models.sh` and then `RES2CSV.py` which will convert the stdout output to csv files.
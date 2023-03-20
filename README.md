# Sohpappeal Images
This repository is part of [Sohpappeal](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal).
Please use the main repository as starting point.
Some analysis script may require subfolders which are organized in the main repo correctly.


This repository is part of the DFG project [Sophoappeal (437543412)](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-elektrotechnik-und-informationstechnik/profil/institute-und-fachgebiete/fachgebiet-audiovisuelle-technik/forschung/dfg-projekt-sophoappeal), it contains images and analysis scripts.


## Requirements

For this repo you need to have git-lfs installed, see [git-lfs](https://git-lfs.github.com/).

* python3, python3-pip, git, imagemagick, wget
* jupyternotebook for the analysis scripts

Run `./prepare.sh` to download all images.

To run all extraction tools in the folder `tools` more dependencies are required, see `tools/README.md`.
This repository contains already all pre-calculated feature values for the dataset.

* `rule_of_thirds.json` and `simplicity.json` have been extracted using [sophoappeal_rule_prediction](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal_rule_prediction).

## Scripts

* `./create_grid_view.sh`: creates overview image of all images, see all.jpg
* `./create_grid_view_crop.sh`: create overview image of all images as cropped variant, see all_crop.jpg

* `analysis_crowd_ratings.ipynb`: crowd ratings, requires a the main repo
* `analysis_crowd_ratings_vs_features.ipynb`: crowd ratings compared to features, requires a the main repo
* `check_features.ipynb`: analysis of fetures
* `check_likes_views.ipynb`: check likes and views
* `check_nima_niqe.ipynb`: evaluate nima and niqe
* `check_photo_rules.ipynb`: check rule prediction
* `check_resolution.ipynb`: checks resolutions of images
* `check_visual_sentiment.ipynb`: visual sentiment analysis
* `extract_like_view.ipynb`: extracts like and view from the `ratings.csv` of each subdataset.

## Structure
* subdatasets:
    * `500px_cc0`: 500px images
    * `aadb`: images from the AADB dataset
    * `ava`: images from the AVA dataset
    * `koniq10k`: koniq10k images
    * `own`: own images
    * `pixabay_first50k`: images from Pixabay
* `tools`: tools for feature extraction



## Hints

Each of the database folders has a `ratings.csv` with some scores from the original databases.
Each database has further `<database>/{small,medium}` subfolders, where smaller resolution variants of the photos are stored, they are e.g. used in the corresponding crowd tests.


## Acknowledgments

If you use this software or data in your research, please include a link to the repository and reference the following paper.

```bibtex
@article{goering2023imageappeal,
  title={Image Appeal Revisited: Analysis, new Dataset and Prediction Models},
  author={Steve G\"oring and Alexander Raake},
  journal={IEEE Access},
  year={2023},
  publisher={IEEE},
  note={to appear}
}
```

## License
GNU General Public License v3. See [LICENSE.md](./LICENSE.md) file in this repository.
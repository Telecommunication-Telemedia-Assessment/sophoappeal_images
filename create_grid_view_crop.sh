#!/bin/bash

montage -density 100 -tile 50x0 -geometry +0+0 -border 0  */crop_small/* all_crop.jpg
mogrify -resize 40% -quality 70  all_crop.jpg
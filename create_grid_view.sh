#!/bin/bash

montage -density 100 -tile 50x0 -geometry +0+0 -border 0  */small/* all.jpg
mogrify -resize 20% -quality 70  all.jpg
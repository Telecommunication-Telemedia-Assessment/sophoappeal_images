#!/bin/bash

git clone https://github.com/idealo/image-quality-assessment.git
cd image-quality-assessment
git checkout dceaf7c2d218bc6e80b21d6e147e3b56a21b7f31
git apply ../image-quality-assessment.patch
cd ..

echo "check the image-quality-assessment readme, to setup docker container"
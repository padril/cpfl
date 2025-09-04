#!/bin/bash

custom_zip() {
    zip -r $1 $2 -x \
        \*/.mypy_cache/\* \
        \*/__pycache__/\* \
        \*/.ipynb_checkpoints/\* \
        \*/.log
}

cd updated/

rm ../docs/assets/zips/*.zip
cp ./Hub.ipynb ../docs/assets/notebooks/

custom_zip setup.zip ./Module_A/
mv setup.zip ../docs/assets/zips/

custom_zip bubblegum.zip ./Module_B/
mv bubblegum.zip ../docs/assets/zips/

custom_zip calisson.zip ./Module_C/
mv calisson.zip ../docs/assets/zips/

custom_zip dumle.zip ./Module_D/
mv dumle.zip ../docs/assets/zips/

cd -



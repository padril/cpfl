#!/bin/bash

rm ./docs/assets/zips/*.zip
cd ./updated/
cp ./Hub.ipynb ../docs/assets/notebooks/
for f in *; do
    if [ -d $f ]; then
        rm $f.zip
        zip -r $f.zip $f/
        mv $f.zip ../docs/assets/zips/
    fi
done
cd -


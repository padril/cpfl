#!/bin/bash

rm ./zips/*.zip
cd ./updated/
for f in *; do
    if [ -d $f ]; then
        rm $f.zip
        zip -r $f.zip $f/
        mv $f.zip ../zips/
    fi
done
cd -


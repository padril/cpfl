#!/bin/bash

rm ./zips/*.zip
for f in ./updated/*; do
    if [ -d $f ]; then
        cd $f
        rm $(basename $f).zip
        zip $(basename $f).zip *
        cd -
        mv $f/$(basename $f).zip ./zips/
    fi
done


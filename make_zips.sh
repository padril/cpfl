#!/bin/bash

cd updated/

rm ../docs/assets/zips/*.zip
cp ./Hub.ipynb ../docs/assets/notebooks/

zip -r setup.zip ./Module_A/
mv setup.zip ../docs/assets/zips/

zip -r bubblegum.zip ./Module_B/
mv bubblegum.zip ../docs/assets/zips/

zip -r calisson.zip ./Module_C/
mv calisson.zip ../docs/assets/zips/

zip -r dumle.zip ./Module_D/
mv dumle.zip ../docs/assets/zips/

cd -



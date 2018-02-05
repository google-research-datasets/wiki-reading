#!/bin/bash

echo "Downloading Turkish WikiReading TensorFlow Records..."

CLOUD_STORAGE=https://storage.googleapis.com/wikireading

wget https://github.com/google-research-datasets/wiki-reading/blob/master/README.md
mkdir tr
cd tr
wget ${CLOUD_STORAGE}/tr/answer.vocab
wget ${CLOUD_STORAGE}/tr/document.vocab
wget ${CLOUD_STORAGE}/tr/type.vocab
wget ${CLOUD_STORAGE}/tr/character.vocab
wget -c ${CLOUD_STORAGE}/tr/valid.tar.gz
tar xvzf valid.tar.gz &
wget -c ${CLOUD_STORAGE}/tr/test.tar.gz
tar xvzf test.tar.gz &
wget -c ${CLOUD_STORAGE}/tr/train.tar.gz
tar xvzf train.tar.gz

echo "Done."
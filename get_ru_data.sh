#!/bin/bash

echo "Downloading Russian WikiReading TensorFlow Records..."

CLOUD_STORAGE=https://storage.googleapis.com/wikireading

wget https://github.com/google-research-datasets/wiki-reading/blob/master/README.md
mkdir ru
cd ru
wget ${CLOUD_STORAGE}/ru/answer.vocab
wget ${CLOUD_STORAGE}/ru/document.vocab
wget ${CLOUD_STORAGE}/ru/type.vocab
wget ${CLOUD_STORAGE}/ru/character.vocab
wget -c ${CLOUD_STORAGE}/ru/valid.tar.gz
tar xvzf valid.tar.gz &
wget -c ${CLOUD_STORAGE}/ru/test.tar.gz
tar xvzf test.tar.gz &
wget -c ${CLOUD_STORAGE}/ru/train.tar.gz
tar xvzf train.tar.gz

echo "Done."
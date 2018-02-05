#!/bin/bash

echo "Downloading English WikiReading TensorFlow Records..."

CLOUD_STORAGE=https://storage.googleapis.com/wikireading

wget https://github.com/google-research-datasets/wiki-reading/blob/master/README.md
wget ${CLOUD_STORAGE}/answer.vocab
wget ${CLOUD_STORAGE}/document.vocab
wget ${CLOUD_STORAGE}/raw_answer.vocab
wget ${CLOUD_STORAGE}/type.vocab
wget ${CLOUD_STORAGE}/character.vocab
wget -c ${CLOUD_STORAGE}/validation.tar.gz
tar xvzf validation.tar.gz &
wget -c ${CLOUD_STORAGE}/test.tar.gz
tar xvzf test.tar.gz &
wget -c ${CLOUD_STORAGE}/train.tar.gz
tar xvzf train.tar.gz

echo "Done."

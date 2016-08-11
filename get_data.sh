#!/bin/bash

echo "Downloading WikiReading..."

wget https://github.com/dmorr-google/wiki-reading/blob/master/README.md
wget https://github.com/dmorr-google/wiki-reading/blob/master/data/answer.vocab
wget https://github.com/dmorr-google/wiki-reading/blob/master/data/document.vocab
wget https://github.com/dmorr-google/wiki-reading/blob/master/data/raw_answer.vocab
wget https://github.com/dmorr-google/wiki-reading/blob/master/data/type.vocab
wget -c https://storage.googleapis.com/wikireading/validation.tar.gz
tar xvzf validation.tar.gz &
wget -c https://storage.googleapis.com/wikireading/test.tar.gz
tar xvzf test.tar.gz &
wget -c https://storage.googleapis.com/wikireading/train.tar.gz
tar xvzf train.tar.gz

echo "Done."

# WikiReading

This repository contains the three WikiReading datasets as used and described in [WikiReading: A Novel Large-scale Language Understanding Task over Wikipedia, Hewlett, et al, ACL 2016](https://arxiv.org/abs/1608.03542) (the English WikiReading dataset) and [Byte-level Machine Reading across Morphologically Varied Languages, Kenter et al, AAAI-18](http://tomkenter.nl/pdf/kenter_byte-level_2018.pdf) (the Turkish and Russian datasets).

Run `get_data.sh` to download data the English WikiReading dataset.

Run `get_ru_data.sh` and `get_tr_data.sh` to get the Russian and Turkish version of the WikiReading data, respectively.

If you use the data or the results reported in the papers, please feel free to cite them.

    @inproceedings {hewlett2016wikireading,
     title = {{WIKIREADING}: A Novel Large-scale Language Understanding Task over {Wikipedia}},
     booktitle = {Proceedings of the The 54th Annual Meeting of the Association for Computational Linguistics (ACL 2016)},
     author = {Daniel Hewlett and Alexandre Lacoste and Llion Jones and Illia Polosukhin and Andrew Fandrianto and Jay Han and Matthew Kelcey and David Berthelot},
     year = {2016}
    }

and

    @inproceedings{byte-level2018kenter,
      title={Byte-level Machine Reading across Morphologically Varied Languages},
      author={Tom Kenter and Llion Jones and Daniel Hewlett},
      booktitle={Proceedings of the The Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18)},
      year={2018}
    }

## WikiReading Data

Train, validation, and test datasets are in [TFRecord](https://www.tensorflow.org/versions/r0.10/how_tos/reading_data/index.html#file-formats)
or streamed JSON (one JSON object per line). They are 45GB, 5GB, and 3GB respectively.
For example test.tar.gz contains 15 files whose union is the whole test set.
We split them to help speed up training/testing by parallelizing reads.
Any one of the shards can be opened with a [TFRecordReader](https://www.tensorflow.org/versions/r0.10/api_docs/python/io_ops.html#TFRecordReader)
or with your favorite JSON reader for every line.
[Download a sample TFRecord shard](https://storage.googleapis.com/wikireading/validation-00000-of-00015) 
or [a sample JSON shard](https://storage.googleapis.com/wikireading/validation-00000-of-00015.json)
of the validation set (1/15th) to play around with if disk space is limited.

### English
| file             | size               | description                                                            |
|------------------|--------------------|------------------------------------------------------------------------|
| train            | 16,039,400 examples| TFRecord https://storage.googleapis.com/wikireading/train.tar.gz       |
|                  |                    | JSON https://storage.googleapis.com/wikireading/train.json.tar.gz      |
| validation       | 1,886,798 examples | TFRecord https://storage.googleapis.com/wikireading/validation.tar.gz  |
|                  |                    | JSON https://storage.googleapis.com/wikireading/validation.json.tar.gz |
| test             | 941,280 examples   | TFRecord https://storage.googleapis.com/wikireading/test.tar.gz        |
|                  |                    | JSON https://storage.googleapis.com/wikireading/test.json.tar.gz       |
| document.vocab   | 176,978 tokens     | vocabulary for tokens from Wikipedia documents                         |
| answer.vocab     | 10,876 tokens      | vocabulary for tokens from answers                                     |
| raw_answer.vocab | 1,359,244 tokens   | vocabulary for whole answers as they appear in WikiData                |
| type.vocab       | 80 tokens          | vocabulary for Part of Speech tags                                     |
| character.vocab  | 12486 tokens       | vocabulary for all characters that appear in the string sequences      |

### Russian
| file             | size               | description                                                            |
|------------------|--------------------|------------------------------------------------------------------------|
| train            | 4,259,667 examples | TFRecord https://storage.googleapis.com/wikireading/ru/train.tar.gz    |
|                  |                    | JSON https://storage.googleapis.com/wikireading/ru/train.json.tar.gz   |
| validation       | 531,412 examples   | TFRecord https://storage.googleapis.com/wikireading/ru/valid.tar.gz    |
|                  |                    | JSON https://storage.googleapis.com/wikireading/ru/valid.json.tar.gz   |
| test             | 533,026 examples   | TFRecord https://storage.googleapis.com/wikireading/ru/test.tar.gz     |
|                  |                    | JSON https://storage.googleapis.com/wikireading/ru/test.json.tar.gz    |
| document.vocab   | 965,157 tokens     | vocabulary for tokens from Wikipedia documents                         |
| answer.vocab     | 57,952 tokens      | vocabulary for tokens from answers                                     |
| type.vocab       | 56 tokens          | vocabulary for Part of Speech tags                                     |
| character.vocab  | 12,205 tokens      | vocabulary for all characters that appear in the string sequences      |

### Turkish
| file             | size               | description                                                            |
|------------------|--------------------|------------------------------------------------------------------------|
| train            | 654,705 examples   | TFRecord https://storage.googleapis.com/wikireading/tr/train.tar.gz    |
|                  |                    | JSON https://storage.googleapis.com/wikireading/tr/train.json.tar.gz   |
| validation       | 81,622 examples    | TFRecord https://storage.googleapis.com/wikireading/tr/valid.tar.gz    |
|                  |                    | JSON https://storage.googleapis.com/wikireading/tr/valid.json.tar.gz   |
| test             | 82,643 examples    | TFRecord https://storage.googleapis.com/wikireading/tr/test.tar.gz     |
|                  |                    | JSON https://storage.googleapis.com/wikireading/tr/test.json.tar.gz    |
| document.vocab   | 215,294 tokens     | vocabulary for tokens from Wikipedia documents                         |
| answer.vocab     | 11,123 tokens      | vocabulary for tokens from answers                                     |
| type.vocab       | 10 tokens          | vocabulary for Part of Speech tags                                     |
| character.vocab  | 6638 tokens        | vocabulary for all characters that appear in the string sequences      |

## Features

Each instance contains these features (some features may be empty).

| feature name                 | description                                                                      |
|------------------------------|----------------------------------------------------------------------------------|
| `answer_breaks`              |  Indices into `answer_ids` and `answer_string_sequence`.                         |
|                              |  Used to delimit multiple answers to a question, e.g. a list answer.             |
| `answer_ids`                 | `answer.vocab` ID sequence for words in the answer.                              |
| `answer_location`            | Word indices into the document where any one token in the answer was found.      |
| `answer_sequence`            | `document.vocab` ID sequence for words in the answer.                            |
| `answer_string_sequence`     | String sequence for the words in the answer.                                     |
| `break_levels`               | One integer [0,4] indicating a break level for each word in the document.        |
|                              | * 0 = no separation between tokens                                               |
|                              | * 1 = tokens separated by space                                                  |
|                              | * 2 = tokens separated by line break                                             |
|                              | * 3 = tokens separated by sentence break                                         |
|                              | * 4 = tokens separated by paragraph break                                        |
| `document_sequence`          | `document.vocab` ID sequence for words in the document.                          |
| `full_match_answer_location` | Word indices into the document where all contiguous tokens in answer were found. |
| `paragraph_breaks`           | Word indices into the document indicating a paragraph boundary.                  |
| `question_sequence`          | `document.vocab` ID sequence for words in the question.                          |
| `question_string_sequence`   | String sequence for the words in the question.                                   |
| `raw_answer_ids`             | `raw_answer.vocab` ID for the answer.                                            |
| `raw_answers`                | A string containing the raw answer.                                              |
| `sentence_breaks`            | Word indices into the document indicating a sentence boundary.                   |
| `string_sequence`            | String sequence for the words in the document. `character.vocab` for char IDs.   |
| `type_sequence`              | `type.vocab` ID sequence for tags (POS, type, etc.) in the document.             |

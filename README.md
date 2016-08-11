# WikiReading

http://www.aclweb.org/anthology/P/P16/P16-1145.pdf

Run get_data.sh to download data used in this paper.

## WikiReading Data

Train, validation, and test datasets are in [TFRecord](https://www.tensorflow.org/versions/r0.10/how_tos/reading_data/index.html#file-formats) format. 
For example test.tar.gz contains 15 files whose union is the whole test set.
We split them to help speed up training/testing by parallelizing reads.
Any one of the shards can be opened with a [TFRecordReader](https://www.tensorflow.org/versions/r0.10/api_docs/python/io_ops.html#TFRecordReader).

| file             | size               | description                                                  |
|------------------|--------------------|--------------------------------------------------------------|
| train            | 16,039,400 examples| https://storage.googleapis.com/wikireading/train.tar.gz      |
| validation       | 1,886,798 examples | https://storage.googleapis.com/wikireading/validation.tar.gz |
| test             | 941,280 examples   | https://storage.googleapis.com/wikireading/test.tar.gz       |
| document.vocab   | 176,978 tokens     | vocabulary for tokens from Wikipedia documents               |
| answer.vocab     | 10,876 tokens      | vocabulary for tokens from answers                           |
| raw_answer.vocab | 1,359,244 tokens   | vocabulary for whole answers as they appear in WikiData      |
| type.vocab       | 80 tokens          | vocabulary for Part of Speech tags                           |

### Features

| TFRecord feature name        | description                                                                      |
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
| `string_sequence`            | String sequence for the words in the document.                                   |
| `type_sequence`              | `type.vocab` ID sequence for tags (POS, type, etc.) in the document.             |

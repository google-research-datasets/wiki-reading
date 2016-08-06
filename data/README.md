## WikiReading Data

Train, validation, and test datasets are in [TFRecord](https://www.tensorflow.org/versions/r0.10/how_tos/reading_data/index.html#file-formats) form.

| file             | size            | description                                                  |
|------------------|-----------------|--------------------------------------------------------------|
| train            | 16,039,400      | https://storage.googleapis.com/wikireading/train.tar.gz      |
| validation       | 1,886,798       | https://storage.googleapis.com/wikireading/validation.tar.gz |
| test             | 941,280         | https://storage.googleapis.com/wikireading/test.tar.gz       |
| document.vocab   | 176,978 tokens  | vocabulary for tokens from Wikipedia documents               |
| answer.vocab     | 10,876 tokens   | vocabulary for tokens from answers                           |
| raw_answer.vocab | 1,359,244 tokens| vocabulary for whole answers as they appear in WikiData      |
| type.vocab       | 80 tokens       | vocabulary for Part of Speech tags                           |

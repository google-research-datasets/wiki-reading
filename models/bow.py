# Copyright 2016 The Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Bag of embeddings model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow.contrib import learn
from tensorflow.contrib import layers

import utils

VOCAB_SIZE = 10000
EMBED_DIM = 20
ANSWER_DIM = 2 * EMBED_DIM
ANSWER_NUM = 5000
BATCH_SIZE = 128
LEARNING_RATE = 0.01
HIDDEN_SIZE = 128
SPARSE_FEATURES = ['document_sequence', 'question_sequence']


def get_wikireading_input():
  filename = "../train-*"
  feature_info = {k: tf.VarLenFeature(dtype=tf.int64) for k in SPARSE_FEATURES}
  feature_info['answer_ids'] = tf.VarLenFeature(dtype=tf.int64)
  def input_fn():
    features = learn.read_batch_features(
        filename, BATCH_SIZE, feature_info,
        reader=tf.TFRecordReader)
    target = features.pop('answer_ids')
    target = utils.resize_axis(tf.sparse_tensor_to_dense(target), 1, 1)
    return features, target
  return input_fn


def bow_model(features, target):
  document = utils.prune_out_of_vocab_ids(features['document_sequence'], VOCAB_SIZE)
  question = utils.prune_out_of_vocab_ids(features['question_sequence'], VOCAB_SIZE)
  answers = tf.squeeze(tf.one_hot(target, ANSWER_NUM, 1.0, 0.0),
                       squeeze_dims=[1])
  embeddings = tf.get_variable('embeddings', [VOCAB_SIZE, EMBED_DIM])
  doc_enc = layers.safe_embedding_lookup_sparse(
      [embeddings], document, None, combiner='sum')
  question_enc = layers.safe_embedding_lookup_sparse(
      [embeddings], question, None, combiner='sum')
  joint_enc = tf.concat(1, [doc_enc, question_enc])
  answer_embeddings = tf.get_variable(
      'answer_embeddings', [ANSWER_DIM, ANSWER_NUM])
  answer_biases = tf.get_variable('answer_biases', [ANSWER_NUM])
  softmax, loss = learn.ops.softmax_classifier(
      joint_enc, answers, answer_embeddings, answer_biases)
  train_op = layers.optimize_loss(
      loss, tf.contrib.framework.get_global_step(),
      learning_rate=LEARNING_RATE,
      optimizer='Adam')
  return softmax, loss, train_op


def main():
  tf.logging.set_verbosity(tf.logging.INFO)
  estimator = learn.Estimator(
    model_fn=bow_model,
    model_dir="results/bow/",
  )
  estimator.fit(input_fn=get_wikireading_input(), steps=10000)


if __name__ == "__main__":
  main()


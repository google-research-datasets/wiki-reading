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

"""Utils for all models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def resize_axis(tensor, axis, new_size, fill_value=0):
  """Truncates or pads a tensor to new_size on on a given axis.

  Truncate or extend tensor such that tensor.shape[axis] == new_size. If the
  size increases, the padding will be performed at the end, using fill_value.

  Args:
    tensor: The tensor to be resized.
    axis: An integer representing the dimension to be sliced.
    new_size: An integer or 0d tensor representing the new value for
      tensor.shape[axis].
    fill_value: Value to use to fill any new entries in the tensor. Will be
      cast to the type of tensor.

  Returns:
    The resized tensor.
  """
  tensor = tf.convert_to_tensor(tensor)
  shape = tf.unpack(tf.shape(tensor))

  pad_shape = shape[:]
  pad_shape[axis] = tf.maximum(0, new_size - shape[axis])

  shape[axis] = tf.minimum(shape[axis], new_size)
  shape = tf.pack(shape)

  resized = tf.concat(axis, [
      tf.slice(tensor, tf.zeros_like(shape), shape),
      tf.fill(tf.pack(pad_shape), tf.cast(fill_value, tensor.dtype))
  ])

  # Update shape.
  new_shape = tensor.get_shape().as_list()  # A copy is being made.
  new_shape[axis] = new_size
  resized.set_shape(new_shape)
  return resized


def prune_out_of_vocab_ids(sparse_ids, vocab_size):
  """Prunes out of vocabulary ids from given SparseTensor."""
  is_id_valid = tf.less(sparse_ids.values, vocab_size)
  return tf.sparse_retain(sparse_ids, is_id_valid)


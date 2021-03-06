# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import unittest

from model import evals


class TestComputeSequenceMatchAccuracy(unittest.TestCase):

  def test_get_list_inverse_index(self):
    unique_ids = ['a', 3, 'abc']
    expected = {
      'a': 0,
      3: 1,
      'abc': 2
    }
    self.assertDictEqual(
        expected,
        evals.get_list_inverse_index(unique_ids))

  def test_mismatched_sequences(self):
    sequence1 = [0, 0, 1, 2, 2]
    sequence2 = [3, 3, 4, 4, 1]
    accuracy = evals.compute_sequence_match_accuracy(
        sequence1, sequence2)
    self.assertEqual(0.8, accuracy)

  def test_equivalent_sequences(self):
    sequence1 = [0, 0, 1, 2, 2]
    sequence2 = [3, 3, 4, 1, 1]
    accuracy = evals.compute_sequence_match_accuracy(
        sequence1, sequence2)
    self.assertEqual(1.0, accuracy)

  def test_symmetry(self):
    sequence1 = [1] * 10 + [2] * 20 + [3] * 30 + [4] * 40
    sequence2 = [1] * 10 + [2] * 20 + [3] * 30 + [4] * 40
    random.shuffle(sequence1)
    random.shuffle(sequence2)
    accuracy1 = evals.compute_sequence_match_accuracy(
        sequence1, sequence2)
    accuracy2 = evals.compute_sequence_match_accuracy(
        sequence2, sequence1)
    self.assertEqual(accuracy1, accuracy2)

  def test_sequences_of_different_lengths(self):
    sequence1 = [0, 0, 1, 2]
    sequence2 = [3, 3, 4, 4, 1]
    with self.assertRaises(Exception):
      evals.compute_sequence_match_accuracy(sequence1, sequence2)

  def test_empty_sequences(self):
    with self.assertRaises(Exception):
      evals.compute_sequence_match_accuracy([], [])


if __name__ == '__main__':
  unittest.main()

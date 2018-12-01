#! /usr/bin/python
import unittest
import itertools
from typing import List
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as input1:
    data = input1.read().strip()
    frequencies = list(map(int, data.splitlines()))


def change_frequency(l: List[int]) -> int:
    return sum(l)


def frequency_reached_twice(l: List[int]) -> int:
    found = set([0])
    current_freq = 0
    for change in itertools.cycle(l):
        current_freq += change
        if current_freq in found:
            return current_freq
        else:
            found.add(current_freq)


class Tests(unittest.TestCase):

    def test_p1_sample(self):
        self.assertEqual(change_frequency([+1, -2, +3, +1]), 3)

    def test_p1_sample1(self):
        self.assertEqual(change_frequency([+1, +1, +1]), 3)

    def test_p1_sample2(self):
        self.assertEqual(change_frequency([+1, +1, -2]), 0)

    def test_p1_sample3(self):
        self.assertEqual(change_frequency([-1, -2, -3]), -6)

    def test_p2_sample(self):
        self.assertEqual(frequency_reached_twice([+1, -2, +3, +1]), 2)

    def test_p2_sample1(self):
        self.assertEqual(frequency_reached_twice([+1, -1]), 0)

    def test_p2_sample2(self):
        self.assertEqual(frequency_reached_twice([+3, +3, +4, -2, -4]), 10)

    def test_p2_sample3(self):
        self.assertEqual(frequency_reached_twice([-6, +3, +8, +5, -6]), 5)

    def test_p2_sample4(self):
        self.assertEqual(frequency_reached_twice([+7, +7, -2, -7, -4]), 14)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
    print(change_frequency(frequencies))  # 486
    print(frequency_reached_twice(frequencies))  # 69285

#! /usr/bin/python
import unittest
from typing import List
import itertools
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r', encoding='utf-8') as input1:
    data = input1.read().strip()
    box_input: List[str] = [line for line in data.splitlines()]


def checksum(box_ids: List[str]) -> int:
    boxes = [Box(l) for l in box_ids]
    doubles = [box for box in boxes if box.has_doubles()]
    triples = [box for box in boxes if box.has_triples()]
    return len(doubles) * len(triples)


class Box:
    id: str
    groups: []

    def __init__(self, id: str):
        self.id = id
        self.groups = [{k: len(list(g))} for k, g in itertools.groupby(sorted(list(id)))]

    def has_doubles(self) -> bool:
        double = [item for item in self.groups if 2 in item.values()]
        return double != []

    def has_triples(self) -> bool:
        tripple = [item for item in self.groups if 3 in item.values()]
        return tripple != []


def fabric_pairs(box_ids: List[str]) -> (str, str):
    for id1 in box_ids:
        for id2 in box_ids:
            if id1 == id2:
                continue  # same id, not common
            diff = 0
            for i in range(len(id1)):
                if diff > 1:
                    break
                if id1[i] != id2[i]:
                    diff = diff + 1
            if diff == 1:
                return id1, id2


def common_letters(pair: (str, str)) -> str:
    return "".join(letter for letter in pair[0] if letter in pair[1])


class Tests(unittest.TestCase):
    def test_box_has_no_doubles(self):
        self.assertEqual(Box("abcdef").has_doubles(), False)

    def test_box_has_no_triples(self):
        self.assertEqual(Box("abcdef").has_triples(), False)

    def test_box_has_doubles(self):
        self.assertEqual(Box("bababc").has_doubles(), True)

    def test_box_has_triples(self):
        self.assertEqual(Box("bababc").has_triples(), True)

    def test_p1_checksum_sample(self):
        self.assertEqual(checksum(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), 12)

    def test_fabric_pairs(self):
        self.assertEqual(fabric_pairs(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]),
                         ("fghij", "fguij"))

    def test_common_letters(self):
        self.assertEqual(common_letters(("fghij", "fguij")), "fgij")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
    print(f'checksum {checksum(box_input)}')  # 6972
    pair = fabric_pairs(box_input)  # ('aixwcbzrmdvpsjfgllthdyeoqe', 'aixwcbzrmdvpsjfgllthdyioqe')
    print(f'boxes with fabric: {pair}')
    print(f'common letters: {common_letters(pair)}')  # aixwcbzrmdvpsjfgllthdyoqe

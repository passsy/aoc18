#! /usr/bin/python
import unittest
from typing import List
from os import path
import re

with open(path.join(path.dirname(__file__), 'input.txt'), 'r', encoding='utf-8') as input1:
    data = input1.read().strip()
    claims: List[str] = [line for line in data.splitlines()]


class Rect:
    id: str
    x: int
    y: int
    width: int
    height: int

    def __init__(self, id: str, x: int, y: int, width: int, height: int):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def squared_claimed_multiple_times(claims: List[Rect]) -> int:
    fabric = [[0 for x in range(1000)] for y in range(1000)]

    for rect in claims:
        for y in range(rect.x, rect.x + rect.width):
            for x in range(rect.y, rect.y + rect.height):
                fabric[x][y] = fabric[x][y] + 1

    multiClaims = 0
    for y in range(1000):
        for x in range(1000):
            if fabric[x][y] > 1:
                multiClaims = multiClaims + 1

    return multiClaims


def claimed_once(claims: List[Rect]) -> Rect:
    fabric = [[0 for x in range(1000)] for y in range(1000)]

    for rect in claims:
        for y in range(rect.x, rect.x + rect.width):
            for x in range(rect.y, rect.y + rect.height):
                fabric[x][y] = fabric[x][y] + 1

    for rect in claims:
        try:
            for y in range(rect.x, rect.x + rect.width):
                for x in range(rect.y, rect.y + rect.height):
                    if fabric[x][y] > 1:
                        raise Exception("has overlap")
            return rect
        except Exception:
            rect.height

    raise Exception("no rect found without overlap")


def to_rect(s: str) -> Rect:
    match = re.match(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', s)
    return Rect(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)))


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
    parsedClaims = [to_rect(claim) for claim in claims]

    print(f"multiple claimed fields: {squared_claimed_multiple_times(parsedClaims)}")
    print(f"claimed once id: {claimed_once(parsedClaims).id}")

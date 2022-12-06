from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

scale = {'R': 1, 'P': 2, 'S': 3}
win = {'R': 'S', 'S': 'P', 'P': 'R'}

columns = {
    'A': 'R', 'B': 'P', 'C': 'S',
    'X': 'R', 'Y': 'P', 'Z': 'S',
}

R = {'A', 'X'}
P = {'B', 'Y'}
S = {'C', 'Z'}

def compute(s: str) -> int:
    score = 0

    for k, v in columns.items():
        s = s.replace(k, v)

    for line in s.splitlines():
        computer, user = line.split()
        if computer == user:
            score += 3
        elif win[user] == computer:
            score += 6
        score += scale[user]
    return score

INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 15


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

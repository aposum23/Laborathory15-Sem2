#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Rangechecker:
    first = None
    second = None

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __del__(self):
        self.first = None
        self.second = None
        print('Object has been deleted!')

    def __lt__(self, other):
        if other > self.second:
            return True
        else:
            return False

    def __gt__(self, other):
        if other < self.first:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.second > other >= self.first:
            return True
        else:
            return False

    def read(self):
        first = int(input('first: '))
        self.first = first
        second = int(input('second: '))
        self.second = second

    def display(self):
        print(f'first: {self.first}; second: {self.second}')

    def rangecheck(self, num):
        print(f'Num is: {num}')
        print(f'Num in diaposon: '
              f'{self.second.__gt__(num) and self.first.__le__(num)}')
        print(f'Start: {self.first}; end: {self.second}')


def main():
    diap = Rangechecker(10, 16)
    x = random.randint(0, 20)
    diap.rangecheck(x)
    diap.display()
    diap.read()
    x = random.randint(0, 20)
    diap.rangecheck(x)
    print(f'diap < x: {diap < x}')
    print(f'diap > x: {diap > x}')
    print(f'diap == x: {diap == x}')


if __name__ == '__main__':
    main()

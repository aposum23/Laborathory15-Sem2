#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    lst = None
    length = None

    def __init__(self, length):
        self.lst = []
        self.length = length

    def __getitem__(self, key):
        elem = self.lst[key]
        return elem

    def __setitem__(self, key, value):
        currency = value[0]
        val = value[1]
        self.lst[key] = {'currency': currency, 'value': val}

    def add(self, currency, value):
        self.lst.append({
            'currency': currency,
            'value': value
        })
        if len(self.lst) > self.length:
            self.lst.pop(self.length - 1)
            print('List is full!!!!')


def main():
    money = Money(3)
    money.add('Ruble', 500)
    money.add('Dollar', 6)
    money.add('Euro', 10)
    print(f'First in list: {money[0]}')
    money.add('Frank', 15)
    money[0] = ('Dollar', 100)
    print(f'First in list: {money[0]}')


if __name__ == '__main__':
    main()

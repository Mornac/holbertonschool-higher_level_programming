#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._iterator = iter(iterable)
        self._count = 0

    def get_count(self):
        return self._count

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self._iterator)
            self._count += 1
            return value
        except StopIteration:
            raise StopIteration

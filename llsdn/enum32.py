from __future__ import print_function
import inspect


class Enum:
    def __init__(self, value):
        if isinstance(value, self.__class__):
            self.name = value.name
            return

        attributes = inspect.getmembers(
            self.__class__, lambda a: not(inspect.isroutine(a)))
        members = [a for a in attributes if not(
            a[0].startswith('__') and a[0].endswith('__'))]

        self.name = None
        for mb in members:
            name, val = mb
            if val == value:
                self.name = name
        if self.name is None:
            raise TypeError('{} has no value {}'.format(self.__class__.__name__, value))

    def __eq__(self, other):
        other_enum = self.__class__(other)
        return self.name == other_enum.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)

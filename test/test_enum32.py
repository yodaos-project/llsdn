import unittest
from llsdn.enum32 import Enum


class Foobar(Enum):
    Foo = 1
    Bar = 3


class EnumTest(unittest.TestCase):
    def test_new_value(self):
        foo = Foobar(1)
        try:
            Foobar(2)
        except Exception as e:
            assert(isinstance(e, TypeError))

    def test_eq(self):
        foo = Foobar(1)
        foo_static = Foobar.Foo
        assert(foo == foo_static)

        bar = Foobar(3)
        bar_static = Foobar.Bar
        assert(foo != bar)
        assert(foo != bar_static)


if __name__ == '__main__':
    unittest.main()

import unittest

from gtfs_util import util


class TestCamelToSnake(unittest.TestCase):
    def test_no_upper(self):
        x = 'ateststring'
        self.assertEqual(
            x,
            util.camel_to_snake(x),
        )

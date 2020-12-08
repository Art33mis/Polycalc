import unittest
from PartOfMnogochlen import PartOfMnogochlen


class TestPartOfMnogochlen(unittest.TestCase):

    def setUp(self):
        self._term = PartOfMnogochlen(2, 7)

    def test_get_power(self):
        self.assertEqual(self._term.get_power(), 7)

    def test_get_coefficient(self):
        self.assertEqual(self._term.get_coefficient(), 2)

    def tearDown(self):
        self._term = None


if __name__ == '__main__':
    unittest.main()
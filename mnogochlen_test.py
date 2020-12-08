import unittest
from PartOfMnogochlen import PartOfMnogochlen
from Mnogochlen import Mnogochlen


class TestMnogochlen(unittest.TestCase):

    def setUp(self):
        self._first_polynomial = Mnogochlen([PartOfMnogochlen(2, 2), PartOfMnogochlen(2, 3)])
        self._second_polynomial = Mnogochlen([PartOfMnogochlen(2, 4), PartOfMnogochlen(2, 2)])
        self._result = {6: 4,
                        4: 4,
                        7: 4,
                        5: 4}

    def test_multiply(self):
        self._new_polynomial = Mnogochlen
        self.assertCountEqual(self._new_polynomial.__mul__(self._first_polynomial, self._second_polynomial), )

    def tearDown(self):
        self._term = None












if __name__ == '__main__':
    unittest.main()
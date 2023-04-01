from sequential_search import sequential_search
import unittest

class TestSequentialSearch(unittest.TestCase):

    def test_key_found(self):
        array = [45, 23, 86, 21, 10]
        key = 21
        self.assertEqual(sequential_search(array, key), 3)

    def test_key_not_found(self):
        array = [45, 23, 86, 10]
        key = 21
        self.assertEqual(sequential_search(array, key), -1)


if __name__ == "__main__":
    unittest.main()

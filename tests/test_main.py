import unittest
from main import add_numbers

class TestMain(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
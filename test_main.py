import unittest
from main import scitani, nasobeni

class TestScitani(unittest.TestCase):
    def test_scitani(self):
        self.assertEqual(scitani(2, 3), 5)

    def test_scitani_zaporne(self):
        self.assertEqual(scitani(-5, 8), 3)

    def test_nasobeni(self):
        self.assertEqual(nasobeni(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

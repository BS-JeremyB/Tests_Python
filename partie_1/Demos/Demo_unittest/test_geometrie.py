import unittest
from geometrie import calcul_aire_cercle

class TestGeometrie(unittest.TestCase):
    def test_positif(self):
        self.assertAlmostEqual(calcul_aire_cercle(3), 28.27, places=2)


    def test_zero(self):
        self.assertEqual(calcul_aire_cercle(0), 0)

    def test_negatif(self):
        with self.assertRaises(ValueError):
            calcul_aire_cercle(-3)



if __name__ == '__main__':
    unittest.main(verbosity=2)
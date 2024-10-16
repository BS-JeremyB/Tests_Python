from moyenne import calcul_moyenne
import unittest


class TestMoyenne(unittest.TestCase):
    def test_calcul_moyenne(self):
        self.assertEqual(calcul_moyenne([10,20,30]), 20)
        with self.assertRaises(ValueError):
            calcul_moyenne([])
    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

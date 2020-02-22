import unittest
import NumberToPattern

class Test(unittest.TestCase):

    def test_NumberToPattern(self):
        self.assertEqual(NumberToPattern.NumberToPattern(0, 4), 'AAAA')
        self.assertEqual(NumberToPattern.NumberToPattern(255, 4), 'TTTT')
        with self.assertRaises(ValueError):
            NumberToPattern.NumberToPattern(256, 4)
        

if __name__ == '__main__':
    unittest.main()
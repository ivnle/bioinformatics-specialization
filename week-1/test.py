import unittest
import NumberToPattern
import FasterFrequentWords

class Test(unittest.TestCase):

    def test_NumberToPattern(self):
        self.assertEqual(NumberToPattern.NumberToPattern(0, 4), 'AAAA')
        self.assertEqual(NumberToPattern.NumberToPattern(255, 4), 'TTTT')
        with self.assertRaises(ValueError):
            NumberToPattern.NumberToPattern(256, 4)

    def test_FasterFrequentWords(self):
        self.assertEqual(set(FasterFrequentWords.FasterFrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))

        self.assertEqual(FasterFrequentWords.FasterFrequentWords('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC', 12), ['CGAGGCGACTCG'])

        self.assertEqual(set(FasterFrequentWords.FasterFrequentWords('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC', 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))        

if __name__ == '__main__':
    unittest.main()
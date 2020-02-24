import unittest
import FasterFrequentWords
import FrequentWords
import ReverseComplement
import PatternMatching
from ClumpFinding import ClumpFinding
from NaiveClumpFinding import NaiveClumpFinding
from PatternToNumber import PatternToNumber
from PatternToNumberRecursive import PatternToNumberRecursive
from NumberToPatternRecursive import NumberToPatternRecursive
from NumberToPattern import NumberToPattern

class Test(unittest.TestCase):
    def test_NumberToPatternRecursive(self):
        self.assertEqual(NumberToPatternRecursive(5353, 7), 'CCATGGC')   
        self.assertEqual(NumberToPatternRecursive(6421, 10), 'AAACGCACCC')   

    def test_PatternToNumberRecursive(self):
        self.assertEqual(PatternToNumberRecursive('TCTGAAGTGTAACGA'), 931327000)
        self.assertEqual(PatternToNumberRecursive('CCATCATGAACGCATAA'), 5590489392)
        with self.assertRaises(ValueError):
            PatternToNumberRecursive('')
        with self.assertRaises(ValueError):
            PatternToNumberRecursive('ATBG')    

    def test_PatternToNumber(self):
        self.assertEqual(PatternToNumber('TCTGAAGTGTAACGA'), 931327000)
        self.assertEqual(PatternToNumber('CCATCATGAACGCATAA'), 5590489392)

    def test_ClumpFinding(self):
        self.assertEqual(ClumpFinding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',
        5, 50, 4), ['CGACA', 'GAAGA'])
        self.assertEqual(ClumpFinding('AAAACGTCGAAAAA', 2, 4, 2), ['AA'])
        self.assertEqual(ClumpFinding('ACGTACGT', 1, 5, 2), ['A', 'C', 'G', 'T'])                
        self.assertEqual(ClumpFinding('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG', 
        3, 25, 3), ['AAA', 'CAG', 'CAT', 'CCA', 'GCC', 'TTC'])   
        self.assertEqual(ClumpFinding('GCGGTTATGCACCGTTCAAATTAGCAAACCACTAAGCGACGTAGTCTGGATTGATTTCTCCCTACCAGTGACCCAAGACGCGTTAGTGAGTTAAGTTCATATCCAGTACCTGCCGCCCTCTGTACTTGGGCGTCCGATTCGCATGCTTACTCAGGTGGAGGACACGATAATCTGATTAAACTGAGCTAAACCAGGTGGAACCAGAAACCAGGTGGGGAGTCTCGCTTCAAGCCGTTCTTGCGATCAAACCAGGTGGTCCATTATGAAACCAGGTGGCTAAACCAGGTGGTCCAGATCCTCGAATGATGTCGGTGCACATCAAAACCAGGTGGGGTGGTGGAACGTAAAACCAGGTGGCATAAACCAGGTGGGCCGGTTCGTAAACCAGGTGAAACCAGGTGGGGTGGAAACCAGGTGGGTTACAAATTACGTTGAGATGGCCCAAACCAGGTGGTGGGCTTCACCCATGTCAACAAACCACCCTATGGAACTAAACCAGGTGGAACCAGGTGGTGAAGGCTTATCCTCAGGAAAAACCAGGTGGAGGTGGTGAAATAAAACCAGGTGGACCAGGTGGATAACCCTCGCCTCGCTTCTCAACCGAGACCTGGATAAACCAGGTGGGGTGGTCCACCGATTTTTGAGACACTAGAAACCAGGTGGGCGGGGAAACCAGGTGGCAAACCAGGTGGGGTGGACGGAAACCAGGTGGATATGTCATAAAACCAAACCAGGTGGTGCACCCCCATGGTGTGTCTTATCCGTGCGTATAAACCAGGTGGTCGCACGGCTTCCACTTGCTGAGAATAGGCCCGCAGGGTCAGTGCCATGCCCTCCGTCACTCGATATGTGTTGTAAGAGTGGTTACCCCTTCATTGAAGTCGCCCACAGCCCCACCTGCATTGCTAGACTATCACCCTACAGTAGGCCTTTTCGCCTTCTTCAAGCAGCAATCTCTTATCCGCGGATGGGCGCGGCGAGCGTGGCGTCCCCGAACATTTTTACCTAACGTGTTTTGTTGGCCGCAAGCCTTCCCTCTAGTCCACCTCAGCCATTCAGCCTAGTAGCTTTCAAGCCGAGCCTTCCATATCTAATGGACCGTCCAGAATTTCACACGTTTCACAGGGCTGTGTTCGACCGCCCGTAATGCTGTTTCACAGGCGATCGCCTTGCGGTTTTTTCACAGATCGCAGCCGATGGACATGCCAACTCGATTTTCACAGAGTTTTTCACAGCGGTTTCACAGCACAGCAGTGATTGTTTCACAGCAATTTTCACTTTCACAGGGGCCCTTTTCACAGCTCAGGGCTCTTTTCACTTTCACAGTTTCACAGCGCTCCTTTCACAGAGCGGGGAAATTTAAGGGAACACTCAAGGGAACAAGGGAACACACAAAGGGAACACAACACAACACATAAGGGAACACTTTCACAGAACACAAAAGTCCGAAATCATCAGCGGCGAAGGGATTTCACAGACAGACACTTTCACAGCGCATTTCACAGATACGTACTTTCACAGGCGTACTTTCACAGACTTTCACAGAGGACAAGCTCAATTTTCACAGACAGGCTGGATAAATTTCACAGCGGTAAGGGTTTCACAGCACACATAAGGGAACACGAATTTCACAGCAGGGAACACCTCTACGAGTAATCTATTACTCTACCTACTGAAGGGAACACACCGAAGACCTACTATTACCTATTACTCTTAAAGGGAACACATTACAAGGGAACACACTCTCTCGTCATATCTCACCTCTCTATTACTCTTAAGGGAACACCTTCTCGATCAACCTATTACTCTATGGAGATAGAGATATTCCAGACATATGGAGATAACATGGAGATATGGAGATAATGGAGATGGAGATAGCTCTTATATTTATCCTATGGAGATATGATACTATTAATGGAGATAATTCTAATGGAGATATAATTACTCTAAGAGGATGGGATCTCGGGCTATTACTCTAATGGAGATAAGCACTATTACTCTAGGAAATGGAGATATGTCAATGGAGATATGTAATGGAGATAGAGGGAGATGGAGTCGCCATTTCATAATCGCCATTTCATAGTTCAGGAATCGCCATTTCCGCCATTTCTAAGATGGAGTCGCCATTTCTACGTATGGAGATAGGATCGCCATTTCATACGACCCGTTGGATATCGCCATTTCCTCGCCATTTCTGGTGACATTTCTCGCCATTTCATTTCTGGAGATAGATGGATCTCGCCATTTCATAGGAATCGCCATTTCCACGTAGGGGGGGCCACAATCCGTAGGTCGGAATTCAGACTCGCCATTTCCCATCGCCATTTCTTCACCTGTATGCCGATCCCTTCGCCATTTCTCATGGAGATAACTCTCTCTCGCCATTTCTCGCCATTTCCATTTCACTCTCATTCGCCATCGCCATTTCCATTCGCCATTTCATCGCCATTTCTTCAGGATAAGATATCGCCATTTCGACTCTCATTCGCATACTGACTCTCATTCTCATCTCGCCATTTCTCATCTGACTCTCATCCTGGGGGAAACTTGCGACTCTCATCACACTTCCGTCGACTCTCATACTGGCGGATAGCATAGGAGCCATTTAAAGACTCTCATTCTCATTCGAGACTCTCATTCAAATCCTACGAGGACTCTCATATAGACTCTCATATCATTACGAGGACTCTCATATACGAGCCATGCATGTGGCGACGACTCTCATCTACGAGCCATGCAAGCAGAATCTACGAGCGACTCTCATTACGAGCCATGTGACCGTACGAGCCATGCATGCATGCCATGCTGACTCTCATCGAGTACGAGCCATGGAAGTTCTTGTTGGTTCGTAGCCCAAGAGCTGAAGTTACGAGCCTACGAGCCATGAAGTTACTTTTACGAGCCATGAAGCTTACGATACGAGCCATGCGAGCCATGCATCCGCGCTACGAGCCATGTTCCAGTACGAGCCATGTTAGTTGCTGAAGTTAAGTTTGGCGCTGAAGTTTGTACGAGCCATGTGCCCGCTGAAGTTTGTTGTACGAGCCATGCATGCTGAAGTTAATGGCTGAAGTTAGCGTTTGCGGGCAGATCCTCATTCTACGATACGAGCCATGCCATGCAGCTGAAGTTAAGTTGGGTTACGAGCCATGCGAGCCATGTGAAGTACGAGCCATGCTGGCTGAAGTTGTTTGTGCTGCTGAAGTTGCTCTTGTCTCTAGCTGAAGTTGCCAACAGGGCTGAAGCTGAAGTTTAAGCTGAAGTTGCGAGCAGGCTGAAGTTATCGGATTGGGGCTGAAGTTCAACCTCCCGTCCCCCCACACTATATTCCCGTCCCCCCCCGCGCACGCGCCGTCTCCCGTCCCCCCTATCCCGTGCGCACGCGACGCGATCCCGTCCCCCCAGAGTGCGCGCACGCGTCCCCCTTCCCGTCCCCCTCTCCCGGGCGCACGCGTCGCTCAACATTTCCGCGCACGCGTCGCGCACGCGGGCGCACGCGGGTCCCGTCCCCCCCCCTCTTCGGCGCACGCGGAATTCCCGTCGCGCACGCGTCCCGTCCCGCGCACGCGTCGCGCACGCGACTGCCCTAACCAACAGTGCGCACGCGCCGGTAACCCGGTAACCCGGTAACCGCGCACGCGGGCGCACGCGCGTAACCCGCGCACGCGCCGCGCACGCGGCCCGGTTCCCGTCCCCCCCGGTAACCCGGTAACTCCCGTCCCCCGTAACCCGGTGCGCACGCGCCCGGCGCACGCGGAGCGCACGCGCCCCCCCCGGTAATAGCGCACGCGCCCGGGCGCACGCGCCCGGTAACCCGGTAACCCGGGCGCGCGCACGCGGCGGCGCACGCGGCGCACGCGGCGCACGCG', 
        11, 566, 18), ['AAACCAGGTGG'])

    def test_NaiveClumpFinding(self):
        self.assertEqual(NaiveClumpFinding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',
        5, 50, 4), ['CGACA', 'GAAGA'])
        self.assertEqual(NaiveClumpFinding('AAAACGTCGAAAAA', 2, 4, 2), ['AA'])
        self.assertEqual(NaiveClumpFinding('ACGTACGT', 1, 5, 2), ['A', 'C', 'G', 'T'])                
        self.assertEqual(NaiveClumpFinding('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG', 
        3, 25, 3), ['AAA', 'CAG', 'CAT', 'CCA', 'GCC', 'TTC'])   

    
    def test_PatternMatching(self):
        self.assertEqual(PatternMatching.PatternMatching('ATAT', 'GATATATGCATATACTT'), [1, 3, 9])
        self.assertEqual(PatternMatching.PatternMatching('ACAC', 'TTTTACACTTTTTTGTGTAAAAA'), [4])
        self.assertEqual(PatternMatching.PatternMatching('AAA', 'AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT')
        , [0, 46, 51, 74])
        self.assertEqual(PatternMatching.PatternMatching('TTT', 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT')
        , [88, 92, 98, 132])
        self.assertEqual(PatternMatching.PatternMatching('ATA', 'ATATATA'), [0, 2, 4])

    def test_ReverseComplement(self):
        self.assertEqual(ReverseComplement.ReverseComplement('AAAACCCGGT'), 'ACCGGGTTTT')
        self.assertEqual(ReverseComplement.ReverseComplement('ACACAC'), 'GTGTGT')
        self.assertEqual(ReverseComplement.ReverseComplement('AAAACCCGGT'.lower()), 'ACCGGGTTTT')
        with self.assertRaises(ValueError):
            ReverseComplement.ReverseComplement('BACGT')
        with self.assertRaises(ValueError):
            ReverseComplement.ReverseComplement('ACGTX') 
        with self.assertRaises(ValueError):
            ReverseComplement.ReverseComplement('ACYGT')                

    def test_NumberToPattern(self):
        self.assertEqual(NumberToPattern(0, 4), 'AAAA')
        self.assertEqual(NumberToPattern(255, 4), 'TTTT')
        with self.assertRaises(ValueError):
            NumberToPattern(256, 4)

    def test_FasterFrequentWords(self):
        self.assertEqual(set(FasterFrequentWords.FasterFrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))

        self.assertEqual(FasterFrequentWords.FasterFrequentWords('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC'
        , 12), ['CGAGGCGACTCG'])

        self.assertEqual(set(FasterFrequentWords.FasterFrequentWords('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC'
        , 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))        

    def test_FrequentWords(self):
        self.assertEqual(set(FrequentWords.FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))

        self.assertEqual(FrequentWords.FrequentWords('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC'
        , 12), ['CGAGGCGACTCG'])

        self.assertEqual(set(FrequentWords.FrequentWords('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC'
        , 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))  
        

if __name__ == '__main__':
    unittest.main()
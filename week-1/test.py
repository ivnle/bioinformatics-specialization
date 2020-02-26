import unittest
from FasterFrequentWords import FasterFrequentWords
from FindingFrequentWordsBySorting import FindingFrequentWordsBySorting
from FrequentWords import FrequentWords
import ReverseComplement
import PatternMatching
from ClumpFinding import ClumpFinding
from NaiveClumpFinding import NaiveClumpFinding
from PatternToNumber import PatternToNumber
from PatternToNumberRecursive import PatternToNumberRecursive
from NumberToPatternRecursive import NumberToPatternRecursive
from NumberToPattern import NumberToPattern
from Skew import Skew
from MinimumSkew import MinimumSkew
from HammingDistance import HammingDistance
from ApproximatePatternMatching import ApproximatePatternMatching
from ApproximatePatternCount import ApproximatePatternCount
from FrequentWordsWithMismatches import FrequentWordsWithMismatches

class Test(unittest.TestCase):
    def test_FrequentWordsWithMismatches(self):
        self.assertEqual(set(FrequentWordsWithMismatches('TAGCG', 2, 1)), set(['GG', 'TG']))
        self.assertEqual(set(FrequentWordsWithMismatches('AAT', 3, 0)), set(['AAT']))
        self.assertEqual(set(FrequentWordsWithMismatches('ATA', 3, 1)), set(['GTA', 'ACA', 'AAA', 'ATC', 'ATA', 'AGA', 'ATT', 'CTA', 'TTA', 'ATG']))

    def test_ApproximatePatternCount(self):
        self.assertEqual(ApproximatePatternCount('TTTAGAGCCTTCAGAGG', 'GAGG', 2), 4)
        self.assertEqual(ApproximatePatternCount('AAA', 'AA', 0), 2)
        self.assertEqual(ApproximatePatternCount('ATA', 'ATA', 1), 1)

    def test_ApproximatePatternMatching(self):
        self.assertEqual(ApproximatePatternMatching('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
                                                    ,'ATTCTGGA'
                                                    , 3), [6, 7, 26, 27])
        self.assertEqual(ApproximatePatternMatching('TTTTTTAAATTTTAAATTTTTT'
                                                    ,'AAA'
                                                    , 2), [4, 5, 6, 7, 8, 11, 12, 13, 14, 15])
        self.assertEqual(ApproximatePatternMatching('GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT'
                                                    ,'GAGCGCTGG'
                                                    , 2), [0, 30, 66])
        self.assertEqual(ApproximatePatternMatching('CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA'
                                                    ,'AATCCTTTCA'
                                                    , 3), [3, 36, 74, 137])
        self.assertEqual(ApproximatePatternMatching('CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC'
                                                    ,'CCGTCATCC'
                                                    , 3), [0, 7, 36, 44, 48, 72, 79, 112])
        self.assertEqual(ApproximatePatternMatching('AAAAAA'
                                                    ,'TTT'
                                                    , 3), [0, 1, 2, 3])
        self.assertEqual(ApproximatePatternMatching('CCACCT'
                                                    ,'CCA'
                                                    , 0), [0])                                                                                                                                                                                                                                                                                                                        
    
    def test_HammingDistance(self):
        self.assertEqual(HammingDistance('GGGCCGTTGGT','GGACCGTTGAC'),3)
        self.assertEqual(HammingDistance('AAAA','TTTT'),4)
        self.assertEqual(HammingDistance('ACGTACGT','TACGTACG'),8)
        self.assertEqual(HammingDistance('ACGTACGT','CCCCCCCC'),6)
        self.assertEqual(HammingDistance('ACGTACGT','TGCATGCA'),8)
        self.assertEqual(HammingDistance('GATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACT'
                                        ,'AATAGCAGCTTCTCAACTGGTTACCTCGTATGAGTAAATTAGGTCATTATTGACTCAGGTCACTAACGTCT'
                                        ),15)
        self.assertEqual(HammingDistance('AGAAACAGACCGCTATGTTCAACGATTTGTTTTATCTCGTCACCGGGATATTGCGGCCACTCATCGGTCAGTTGATTACGCAGGGCGTAAATCGCCAGAATCAGGCTG'
                                        ,'AGAAACCCACCGCTAAAAACAACGATTTGCGTAGTCAGGTCACCGGGATATTGCGGCCACTAAGGCCTTGGATGATTACGCAGAACGTATTGACCCAGAATCAGGCTC'
                                        ),28)

    def test_MinimumSkew(self):
        self.assertEqual(MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'), [11, 24])
        self.assertEqual(MinimumSkew('ACCG'), [3])
        self.assertEqual(MinimumSkew('ACCC'), [4])
        self.assertEqual(MinimumSkew('CCGGGT'), [2])
        self.assertEqual(MinimumSkew('CCGGCCGG'), [2, 6])

    def test_Skew(self):
        self.assertEqual(Skew('CATGGGCATCGGCCATACGCC'), [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2])
        self.assertEqual(Skew('GAGCCACCGCGATA'), [0, 1, 1, 2, 1, 0, 0, -1, -2, -1, -2, -1, -1, -1, -1])

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
        self.assertEqual(set(FasterFrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))
        self.assertEqual(FasterFrequentWords('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC'
        , 12), ['CGAGGCGACTCG'])
        self.assertEqual(set(FasterFrequentWords('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC'
        , 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))        

    def test_FrequentWords(self):
        self.assertEqual(set(FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))
        self.assertEqual(FrequentWords('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC'
        , 12), ['CGAGGCGACTCG'])
        self.assertEqual(set(FrequentWords('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC'
        , 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))  
    
    def test_FindingFrequentWordsBySorting(self):
        self.assertEqual(set(FindingFrequentWordsBySorting('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)), set(['CATG', 'GCAT']))
        self.assertEqual(FindingFrequentWordsBySorting('GGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCTATCGTTCGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTAGTGGGAACGAGGCGACTCGCTAGTATGTGGGAACGGGCAGTAGTGGGAACGTGGGAACTATCGTTCGTGGGAACGTGGGAACGTGGGAACGTGGGAACTATCGTTCTATCGTTCGAGGCGACTCGTGGGAACTATCGTTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTAGCTAGTATGAGGCGACTCGAGGCGACTCTATCGTTCGGGCAGTAGGGCAGTATATCGTTCGCTAGTATGAGGCGACTCGAGGCGACTCGGGCAGTATATCGTTCGGGCAGTAGGGCAGTATATCGTTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGGGCAGTAGAGGCGACTCGAGGCGACTCGCTAGTATGTGGGAACTATCGTTCGTGGGAACGTGGGAACGAGGCGACTCGCTAGTATGCTAGTATGCTAGTATGTGGGAACGCTAGTATGGGCAGTAGCTAGTATTATCGTTCGCTAGTATTATCGTTCGGGCAGTATATCGTTCTATCGTTCGGGCAGTAGGGCAGTAGAGGCGACTCTATCGTTCGAGGCGACTCGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGAGGCGACTCGTGGGAACGTGGGAACGAGGCGACTCGAGGCGACTCGGGCAGTAGTGGGAACGGGCAGTATATCGTTCGAGGCGACTCGTGGGAACGCTAGTATTATCGTTCGAGGCGACTCGTGGGAACGCTAGTATGCTAGTATGAGGCGACTCGCTAGTATGGGCAGTAGGGCAGTAGAGGCGACTC'
        , 12), ['CGAGGCGACTCG'])
        self.assertEqual(set(FindingFrequentWordsBySorting('CTCCTCGCATAAAGTCATAATCGGACCGCTAATAAGGTCGGACCGCTAATAAGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGTAATAAGGCCTGTTGGCCTGTTGGTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCTCCTCGCATAAAGTCATAAAAAGTCATAATCGGACCGCCTCCTCGCATAAAGTCATAACCTGTTGGTCGGACCGCCCTGTTGGCTCCTCGCATTAATAAGGCCTGTTGGCTCCTCGCATCCTGTTGGTCGGACCGCTAATAAGGTAATAAGGCCTGTTGGCCTGTTGGTAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATTCGGACCGCCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTCGGACCGCTAATAAGGCCTGTTGGTCGGACCGCTCGGACCGCCCTGTTGGCCTGTTGGTAATAAGGTCGGACCGCCTCCTCGCATTCGGACCGCTCGGACCGCCTCCTCGCATTCGGACCGCAAAGTCATAATAATAAGGCCTGTTGGCTCCTCGCATTAATAAGGTAATAAGGCTCCTCGCATAAAGTCATAACTCCTCGCATAAAGTCATAATCGGACCGCCCTGTTGGTAATAAGGTAATAAGGAAAGTCATAACCTGTTGGCTCCTCGCATTAATAAGGAAAGTCATAACTCCTCGCATAAAGTCATAATAATAAGGTAATAAGGTCGGACCGCAAAGTCATAACTCCTCGCATCTCCTCGCATCCTGTTGGCCTGTTGGTCGGACCGCCTCCTCGCATCCTGTTGGCCTGTTGGTAATAAGGCTCCTCGCATCCTGTTGGCCTGTTGGAAAGTCATAATCGGACCGC'
        , 14)), set(['GTTGGTCGGACCGC', 'TGTTGGTCGGACCG', 'CTGTTGGTCGGACC', 'CCTGTTGGTCGGAC']))    
        

if __name__ == '__main__':
    unittest.main()
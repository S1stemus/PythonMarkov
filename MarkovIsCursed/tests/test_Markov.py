import unittest
import MarkovIsCursed.MarkovLibrary as markov
import array as arr

class MarkovTestCase(unittest.TestCase):
    def setUp(self):
        self.input = "abcd"
    def test_1 (self):
        rules = "ab-bd;dc-aa"
        result = ["abcd", "bdcd","baad"]
        self.assertEqual(markov.start(rules, self.input), result)  # add assertion here
    def test_2 (self):
        rules = "ab-bd;d-aa"
        result = ["abcd", "bdcd","baacd","baacaa"]
        self.assertEqual(markov.start(rules, self.input), result)
    def test_3 (self):
        rules = "m-p"
        result = ["abcd"]
        self.assertEqual(markov.start(rules, self.input), result)
    def test_1_input (self):
        rules = "ab+bd;dc-aa"
        self.assertEqual(markov.check_rules(rules), False)
    def test_2_input (self):
        input="abcd;ab"
        self.assertEqual(markov.check_word(input), False)

if __name__ == '__main__':
    unittest.main()

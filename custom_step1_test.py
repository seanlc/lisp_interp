# GENERATED by make_pyunitt.py with step1_read_print.mal as input

import unittest
import reader

class REPLTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        assert(reader.apply_seqs("test string") == "test string")

    def test1(self):
        res = reader.apply_seqs("test\\\"string")
        exp = "test\"string"
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

    def test2(self):
        res = reader.apply_seqs("\\\"")
        exp = "\""
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

    def test3(self):
        res = reader.apply_seqs("test\\nstring")
        exp = "test\nstring"
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

    def test4(self):
        res = reader.apply_seqs("\\n")
        exp = "\n"
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

    def test5(self):
        res = reader.apply_seqs("\\\\")
        exp = "\\"
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

    def test6(self):
        res = reader.apply_seqs("test\\\\string")
        exp = "test\\string"
        assert(res == exp), \
            "expected: {} actual: {}".format(exp, res)

if __name__ == "__main__":
    unittest.main()

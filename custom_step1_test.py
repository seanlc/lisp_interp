import unittest
import reader
import printer

err_str = "expected: {} actual: {}"

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
            err_str.format(exp, res)

    def test2(self):
        res = reader.apply_seqs("\\\"")
        exp = "\""
        assert(res == exp), \
            err_str.format(exp, res)

    def test3(self):
        res = reader.apply_seqs("test\\nstring")
        exp = "test\nstring"
        assert(res == exp), \
            err_str.format(exp, res)

    def test4(self):
        res = reader.apply_seqs("\\n")
        exp = "\n"
        assert(res == exp), \
            err_str.format(exp, res)

    def test5(self):
        res = reader.apply_seqs("\\\\")
        exp = "\\"
        assert(res == exp), \
            err_str.format(exp, res)

    def test6(self):
        res = reader.apply_seqs("test\\\\string")
        exp = "test\\string"
        assert(res == exp), \
            err_str.format(exp, res)

    def test7(self):
        res = printer.pr_str("\"", True)
        exp = "\\\""
        assert(res == exp), \
            err_str.format(exp, res)

    def test8(self):
        res = printer.pr_str("test\"string", True)
        exp = "test\\\"string"
        assert(res == exp), \
            err_str.format(exp, res)

    def test9(self):
        res = printer.pr_str("\n", True)
        exp = "\\n"
        assert(res == exp), \
            err_str.format(exp, res)

    def test10(self):
        res = printer.pr_str("test\nstring", True)
        exp = "test\\nstring"
        assert(res == exp), \
            err_str.format(exp, res)

    def test11(self):
        res = printer.pr_str("test\\string", True)
        exp = "test\\\\string"
        assert(res == exp), \
            err_str.format(exp, res)

    def test12(self):
        res = printer.pr_str("\\", True)
        exp = "\\\\"
        assert(res == exp), \
            err_str.format(exp, res)

if __name__ == "__main__":
    unittest.main()

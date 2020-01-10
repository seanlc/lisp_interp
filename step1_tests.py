import unittest
import repl, printer

class ReadTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        assert(repl.repl_read("(1 2 3)") == [1, 2, 3])

    def testB(self):
        assert(repl.repl_read("123") == 123)

    def testC(self):
        assert(repl.repl_read("123 ") == 123)

    def testD(self):
        assert(repl.repl_read("abc") == "abc")

    def testE(self):
        assert(repl.repl_read("abc ") == "abc")

    def testF(self):
        assert(repl.repl_read("abc ") == "abc")

    def testG(self):
        assert(repl.repl_read("(123 456)") == [123, 456])

    def testH(self):
        assert(repl.repl_read("( 123 456 789 )") == [123, 456, 789])

    def testI(self):
        assert(repl.repl_read("( + 2 (* 3 4) )") == ["+", 2, [ "*", 3, 4]])

class PrintTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        assert(printer.pr_str([1, 2, 3]) == "(1 2 3)")

    def testB(self):
        assert(printer.pr_str(123) == "123")

    def testC(self):
        assert(printer.pr_str("abc") == "abc")

    def testD(self):
        assert(printer.pr_str([123, 456]) == "(123 456)")

    def testE(self):
        assert(printer.pr_str([123, 456, 789]) == "(123 456 789)")

    def testF(self):
        assert(printer.pr_str(["+", 2, [ "*", 3, 4]]) == "(+ 2 (* 3 4))")

if __name__ == "__main__":
    unittest.main()

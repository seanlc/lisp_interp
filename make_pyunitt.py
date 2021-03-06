import sys

if len(sys.argv) < 2:
    print("usage: python3 make_pyunitt.py <test_name>")
    print("no filename specified")
    sys.exit()

def write_with_indent(fp, write_str, indent):
    ind = (indent * 4) * " "
    fp.write("{}{}\n".format(ind, write_str))

with open("tests/{}".format(sys.argv[1])) as tf:
    read_data = tf.read()

line_list = read_data.split("\n")

# indicates whether optional and deferrable test cases should be included
optional = False
deferrable = True
test_inputs = []
test_outputs = []

# total number of tests that should be written
test_read = 58

# loop through all lines in mal test file and extract expected
# inputs and outputs of test cases
# Uses status of optional and deferrable vars to make descision
# on whether these test cases should be included
for ln in line_list:
    ln_len = len(ln)
    if ln_len == 0:
        # blank lines
        continue
    elif ln_len == 1:
        # one character inputs
        test_inputs.append(ln)
    else:
        if ln[:2] == ";;":
            # comments
            continue

        if ln[:2] == ";>":
            # directives
            if "deferrable" in ln and not deferrable:
                break
            elif "optional" in ln and not optional:
                break

        else:
            if ln[0] == ";":
                test_outputs.append(ln[3:])
            else:
                test_inputs.append(ln)
                pass

    if len(test_inputs) == test_read and len(test_outputs) == test_read:
        break

print("test inputs: ")
print(test_inputs)
print("test outputs: ")
print(test_outputs)

num_inputs = len(test_inputs)
num_outputs = len(test_outputs)

if num_inputs != num_outputs:
    raise RuntimeError("num_inputs: {} != num_outputs: {}".format(num_inputs, num_outputs))

# write PyUnit test file with inputs and outputs
mods_to_import = ["unittest", "repl", "printer"]

newFileName = sys.argv[1].replace(".mal", "") + ".py"
print("creating PyUnit test fixture: {}".format(newFileName))

with open(newFileName, "w") as pf:
    write_with_indent(pf, "# GENERATED by make_pyunitt.py with {} as input".format(sys.argv[1]), 0)
    write_with_indent(pf, "", 0)

    # imports
    for mod in mods_to_import:
        write_with_indent(pf, "import {}".format(mod), 0)
    write_with_indent(pf, "", 0)

    write_with_indent(pf, "err_str = \"expected: {} actual: {}\"", 0)
    write_with_indent(pf, "", 0)

    # testClass
    write_with_indent(pf,"class REPLTest(unittest.TestCase):", 0)

    # setUp
    write_with_indent(pf, "def setUp(self):", 1)
    write_with_indent(pf, "pass", 2)
    write_with_indent(pf, "", 0)

    # tearDown
    write_with_indent(pf, "def tearDown(self):", 1)
    write_with_indent(pf, "pass", 2)
    write_with_indent(pf, "", 0)

    # write tests
    testNumber = 0
    for inp, outp in zip(test_inputs, test_outputs):
        write_with_indent(pf, "def test{}(self):".format(testNumber), 1)

        # this block looks for backslashes and double quotes within the test
        # inputs and outputs
        # when found, it prepends a backslashto indicate literal interpretatopm
        puts = [inp, outp]
        for i, put in enumerate(puts):
            n = 0
            put_len = len(put)
            while n < put_len:
                if put[n] == "\"" or put[n] == "\\":
                    put = put[:n] + "\\" + put[n:]
                    n += 1
                    put_len += 1
                n += 1
            if i == 0:
                inp = put
            elif i == 1:
                outp = put

        #if outp == "+":
        #change this back to the above for step2 tests to pass
        if False:
            write_with_indent(pf, "try:", 2)
            write_with_indent(pf, 
                "self.assertRaises(RuntimeError, repl.repl(\"{}\"))".format(inp, outp), 3)
            write_with_indent(pf, "except RuntimeError:", 2)
            write_with_indent(pf, "pass", 3)
        else:
            write_with_indent(pf, "exp = \"{}\"".format(outp), 2)
            write_with_indent(pf, "res = repl.repl(\"{}\")".format(inp), 2)
            write_with_indent(pf, "assert(res == exp), \\".format(inp, outp), 2)
            write_with_indent(pf, "err_str.format(exp, res)", 3)
        write_with_indent(pf, "", 0)
        testNumber += 1

    # call all tests if this file is invoked directly
    write_with_indent(pf, "if __name__ == \"__main__\":", 0)
    write_with_indent(pf, "unittest.main()", 1)

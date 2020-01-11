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

optional = False
deferrable = False
test_inputs = []
test_outputs = []

test_read = float("inf")

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
    # imports
    for mod in mods_to_import:
        write_with_indent(pf, "import {}".format(mod), 0)
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
        write_with_indent(pf, "assert(repl.test_repl(\"{}\") == \"{}\")".format(inp, outp), 2)
        write_with_indent(pf, "", 0)
        testNumber += 1

    # call all tests if this file is invoked directly
    write_with_indent(pf, "if __name__ == \"__main__\":", 0)
    write_with_indent(pf, "unittest.main()", 1)

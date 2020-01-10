import sys

if len(sys.argv) < 2:
    print("usage: python3 make_pyunitt.py tests/<test_name>")
    print("no filename specified")
    sys.exit()

with open(sys.argv[1]) as tf:
    read_data = tf.read()

line_list = read_data.split("\n")

optional = False
deferrable = False
test_inputs = []
test_outputs = []

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

print("test inputs: ")
print(test_inputs)
print("test outputs: ")
print(test_outputs)

# TODO: write PyUnit test file with inputs and outputs

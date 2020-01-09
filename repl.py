def repl_read(line):
    return line

def repl_eval(expr):
    return expr

def repl_print(line):
    return line

def rep(line):
    return repl_print(repl_eval(repl_read(line)))

# start main code
while True:
    try:
        ln = input("user>")
    except EOFError:
        break;

    print(rep(ln))



import reader
import printer

def repl_read(line):
    return reader.read_str(line)

def repl_eval(expr):
    return expr

def repl_print(line):
    return printer.pr_str(line)

def rep(line):
    return repl_print(repl_eval(repl_read(line)))

# start main code
if __name__ == "__main__":
    while True:
        try:
            ln = input("user>")
        except EOFError:
            break;
    
        print(rep(ln))

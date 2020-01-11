import reader
import printer

loop_env = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: int(x / y)
}

def eval_ast(ast, env):
#   import pdb; pdb.set_trace()
   val = None
   if isinstance(ast, list):
       val = []
       for ele in ast:
           val.append(repl_eval(ele, env))
   else:
       sym = loop_env.get(ast)
       if sym is not None:
           val = sym
       else:
           val = ast

   return val

def repl_read(line):
    return reader.read_str(line)

def repl_eval(ast, loop_env):
#    import pdb; pdb.set_trace()
    if isinstance(ast, list):
      # do list stuff
      if len(ast) == 0:
          return ast
      else:
          ast = eval_ast(ast, loop_env)
          if callable(ast[0]):
              # use first param as function name, rest of params as args
              ast = ast[0](*ast[1:])
          else:
              raise RuntimeError("{} is not a function".format(ast[0]))
    else:
        ast = eval_ast(ast, loop_env)
    return ast

def repl_print(line):
    return printer.pr_str(line)

def rep(line):
    return repl_print(repl_eval(repl_read(line), loop_env))

def test_repl(line):
    return rep(line)

# start main code
if __name__ == "__main__":
    while True:
        try:
            ln = input("user>")
        except EOFError:
            break;
    
        print(rep(ln))

import re

class Reader:
    def __init__(self, toks):
        self.tokens = toks
        self.pos = 0
        self.num_toks = len(toks)

    def _get_curTok(self):
        if self.pos == self.num_toks:
            curTok = None
        else:
            curTok = self.tokens[self.pos]

        return curTok

    def next(self):
        curTok = self._get_curTok()
        self.pos += 1

        return curTok

    def peek(self):
        return self._get_curTok()

def apply_seqs(line):
    # apply escape sequences
    num_chars = len(line)
    del_chars = 0

    for i in range(num_chars):
        if i == num_chars-1 or i + del_chars == num_chars-1:
            break

        ch0 = line[i]
        ch1 = line[i+1]

        # /" -> "
        if ch0 == "\\" and ch1 == "\"":
            line = line[:i] + line[i+1:]
            del_chars += 1

        # \n -> (newline)
        elif ch0 == "\\" and ch1 == "n":
            line = line[:i] + "\n" +line[i+2:]
            del_chars += 1

        # \\ -> \
        elif ch0 == "\\" and ch1 == "\\":
            line = line[:i] + line[i+1:]
            del_chars += 1

    return line

def read_str(input_str: str):
    toks = tokenize(input_str)
    rdr = Reader(toks)
    form = read_form(rdr)

    # TODO: apply escape sequences and return new rep
    #rep = apply_seqs(form)
    #return rep

    return form

def tokenize(raw_str: str):
    toks = re.findall(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)""",
                      raw_str)

    if toks[-1] == "":
        tokens = toks[:-1]
    else:
        tokens = toks

    return tokens

def read_form(rdr):
    tok = rdr.peek()
    if tok == "(":
        form = read_list(rdr)
    else:
        form = read_atom(rdr.next())

    return form

def read_list(rdr):
    mal_types = []
    rdr.next()
    while True:
        tok = read_form(rdr)
        if tok is ")":
            break
        elif tok is None:
            raise EOFError("missing closing )")
        mal_types.append(tok)
            
    return mal_types

def read_atom(tok):
    if isNum(tok):
        atom = int(tok)
    else:
        atom = tok

    return atom

def isNum(sym):
    try:
        float(sym)
        sym_is_num = True
    except (ValueError, TypeError) as e:
        sym_is_num = False

    return sym_is_num

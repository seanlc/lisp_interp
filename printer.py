def pr_str(mal, print_readably=False):
    mal_str = ""

    # if mal is a list, recursively unpack it into str representation
    # if mal is not a list, return str representation
    if isinstance(mal, list):
        mal_str += "("
        for i, ele in enumerate(mal):
            if i != 0:
                mal_str += " "
            mal_str += pr_str(ele)
        mal_str += ")"

    else:
        mal_str = str(mal)

        if print_readably:
            # look for special chars
            for i, ch in enumerate(mal):

                # rewrite special chars as escape sequences
                if ch == "\"":
                    mal_str = mal_str[:i] + "\\" + mal_str[i:]

                if ch == "\n":
                    mal_str = mal_str[:i] + "\\n" + mal_str[i+1:]

                if ch == "\\":
                    mal_str = mal_str[:i] + "\\" + mal_str[i:]


    return mal_str

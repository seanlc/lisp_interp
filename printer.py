def check_for_escs(mal_str, ch, i, m_len):
    if ch == "\"" and i != 0 and i != m_len-1 or \
       ch == "\\":
        mal_str = mal_str[:i] + "\\" + mal_str[i:]
    elif ch == "\n":
        mal_str = mal_str[:i] + "\\n" + mal_str[i+1:]
    else:
        return mal_str, i, m_len

    i += 1
    m_len += 1
    return mal_str, i, m_len

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
            i = 0
            m_len = len(mal_str)

            while i < m_len:
                # rewrite special chars as escape sequences
                ch = mal_str[i]
                (mal_str, i, m_len) = check_for_escs(mal_str, ch, i, m_len)
                i += 1


    return mal_str

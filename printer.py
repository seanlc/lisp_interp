def pr_str(mal):
    mal_str = ""

    if isinstance(mal, list):
        mal_str += "("
        for i, ele in enumerate(mal):
            if i != 0:
                mal_str += " "
            mal_str += pr_str(ele)
        mal_str += ")"
        return mal_str
    else:
        return str(mal)

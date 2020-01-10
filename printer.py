def pr_str(mal):
    mal_str = ""

    if mal is list:
        mal_str += "( "
        for ele in mal:
            print_str(ele)
        mal_str += ")"
        return mal_str
    else:
        return str(mal)

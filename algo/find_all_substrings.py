def substrings(string):
    res = []
    # for each letter
    for i in range(len(string)):
        # first append that letter
        res.append(string[i])
        # iterate over the left over string from that letter
        for j in range(i + 1, len(string)):
            # appned a new string from the last string in res
            res.append(res[-1] + string[j])
    return res

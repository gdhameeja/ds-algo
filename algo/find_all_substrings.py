def substrings(self, string):
    res = []
    for i, each in enumerate(string):
        master = ""
        for j in range(i, (len(string))):
            master += string[j]
            res.append(master)
    return res

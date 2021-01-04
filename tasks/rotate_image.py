def rotate(s):
    for o in range(len(s) // 2):
        for i in range(o, len(s) - o - 1):
            s[i][-o-1], s[-o-1][-1-i],  s[-1-i][o],     s[o][i] =\
            s[o][i],    s[i][-o-1],     s[-o-1][-1-i],  s[-1-i][o]

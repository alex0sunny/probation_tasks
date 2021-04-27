def timeToFlowerTree(father, time):
    tree = {0: []}
    for i, f in enumerate(father):
        if i:
            if f not in tree:
                tree[f] = []
            tree[f].append(i)
    stack = [[0, 0]]
    res = 0
    while stack:
        i, t = stack.pop()
        if i not in tree:
            res = max(t, res)
        else:
            for j in tree[i]:
                stack.append([j, t + time[j]])
    return res

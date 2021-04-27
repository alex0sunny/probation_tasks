def timeToFlowerTree(father, time):
    tree = {0: []}
    for i, f in enumerate(father):
        if i:
            if f not in tree:
                tree[f] = []
            tree[f].append(i)
    nodes = [[0, 0]]
    res = 0
    while nodes:
        i, t = nodes.pop()
        if i not in tree:
            res = max(t, res)
        else:
            for j in tree[i]:
                nodes.append([j, t + time[j]])
    return res

# 1323 · Fetch supplies
# Algorithms
# Medium
# Accepted Rate53%
# Description

# There are many military camps on a two-dimensional map. The coordinates of each
# military camp are (x, y). There is a road parallel to the y axis and of
# unlimited length. When the supply vehicle passes this road, the materials
# of each military camp will be placed The roadside closest to their barracks
# (The location of this road makes the distance and minimum distance from all 
# military camps to the road),
# What is the shortest distance from the military camps to the road

#     −109≤x,y≤109-10^9 \leq x,y \leq 10^9−109≤x,y≤109
#     coordinates.size()≤50000coordinates.size() \leq 50000coordinates.size()≤50000

# Example

# imput:

# [[-10,0],[0,0],[10,0]]

# output:20

# Explanation:Assuming the road is at x = 0, the shortest path sum is 10 + 0 + 10 = 20


def median(lst):
    lst.sort()
    n = len(lst)
    r = n // 2
    l = r - 1
    if n % 2:
        return lst[r]
    return (lst[l] + lst[r]) / 2


def fetch_supplies(coordinates):
    med = median([x for x, _ in coordinates])
    dist = sum([abs(x - med) for x, _ in coordinates])
    return int(dist)

# Description

# you have a list intervals of current meetings, and some meeting rooms with start and end timestamp.When a stream of new meeting ask coming in, judge one by one whether they can be placed in the current meeting list without overlapping..A meeting room can only hold one meeting at a time. Each inquiry is independent.

# Note
# Ensure that Intervals can be arranged in rooms meeting rooms
# Ensure that the end time of any meeting is not greater than 50000
# |Intervals|<=50000
# |ask|<=50000
# rooms<=20
# Example

# Example 1:

# Input:
# Intervals:[[1,2],[4,5],[8,10]], rooms = 1, ask: [[2,3],[3,4]]
# Output: 
# [true,true]
# Explanation:
# For the ask of [2,3], we can arrange a meeting room room0.
# The following is the meeting list of room0:
# [[1,2], [2,3], [4,5], [8,10]]
# For the ask of [3,4], we can arrange a meeting room room0.
# The following is the meeting list of room0:
# [[1,2], [3,4], [4,5], [8,10]]

# Example 2:

# Input:
# [[1,2],[4,5],[8,10]]
# 1
# [[4,5],[5,6]]
# Output:
# [false,true]

def meetingRoomIII(intervals, rooms, ask):
    pts = [0] * 50001
    for s, e in intervals:
        pts[s] += 1
        pts[e] -= 1
    for i in range(1, len(pts)):
        pts[i] += pts[i - 1]
    pts = [1 if pts[i] == rooms else 0 for i in range(len(pts))]
    incs = pts[:]
    for i in range(1, len(incs)):
        incs[i] += incs[i - 1]
    return [not (pts[s] or pts[e - 1] or incs[e - 1] > incs[s - 1])
            for s, e in ask]

# There is a 1 * n chess table, indexed with 0,1,2..n−1, every grid is colored.
# And there is a chess piece on position 0, please calculate the minimum step that you should move it to position n−1.
# Here are 3 ways to move the piece, the piece can't be moved outside of the table:

#     Move the piece from position i to position i+1.
#     Move the piece from position i to position i−1.
#     If the colors on position i and position j are same, you can move the piece directly from position i to position j.

# Example 1

# Input:
# colors = [1, 2, 3, 3, 2, 5]
# Output:
# 3
# Explanation: 
# In the example. you should move the piece 3 times:
# 1. Move from position 0 to position 1.
# 2. Because of the same color in position 1 and position 4, move from position 1 to position 4,
# 3. Move from position 4 to position 5.

def minimumStep(colors):
    end = len(colors) - 1
    cur_pts = {0}
    pts_dic = {}
    colors_dic = {}
    for pt, color in enumerate(colors):
        if color not in colors_dic:
            colors_dic[color] = []
        colors_dic[color].append(pt)
        pts_dic[pt] = color
    r = 1
    end_color = colors[-1]
    while True:
        next_pts = set()
        for pt in cur_pts:
            if pt not in pts_dic:
                continue
            color = pts_dic[pt]
            if pt + 1 == end or end_color == color:
                return r
            del pts_dic[pt]
            if (pt + 1) in pts_dic:
                next_pts.add(pt + 1)
            if (pt - 1) in pts_dic:
                next_pts.add(pt - 1)
            color_pts = colors_dic[color]
            color_pts.remove(pt)
            next_pts.update(color_pts)
        cur_pts = next_pts.copy()
        r += 1

# Description

# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

# For each integer in this list:

# 1.The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# 2.The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
# 3.The units digit represents the value V of this node, 0 <= V <= 9.

# Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.
# Example

# Example 1:

# Input: [113, 215, 221]
# Output: 12
# Explanation: 
# The tree that the list represents is:
#     3
#    / \
#   5   1

# The path sum is (3 + 5) + (3 + 1) = 12.

# Example 2:

# Input: [113, 221]
# Output: 4
# Explanation: 
# The tree that the list represents is: 
#     3
#      \
#       1

# The path sum is (3 + 1) = 4.

def pathSumIV(nums):
    nums = list(sorted(nums))
    root = [nums.pop(0) % 10, None, None]
    nodes = [root]
    par_nodes = []
    level = 1
    while nums:
        num = nums.pop(0)
        cur_level = num // 100
        if cur_level != level:
            level = cur_level
            par_nodes = nodes[:]
            nodes = [None] * 2 ** (level - 1)
        pos = (num - cur_level * 100) // 10
        val = num % 10
        node = [val, None, None]
        par_ind = (pos - 1) // 2
        left = pos % 2
        nodes[pos - 1] = node
        par_node = par_nodes[par_ind]
        if left:
            par_node[1] = node
        else:
            par_node[2] = node

    def sum_path(node, par_sum):
        val, left, right = node
        res = 0
        cur_sum = par_sum + val
        if not left and not right:
            return cur_sum
        if left:
            res += sum_path(left, cur_sum)
        if right:
            res += sum_path(right, cur_sum)
        return res

    return sum_path(root, 0)


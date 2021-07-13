# 1907 · Array Game
# Algorithms
# Medium
# Accepted Rate42%

# Description

# Given an array of integers, determine the minimum number of moves 
# to make all elements equals. Each move consists of choosing all
# but 1 element and incrementing their values by 1.

# Example

# Input: 
# [3, 4, 6, 6, 3]
# Output: 
# 7
# Explanation: 
# [3, 4, 6, 6, 3] -> [4, 5, 7, 6, 4] -> [5, 6, 7, 7, 5] -> [6, 7, 8, 7, 6] 
# -> [7, 8, 8, 8, 7] -> [8, 9, 9, 8, 8] -> [9, 9, 10, 9, 9]
# -> [10, 10, 10, 10, 10]

# Tags
# Simulation

# def array_game(arr):
#     arr.sort(reverse=True)
#     r = 0
#     p = arr[0]
#     for i in range(1, len(arr)):
#         e = arr[i]
#         if p != e:
#             r += i * (p - e)
#         p = e
#     return r


# def array_game(arr):
#     return sum(arr) - min(arr) * len(arr)


def array_game(nums):
    mi = min(nums)
    nums = [num - mi for num in nums]
    return sum(nums)


assert(array_game([3, 4, 6, 6, 3]) == 7)



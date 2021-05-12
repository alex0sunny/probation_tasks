# 368. Largest Divisible Subset
# Medium

# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

#     answer[i] % answer[j] == 0, or
#     answer[j] % answer[i] == 0

# If there are multiple solutions, return any of them.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.

# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]

def largestDivisibleSubset(nums):
    nums.sort()
    max_counts = [1] * len(nums)
    prevs = [-1] * len(nums)
    i_max = max_count = 0
    for i in range(1, len(nums)):
        num = nums[i]
        for j in range(i):
            if num % nums[j] == 0 and max_counts[j] + 1 > max_counts[i]:
                max_counts[i] = max_counts[j] + 1
                prevs[i] = j
        if max_counts[i] > max_count:
            max_count = max_counts[i]
            i_max = i
    res = [nums[i_max]]
    i = i_max
    while prevs[i] != -1:
        i = prevs[i]
        res.insert(0, nums[i])
    return res

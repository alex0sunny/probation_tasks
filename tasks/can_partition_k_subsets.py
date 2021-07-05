# 698. Partition to K Equal Sum Subsets
# Medium

# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false


def check_partition(nums, cur_sum, k, target_sum, visited):
    if k == 1:
        return True
    if cur_sum == target_sum:
        return check_partition(nums, 0, k - 1, target_sum, visited)
    for i, num in enumerate(nums):
        if visited[i] or num + cur_sum > target_sum:
            continue
        visited[i] = True
        if check_partition(nums, cur_sum + num, k, target_sum, visited):
            return True
        visited[i] = False
    return False


def can_partition(nums, k):
    visited = [False] * len(nums)
    nums.sort(reverse=True)
    nums_sum = sum(nums)
    target_sum = nums_sum // k
    if nums_sum % k or max(nums) > target_sum or len(nums) < k:
        return False
    return check_partition(nums, 0, k, target_sum, visited)


assert(can_partition([4,3,2,3,5,2,1], 4))

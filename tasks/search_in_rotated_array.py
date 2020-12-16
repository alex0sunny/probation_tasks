# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

def search(nums, target):
    ranges = [[0, len(nums) - 1]]
    while ranges != []:
        [start, end] = ranges[0]
        ranges = ranges[1:]
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        if start >= end:
            continue
        middle = (start + end) // 2
        new_ranges = [[start + 1, middle], [middle + 1, end - 1]]
        if nums[start] < target < nums[end]:
            ranges = new_ranges
        elif nums[start] > nums[end]:
            ranges += new_ranges
    return -1


assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search([1], 0) == -1

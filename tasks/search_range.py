#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]

#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]

#Example 3:

#Input: nums = [], target = 0
#Output: [-1,-1]


def searchRange(nums, target):
    s = 0
    e = len(nums) - 1

    while s < e and nums[s] <= target <= nums[e] and nums[s] != nums[e]:
        middle = (s + e) // 2
        if nums[s] < target:
            if nums[middle] < target:
                s = max(s + 1, middle)
            else:
                s += 1
        else:  # nums[e] > target:
            if nums[middle] < target:
                e = middle
            else:
                e -= 1

    if 0 <= e <= len(nums) - 1 and nums[s] == nums[e] == target:
        return [s, e]
    return [-1, -1]

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]

def nextPermutation(nums):
  for i in range(len(nums) - 1, -1, -1):
    if i == 0 or nums[i - 1] < nums[i]:
      break
    for j in range(0, (len(nums) - i) // 2):
      nums[i + j], nums[-j - 1] = nums[-j - 1], nums[i + j]
    if i == 0:
      return
    for j in range(i, len(nums)):
      if nums[j] > nums[i - 1]:
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        return

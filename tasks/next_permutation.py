def nextPermutation(nums):
  for i in range(len(nums)-2, 0, -1):
    if nums[i] < nums[i+1]:
    for j in range(i+1, len(nums)):
      if j == len(nums)-1 or nums[i] > nums[j+1]:
        nums[i], nums[j] = nums[j], nums[i]
        return nums
  for i in range(0, len(nums) // 2):
    nums[i], nums[-1-i] = nums[-1-i], nums[i]
  return nums

def quicksort(nums, start = 0, end = None):

  if end == None:
    end = len(nums) - 1

  if start >= end:
    return

  pivot = nums[end]
  left = start
  right = end
  
  while left < right:

    while nums[left] < pivot:
      left += 1

    while nums[right] > pivot:
      right -= 1

    if left != right:
      nums[left], nums[right] = nums[right], nums[left]

      if nums[left] == nums[right]:
        left += 1

  quicksort(nums, start, left - 1)
  quicksort(nums, left + 1, end)

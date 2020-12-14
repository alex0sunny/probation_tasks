def shellsort(nums):
  step = len(nums) // 2
  while step:
    for e in range(step, len(nums)):
      pivot = nums[e]
      p = e
      while p >= step and nums[p - step] > pivot:
        nums[p] = nums[p - step] 
        p -= step
      nums[p] = pivot
    step //= 2

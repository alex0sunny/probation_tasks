ar = [1, 48, 42, 20, 21, 46, 48, 26, 42, 44]

def f(nums):
#  print(f'ar:{ar}\nnums:{nums}')
  if len(nums) < 3: 
    if len(nums) == 1:
      print(nums[0])
    if len(nums) == 2:
      if nums[1] > nums[0]:
        print(nums[0])
        print(nums[1])
      else:
        print(nums[1])
        print(nums[0])
    return

  i = 0
  j = len(nums) - 1
  pivot = nums[-1]
  while i < j:
    # print(f'i={i} j={j} pivot={pivot}')
    # sleep(.5)
    if nums[i] <= pivot: 
      i += 1
    elif nums[j] > pivot: 
      j -= 1
    else:
      nums[i], nums[j] = nums[j], nums[i]

  f(nums[:i])
  f(nums[i:])

f(ar)

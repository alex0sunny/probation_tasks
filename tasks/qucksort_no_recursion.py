def quicksort(ar, ranges = None): 
  if ranges == None:
    ranges = [[0, len(ar) - 1]]
  while ranges != []:
    [start, end] = ranges[0]
    ranges = ranges[1:]
    if start >= end:
      continue
    pivot = ar[end]
    left = start
    right = end
    while left < right:
      while ar[left] < pivot:
        left += 1
      while ar[right] > pivot:
        right -= 1
      if left < right:
        ar[left], ar[right] = ar[right], ar[left]
        if ar[left] == ar[right]:
          left += 1
    ranges = [[start, left - 1], [left + 1, end]] + ranges

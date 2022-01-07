# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    le = len(nums)
    start = counter = 0
    while counter < le:
        buf = nums[start]
        r = start
        l = (r-k) % le
        while l != start:
            nums[r] = nums[l]
            counter += 1
            r = l
            l = (l-k) % le
        nums[r] = buf
        counter += 1
        start += 1

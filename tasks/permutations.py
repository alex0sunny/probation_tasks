def permute(nums):
    if not nums:
        return [[]]
    out = []
    for v in nums:
        nums_temp = nums[:]
        nums_temp.remove(v)
    for permutation in self.permute(nums_temp):
        out.append([v] + permutation)
    return out

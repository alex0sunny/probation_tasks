def combination_sum(candidates, target):
    nums = list(sorted(candidates))
    res = []

    def f(start, target, path=[]):
        if target == 0:
            res.append(path)
            return
        if target < 0 or start == len(nums):
            return
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                f(i + 1, target - nums[i], path + [nums[i]])

    f(0, target, [])
    return res

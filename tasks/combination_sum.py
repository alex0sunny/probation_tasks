# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

def combination_sum(candidates, target):
    nums = list(sorted(candidates))
    res = []

    def f(start, target, path):
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

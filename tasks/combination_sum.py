# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

def f(nums, target, res, start = 0, path = []):
    if target == 0:
        res.append(path)
    if target > 0:
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                f(nums, target - nums[i], res, i + 1, path + [nums[i]])
    return res
    
def combination_sum(nums, target):
    return f(list(sorted(nums)), target, [])

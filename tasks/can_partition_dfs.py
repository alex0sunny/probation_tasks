# can_partition_k_subsets dfs solution, not effective, yet passes all tests

def dfs(nums, pos, targets, k):
    if pos == len(nums):
        return True
    for i in range(k):
        if targets[i] >= nums[pos]:
            targets[i] -= nums[pos]
            if dfs(nums, pos + 1, targets, k):
                return True
            targets[i] += nums[pos]
    return False


def can_partition(nums, k):
    nums.sort(reverse=True)
    nums_sum = sum(nums)
    target_sum = nums_sum // k
    if nums_sum % k or max(nums) > target_sum or len(nums) < k:
        return False
    targets = [target_sum] * k
    return dfs(nums, 0, targets, k)

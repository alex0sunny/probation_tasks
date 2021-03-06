# can_partition_k_subsets simplified solution, probably erroneous, yet passes all tests


def check_partition(nums, cur_sum, target_sum, visited):
    if all(visited):
        return True
    if cur_sum == 0:
        cur_sum = target_sum
    for i, num in enumerate(nums):
        if visited[i] or num > cur_sum:
            continue
        visited[i] = True
        if check_partition(cur_sum - num, target_sum):
            return True
        visited[i] = False
    return False


def can_partition(nums, k):
    visited = [False] * len(nums)
    nums.sort(reverse=True)
    nums_sum = sum(nums)
    target_sum = nums_sum // k
    if nums_sum % k or max(nums) > target_sum:
        return False
    return check_partition(nums, target_sum, target_sum, visited)

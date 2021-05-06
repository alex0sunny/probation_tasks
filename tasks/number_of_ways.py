# Number of Ways to Stay in the Same Place After Some Steps
# Hard

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7.

def numWays(steps, arrLen):
    dp = [0] * arrLen
    cur_steps = 1
    dp[0] = dp[1] = 1
    while cur_steps < steps:
        dp_next = [0] * arrLen
        for i in range(arrLen):
            dp_next[i] = dp[i]
            if i > 0:
                dp_next[i] += dp[i - 1]
            if i < arrLen - 1:
                dp_next[i] += dp[i + 1]
            if dp[i] == 0:
                break
        dp = dp_next
        cur_steps += 1
    return dp[0] % (10 ** 9 + 7)

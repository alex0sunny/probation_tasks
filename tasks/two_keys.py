# 650. 2 Keys Keyboard
# Medium

# There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

#     Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
#     Paste: You can paste the characters which are copied last time.

# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

# Example 1:

# Input: n = 3
# Output: 3
# Explanation: Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.

# Example 2:

# Input: n = 1
# Output: 0

# def minSteps(n):
#     steps = 0
#     d = 1
#     while d != n:
#         n = n // d
#         d = n
#         for k in range(2, n):
#             if n % k == 0:
#                 d = k
#                 break
#         steps += d
#     return steps

# def minSteps(n):
#     if n < 2:
#         return 0
#     elif n == 2:
#         return 2
#     else:
#         ds = [i for i in range(3, n // 2 + 1) if n % i == 0]
#         if not ds:
#             return n
#         return min([n // d + minSteps(d) for d in ds])

def minSteps(n):
    dp = [0, 0]
    for i in range(2, n+1):
        dp.append(min([dp[j] + i // j for j in range(1, i) if i % j == 0]))
    return dp[n]

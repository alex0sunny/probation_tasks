# 867 · 4 Keys Keyboard
# Medium

# Imagine you have a special keyboard with the following keys:

#     Key 1: (A): Print one 'A' on screen.
#     Key 2: (Ctrl-A): Select the whole screen.
#     Key 3: (Ctrl-C): Copy selection to buffer.
#     Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

#     1 <= N <= 50
#     Answers will be in the range of 32-bit signed integer.

# Example

# Example 1:

# Input: 3
# Output: 3
# Explanation: A, A, A

# Example 2:

# Input: 7
# Output: 9
# Explanation: A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

def maxA(N):
    dp = [i + 1 if i < 6 else 0 for i in range(N)]
    for i in range(6, N):
        dp[i] = max([(i - b - 1) * dp[b] for b in range(i - 2)])
    return dp[-1]

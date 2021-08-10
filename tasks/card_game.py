# 1448 · Card Game
# Algorithms
# Medium
# Accepted Rate35%

# Description

# A card game that gives you the number of cards n，and two non-negative integers: totalProfit, totalCost.
# Then it will give you the profit value of every card a[i] and the cost value of every card b[i].
# It is possible to select any number of cards from these cards, form a scheme.
# Now we want to know how many schemes are satisfied that all selected cards' profit values are greater than 
# totalProfit and the costs are less than totalCost.

#     Since this number may be large, you only need to return the solution number mod 1e9 + 7.
#     0≤n≤1000 \leq n \leq 1000≤n≤100
#     0≤totalProfit≤1000 \leq totalProfit\leq 1000≤totalProfit≤100
#     0≤totalCost≤1000 \leq totalCost \leq 1000≤totalCost≤100
#     0≤a[i]≤1000 \leq a[i] \leq 1000≤a[i]≤100
#     0≤b[i]≤1000 \leq b[i] \leq 1000≤b[i]≤100

# Example

# Example 1:

# Input：n = 2，totalProfit = 3，totalCost = 5，a = [2,3]，b = [2,2] 
# Output：1
# Explanation:
# At this time, there is only one legal scheme, which is to select both cards. At this time, a[1]+a[2] = 5 > totalProfit and b[1] + b[2] < totalCost.

# Example 2:

# Input: n = 3，totalProfit = 5，totalCost = 10，a = [6,7,8]，b = [2,3,5]
# Output: 6
# Explanation:
# Suppose a legal scheme (i,j) indicates that the i-th card and the j-th card are selected.
# The legal solutions at this time are:
# (1),(2),(3),(1,2),(1,3),(2,3)

# Company
# Google

def numOfPlan(n, totalProfit, totalCost, a, b):
  dp = [[0] * totalCost for _ in range(totalProfit + 2)]
  dp[0][0] = 1
  for k in range(n):
    for i in range(totalCost, -1, -1):
      cost = i + b[k]
      if cost < totalCost:
        for j in range(totalProfit + 1, -1, -1):
          profit = j + a[k]
          if profit > totalProfit + 1:
            profit = totalProfit + 1
            dp[profit][cost] += dp[j][i]
  return sum(dp[-1]) % (10 ** 9 + 7)

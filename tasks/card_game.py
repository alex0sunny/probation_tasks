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

MOD = 10 ** 9 + 7


def num_of_plans(n, tota_profit, total_cost, profits, costs):
    counters = [[0] * total_cost for _ in range(tota_profit + 2)]
    counters[0][0] = 1
    for card_i in range(n):
        for cur_cost in range(total_cost, -1, -1):
            cost = cur_cost + costs[card_i]
            if cost < total_cost:
                for cur_profit in range(tota_profit + 1, -1, -1):
                    profit = cur_profit + profits[card_i]
                    if profit > tota_profit + 1:
                        profit = tota_profit + 1
                        counters[profit][cost] = (counters[profit][cost] +
                                                  counters[cur_profit][cur_cost]) % MOD
    return sum(counters[-1]) % MOD


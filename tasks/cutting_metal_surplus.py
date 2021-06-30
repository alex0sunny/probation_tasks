# Mr. Octopus has recently shut down hisfactory and want to sell off his metal rods to a local businessman.
# In order to maximize profit, he should sellthe metal of same size and shape. If he sells metal rods of length ,he receives N x L xmetal_price. The remaining smallermetal rods will be thrown away. To cut the metal rods, he needs to pay cost_per_cut for every cut.
# What is the maximum amount of money Mr.Octopus can make?
# Input Format
# First line of input contains cost_per_cut
# Second line of input contains metal_price
# Third contains rod lenghts.
# Output Format
# Print the result corresponding to the testcase.
# Constraints
# 1 <= metal_price, cost_per_cut <= 1000
# 1 <= L (number of rods) <= 50
# Each element of lenghts will lie in range [1, 10000].
# Sample Input#00
# 1
# 10
# [26, 103, 59]
# Sample Output#00
# 1770
# Explanation Here cuts are pretty cheap. So we can make largenumber of cuts to reduce the amount of wood wasted. Most optimal lengths ofrods will be . So we will cut pieces of length from rod,and throw peice of length from it. Similarly we will cut piecesof length from rod and throw away a piece of length .From rod, we will cut pieces of length andthrow a piece of length . So in total we have pieces of length andwe have made cuts also. So total profit is
# Sample Input#01
# 100
# 10
# [26, 103, 59]
# Sample Output#01
# 1230

def maxProfit(costPerCut, salePrice, lengths):
    price = 0
    for cur_len in range(1, max(lenghts) + 1):
        n_of_rods = sum([l // cur_len for l in lengths])
        n_of_cuts = sum([max(0, l // cur_len - bool(l % cur_len == 0)) for l in lengths])
        price = max(price, n_of_rods * cur_len * salePrice - n_of_cuts * costPerCut)
        cur_len -= 1
    return max(price, 0)

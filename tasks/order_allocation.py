# Order allocation
# Algorithms
# Medium
# Accepted Rate59%

# Description

# In taxi dispatching scenario, it is assumed that there are N orders 
# to be assigned to N drivers. Before each order is matched with drivers,
# the candidate drivers will be scored, and the scoring results are saved 
# in an N*N matrix score, where score[i][j] represents the score value
# of driver j matching of order i.
# Assume that each order can only be assigned to one driver, and that
# the driver can only be assigned to one order. The final dispatch result
# is obtained so that the matching order and driver's points add up to
# the maximum and all orders are allocated.

# The problem guarantees that the maximum score of each data is unique

# Example

# Example 1

# Input：

# [[1,2,4],[7,11,16],[37,29,22]]

# Output：

# [1,2,0]

# Explanation：

# orders[0] is given to drivers[1], make score[0][1] = 2 points,

# orders[1] is given to drivers[2], make score[1][2] = 16 points,

# orders[2] is given to drivers[0], make score[2][0] = 37 points,

# so we get 2 + 16 + 37 = 55 points totally.


def allocate_orders(score):
    n = len(score)
    paths = [[j] for j in range(n)]
    for _ in range(1, n):
        nx_paths = []
        for path in paths:
            for j in range(n):
                if j not in path:
                    nx_paths.append(path + [j])
        paths = nx_paths[:]
    r = 0
    res_path = []
    for path in paths:
        path_sum = sum([score[i][j] for i, j in enumerate(path)])
        if path_sum > r:
            r = path_sum
            res_path = path
    return res_path


# effective solution
class Solution:

    res_path = []
    res_sum = 0
    score = []
    n = 0

    def allocate(self, i, cur_sum, path, visited):
        if i == self.n:
            if cur_sum > self.res_sum:
                self.res_sum = cur_sum
                self.res_path = path[:]
            return cur_sum
        max_sum = cur_sum
        line = self.score[i]
        for j in range(self.n):
            if not visited[j]:
                visited[j] = True
                path[i] = j
                nx_sum = self.allocate(i+1, cur_sum+line[j], path, visited)
                if nx_sum > max_sum:
                    max_sum = nx_sum
                visited[j] = False
        return max_sum


    """
    @param score: When the j-th driver gets the i-th order, we can get score[i][j] points.
    @return: return an array that means the array[i]-th driver gets the i-th order.
    """
    def orderAllocation(self, score):
        self.score = score
        self.n = len(score)
        visited = [False] * self.n
        path = [0] * self.n
        self.allocate(0, 0, path, visited)
        return self.res_path


solution = Solution()
assert(solution.orderAllocation([[1,2,4],[7,11,16],[37,29,22]]) == [1,2,0])


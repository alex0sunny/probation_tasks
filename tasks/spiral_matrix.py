# 54. Spiral Matrix
# Medium

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:

# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:

# Input: matrix = [[1, 2, 3, 4],
#                  [5, 6, 7, 8],
#                  [9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
  res = matrix.pop(0)
  while matrix:
    matrix = [[matrix[i][j] for i in range(len(matrix))] 
              for j in reversed(range(len(matrix[0])))]
    res += matrix.pop(0)
  return res

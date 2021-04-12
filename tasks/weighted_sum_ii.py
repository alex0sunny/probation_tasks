# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list – whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, 
# now the weight is defined from bottom up. i.e., the leaf level integers have weight 1,
# and the root level integers have the largest weight.

def calc_depth(lst):
  depth = 1
  for e in lst:
    if type(e) == list:
      depth = max(depth, 1 + calc_depth(e))
  return depth

def calc_sum(lst, weight):
  res = 0
  for e in lst:
    if type(e) == list:
      res += calc_sum(e, weight - 1)
    else:
      res += weight * e
  return res

def depthSumInverse(nestedList):
  depth = calc_depth(nestedList)
  return calc_sum(nestedList, depth)

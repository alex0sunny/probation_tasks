''' Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number 
could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone 
buttons) is given below. 
Note that 1 does not map to any letters.
'''

def letterCombinations(digits):
  if not digits:
    return []
  d = {'2':'abc', '3':'def',  '4':'ghi', '5':'jkl', 
       '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
  res = []
  dig = digits[0]
  stack = [list(d[dig])]
  path = []
  while stack:
    if len(path) == len(digits):
      res.append(''.join(path))
      path.pop()
    elif not stack[-1]:
      if not path:
        break
      stack.pop()
      path.pop()
    else:
      path.append(stack[-1].pop())
      if len(path) < len(digits):
        dig = digits[len(path)]
        stack.append(list(d[dig]))                
  return res

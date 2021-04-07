# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

def find_length(A, B):
  la = len(A) 
  lb = len(B)
  l = 0
  for s in range(-la, lb):
    lc = 0
    if s < 0:
      sa = 0
      sb = -s
    else:
      sa = s
      sb = 0
    for i, j in zip(range(sa, la), range(sb, lb)):
      if A[i] == B[j]:
        lc += 1
        l = max(lc, l)
      else:
        lc = 0
    return l
  
  
def find_length2(A, B):
  la = len(A) 
  lb = len(B)
  l = 0
  for s in range(-la, lb):
    lc = 0
    for i, j in zip(range(s, s + lb), range(lb)):
      if 0 <= i < la:
        if A[i] == B[j]:
          lc += 1
          l = max(lc, l)
        else:
          lc = 0
    return l


  def find_length3(A, B):
    la = len(A) 
    lb = len(B)
    l = 0
    for s in range(-la, lb):
      lc = 0
      for i, j in zip(range(max(0, s), la), range(max(0, -s), lb)):
        if A[i] == B[j]:
          lc += 1
          l = max(lc, l)
        else:
          lc = 0
    return l

# Integer to Roman

# Example 1:

# Input: num = 3
# Output: "III"

# Example 2:

# Input: num = 4
# Output: "IV"

# Example 3:

# Input: num = 9
# Output: "IX"

# Example 4:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def intToRoman(num):
  romans_dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                           90:  'XC', 50:  'L', 40:  'XL', 10:  'X',
                           9:   'IX', 5:   'V', 4:   'IV', 1:   'I'}
  res = ''
  for divider, roman in romans_dic.items():
    res += roman * (num // divider)
    num = num % divider
  return res

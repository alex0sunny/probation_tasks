# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


def convert(s, numRows):
    if numRows == 1:
        return s
    rows = numRows * ['']
    down = False
    j = 0
    for i, sym in enumerate(s):
        rows[j] += sym
        if i % (numRows - 1) == 0:
            down = not down
        if down:
            j += 1
        else:
            j -= 1
    return ''.join(rows)

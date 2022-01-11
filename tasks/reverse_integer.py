# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
# causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

MAX_INT = int('1' * 31, 2)
MIN_INT = -MAX_INT - 1

def reverse(x):
    if x < 0:
        st = '-' + str(x)[:0:-1]
        if len(st) == len(str(MIN_INT)) and st > str(MIN_INT):
            return 0
    else:
        st = str(x)[::-1]
        if len(st) == len(str(MAX_INT)) and st > str(MAX_INT):
            return 0
    return int(st)


# consider that '-' is less than '0'..'9'
def reverse_short(x):
    st = '-' * (x < 0) + str(x)[:(0 if x < 0 else None):-1]
    if len(st) == len(str(MIN_INT)) and st > str(MIN_INT) or \
            len(st) == len(str(MAX_INT)) and st > str(MAX_INT):
        return 0
    return int(st)


assert reverse(-123) == -321

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31


def my_atoi(s):
    pos = 0
    while pos < len(s) and s[pos] == ' ':
        pos += 1
    st = ''
    if pos < len(s) and s[pos] in '+-':
        if s[pos] == '-':
            st = '-'
        pos += 1
    if pos == len(s) or not s[pos].isdigit():
        return 0
    while pos < len(s) and s[pos].isdigit():
        st += s[pos]
        pos += 1
    return min(MAX_INT, max(MIN_INT, int(st)))


assert my_atoi('   -42') == -42


TAIL_INI = [0, 0, '+', 0]
CUR_IND = -1
OP_IND = -2
LAST_IND = -3
RES_IND = -4


def calc_tail(stack):
    if stack[OP_IND] in '+-':
        stack[RES_IND] += stack[LAST_IND]
        stack[LAST_IND] = stack[CUR_IND] if stack[OP_IND] == '+' \
            else -stack[CUR_IND]
    elif stack[OP_IND] == '*':
        stack[LAST_IND] *= stack[CUR_IND]
    else:
        stack[LAST_IND] = int(stack[LAST_IND] / stack[CUR_IND])
    stack[-2:] = TAIL_INI[-2:]


def calc(s):
    stack = TAIL_INI[:]
    for i in range(len(s)):
        if s[i].isdigit():
            stack[CUR_IND] = int(s[i]) + stack[CUR_IND] * 10
            if i == len(s) - 1 or not s[i + 1].isdigit():
                calc_tail(stack)
        elif s[i] in '+-*/':
            stack[OP_IND] = s[i]
        elif s[i] == '(':
            stack[-1:] = TAIL_INI
        elif s[i] == ')':
            stack[-4:] = [stack[RES_IND] + stack[LAST_IND]]
            calc_tail(stack)
    return stack[RES_IND] + stack[LAST_IND]


assert calc('5 + 1-2') == 4
assert calc('(5 + 6 * 2) / 3') == 5
assert calc('1 - (2+3)') == -4

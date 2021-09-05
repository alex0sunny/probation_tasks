# get median of two sorted arrays
def get_middles(left, right):
    mid_left = (left + right - 1) // 2
    mid_right = (left + right) // 2
    return mid_left, mid_right


def get_median(a, left, right):
    mid_left, mid_right = get_middles(left, right)
    res = (a[mid_left] + a[mid_right]) / 2
    return res


def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a
    left_a = left_b = 0
    right_a = len(a)
    right_b = len(b)
    mid_a_left, mid_a_right = get_middles(left_a, right_a)
    mid_b_left, mid_b_right = get_middles(left_b, right_b)
    while right_a > left_a + 2:
        offset = mid_a_left - left_a
        if a[mid_a_right] > b[mid_b_right]:
            right_a -= offset
            left_b += offset
        elif a[mid_a_left] < b[mid_b_left]:
            left_a += offset
            right_b -= offset
        else:
            break
        mid_a_left, mid_a_right = get_middles(left_a, right_a)
        mid_b_left, mid_b_right = get_middles(left_b, right_b)
    c = a[mid_a_left:mid_a_right + 1]
    if right_b - left_b < 4:
        c = sorted(c + b[left_b:right_b])
    else:
        c = sorted(c + b[mid_b_left - 1:mid_b_right + 2])
    return get_median(c, 0, len(c))

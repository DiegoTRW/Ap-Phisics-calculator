from math import *
from math import sqrt


def roots(a, b, c):

    dis = b * b - 4 * a * c
    sqrt_val = sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        t1 = (-b + sqrt_val) / (2 * a)
        t2 = (-b - sqrt_val) / (2 * a)
        return t1, t2

    elif dis == 0:
        t = -b / (2 * a)
        return t

    # when discriminant is less than 0
    elif dis < 0:
        # print("""'
        aws1 = print(-b / (2 * a), "+i", sqrt_val / (2 * a))
        aws2 = print(-b / (2 * a), "-i", sqrt_val / (2 * a))
        return aws1, aws2
    if a == 0:
        aws1 = print("Input correct quadratic equation")
        return aws1


print(roots(1, 2, 3))

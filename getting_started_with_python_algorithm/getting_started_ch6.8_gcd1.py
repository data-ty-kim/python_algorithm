# 6.8 유클리드 호제법

def gcd(a, b):
    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    return b


print(gcd(1274, 975))

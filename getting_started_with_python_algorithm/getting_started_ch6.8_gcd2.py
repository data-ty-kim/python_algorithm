# 6.8 유클리드 호제법

# 인수 b가 0인 경우에도 오류 없이 처리 가능
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(gcd(1274, 975))

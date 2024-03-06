# 재귀용법

# 팩토리얼
def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)


# 리스트 합
def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


# 회문 판별
def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


# 콜라츠 추측
def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return (func(3 * n + 1))
    else:
        return (func(int(n / 2)))


# 정수 n을 1,2,3의 합으로 표현하는 경우의 수 - 손으로 직접 써서 패턴을 찾아라!
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)

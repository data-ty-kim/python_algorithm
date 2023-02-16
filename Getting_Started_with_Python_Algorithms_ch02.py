import sys
import math
import time

# 리스트 내포 주의할 점
print([i for i in range(10) if i % 2 == 0])
print([i if i % 2 == 0 else 0 for i in range(10)], '\n')


# 2.2 FizzBuzz
def fizzbuzz(number):
    for i in range(1, number+1):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i %5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')

# fizzbuzz(100)


# 2.3 Vending Machine
## 나의 풀이
class VendingMachine():
    def __init__(self, insert, product):
        self.insert = insert
        self.product = product
        self.change = self.insert - self.product

    def difference(self):
        if self.insert < self.product:
            raise ValueError("Insert more money to buy the product")
        else:
            # print(f"Here is your change: {change}")
            return self.change

    def bill_and_coin(self):
        bill_10 = self.change // 10000
        bill_5 = (self.change - 10000 * bill_10) // 5000
        bill_1 = (self.change - 10000 * bill_10 - 5000 * bill_5) // 1000
        coins = self.change - 1000 * (self.change // 1000)
        list_change = [bill_10, bill_5, bill_1, coins]

        print("Here is your change.")
        print(f"￦10,000: \t{list_change[0]}")
        print(f"￦5,000: \t{list_change[1]}")
        print(f"￦1,000: \t{list_change[2]}")
        print(f"coins: \t\t{list_change[3]}")
        return list_change

# test_vend = VendingMachine(10000, 3980)
# print(test_vend.bill_and_coin())
# print(test_vend.difference())

## 해답
# input_price = input('insert: ')
# if not input_price.isdecimal():
#     print('정수를 입력하세요.')
#     sys.exit()
#
# product_price = input('product: ')
# if not product_price.isdecimal():
#     print('정수를 입력하세요.')
#     sys.exit()
#
# change = int(input_price) - int(product_price)
#
# if change < 0:
#     print('금액이 부족합니다.')
#     sys.exit()
#
# coin = [5000, 1000, 500, 100, 50, 10, 5, 1]
#
# for i in coin:
#     r = change // i
#     change %= i
#     print(str(i) + ': ' + str(r))

## 해답반영하여 코드 개선해보기


# 2.4 기수 변환
## 10진수를 2진수로 변환
### 나의 풀이
def trasform_binary(number):
    if not isinstance(number, int):
        raise ValueError('It is not an integer!')
    else:
        list_remainder = []
        while number // 2 != 0:
            reamainder = number % 2
            list_remainder.append(reamainder)
            number //= 2
        list_remainder.append(1)
        list_binary = [str(i) for i in list_remainder[::-1]]
        return int(''.join(list_binary))

# print(trasform_binary(18))

### 해답 풀이
def convert(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

# print(convert(18,2))

### 해답 반영하여 코드 개선
def convert_binary(number):
    result = ''
    if not isinstance(number, int):
        raise ValueError('It is not an integer!')
    else:
        while number > 0:
            result = str(number % 2) + result
            number //= 2
    return result

# print(convert_binary(18))

## 2진수를 10진수로 변환
### 나의 풀이
def convert_decimal(number):
    result = []
    for i, j in enumerate(str(number)[::-1]):
        result.append(int(j)*(2**(i)))
    return sum(result)

# print(convert_decimal(10010))

### 해답 풀이
def convert3(n: str) -> int:
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (2 ** (len(n) - i - 1))
    return result

# print(convert3('10010'))

### 다른 방법
print(int('10010', 2), '\t\t', type(int('10010', 2)))
print(bin(18), '\t', type(bin(18)))
print(0b10010, '\t\t', type(0b10010))
print()

# 2.5 소수 판정하기
## 소수인지 알아보는 프로그램 만들기
### 나의 풀이
def is_prime(number: int) -> bool:
    divisor = 2
    while divisor <= math.sqrt(number):
        if number % divisor != 0:
            divisor += 1
        else:
            print(f"{number} is not a prime")
            break
    if divisor > math.sqrt(number):
        print(f"{number} is a prime")

# is_prime(79)

### 해답 풀이
def is_prime_1(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_time(n):
    for i in range(n):
        if is_prime_1(i):
            print(i, end='')

## 에라토스테네스의 체
def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    data = [i+1 for i in range(2, n, 2)]

    while limit >= data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]
    return prime + data

# 2.6 피보나치 수열
## 나의 풀이
def fibonacci_0(n):
    if n <= 2:
        return 1

    sequence = [1 for _ in range(n)]
    for i in range(2, n):
        sequence[i] = sequence[i-1] + sequence[i-2]

    return sequence[n-1]

## 답안 풀이 1
def fibonacci_1(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci_1(n-2) + fibonacci_1(n-1)
    # 재귀함수는 코드가 단순하나 속도가 느리다.

## 답안 풀이 2
def fibonacci_2(n):
    memo = {1: 1, 2: 1}
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_2(n-2) + fibonacci_2(n-1)
    return memo[n]

## 답안 풀이 3
def fibonacci_3(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])

    return fib[n-1]


# 내 풀이와 3번 풀이가 가장 빠르다. 3번 풀이가 근소하게 더 빠르긴 하다.
# 그런데 n이 일정 수 이상 더 커지면 ValueError가 발생한다. 해결법은 무엇일까?

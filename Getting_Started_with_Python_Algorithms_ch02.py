# 리스트 내포 주의할 점
print([i for i in range(10) if i % 2 == 0])
print([i if i % 2 == 0 else 0 for i in range(10)], '\n')


# 2.2.1 FizzBuzz
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

fizzbuzz(100)

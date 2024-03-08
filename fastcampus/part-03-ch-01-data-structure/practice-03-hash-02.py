# 코딩테스트 문제 풀이

# 수 찾기 (백준 1920번)
n = 5
array = [4, 1, 5, 2, 3]
m = 5
x = [1, 3, 7, 9, 5]

array = set(array)
for i in x:
    if i in array:
        print('1')
    else:
        print('0')

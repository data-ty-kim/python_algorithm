# 코딩테스트 문제 풀이

# 스택 수열 (백준 1874번)

input = [8, 4, 3, 6, 8, 7, 5, 2, 1]

n = input[0]
stack = []
answer = []
current = 1

for x in input[1:]:
    while not stack or stack[-1] < x:
        stack.append(current)
        current += 1
        answer.append('+')
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        break

for x in answer:
    print(x)

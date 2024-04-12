# 코딩테스트 문제 풀이

# 제로 (백준 10773번)

input = [10, 1, 3, 5, 4, 0, 0, 7, 0, 0, 6]
stack = []

for i in input[1:]:
    if i == 0:
        if stack:
            stack.pop()
    else:
        stack.append(i)

print(sum(stack))

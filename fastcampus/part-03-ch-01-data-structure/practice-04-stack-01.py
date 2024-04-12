# 코딩테스트 문제 풀이

# 스택 (백준 10828번)

input = [14, 'push 1', 'push 2', 'top', 'size', 'empty', 'pop', 'pop', 'pop',
         'size', 'empty', 'pop', 'push 3', 'empty', 'top']

n = input[0]
stack = []
result = []

for work in input[1:n+1]:
    command = work.split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        if not stack:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == 'top':
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

print(result)

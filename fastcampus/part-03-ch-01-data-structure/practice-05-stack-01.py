# 코딩테스트 문제 풀이

# 오큰수 (백준 17298번)

n = 4
arr = [3, 5, 2, 7]

stack = []
NGE = [-1] * n

for i in range(n):
    x = arr[i]
    if len(stack) == 0 or stack[-1][0] >= x:
        stack.append((x,i))
    else:
        while len(stack) > 0:
            previous, index = stack.pop()
            if previous >= x:
                stack.append((previous, index))
                break
            else:
                NGE[index] = x
        stack.append((x, i))

for x in NGE:
    print(x, end=' ')

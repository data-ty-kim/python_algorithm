# 코딩테스트 문제 풀이

# 회전하는 큐 (백준 1021번)

from collections import deque

n = 32
m = 6
d = deque([i for i in range(1, n+1)])
targets = [27, 16, 30, 11, 6, 23]
cnt = 0

for target in targets:
    index = d.index(target)
    if index <= len(d) // 2:
        for i in range(index):
            x = d.popleft()
            d.append(x)
            cnt += 1
    else:
        for i in range(len(d) - index):
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft()

print(cnt)

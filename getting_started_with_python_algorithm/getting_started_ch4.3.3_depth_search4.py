# 4.3.3 깊이 우선 탐색 구현하기
# while문과 for문을 중첩 사용해 구현하기
tree = [[1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [13,14],
        [], [], [], [], [], [], [], []]
data = [0]

while len(data) > 0:
    pos = data.pop()
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)

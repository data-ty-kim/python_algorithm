# 4.3.2 너비 우선 탐색 구현하기
tree = [[1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [13,14],
        [], [], [], [], [], [], [], []]
data = [0]

while len(data) > 0:
    pos = data.pop(0)
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)

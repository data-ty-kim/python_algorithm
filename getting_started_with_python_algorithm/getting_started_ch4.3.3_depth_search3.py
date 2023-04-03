# 4.3.3 깊이 우선 탐색 구현하기
# 중위 순회
tree = [[1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [13,14],
        [], [], [], [], [], [], [], []]


def search(pos):
    if len(tree[pos]) == 2:
        search(tree[pos][0])
        print(pos, end=' ')
        search(tree[pos][1])
    elif len(tree[pos]) == 1:
        search(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')


search(0)

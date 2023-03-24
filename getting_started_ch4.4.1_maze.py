# 4.4 다양한 예제 구현하기
# %%
maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,9,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]

# 너비탐색
# 시작 위치(x좌표, y좌표, 이동횟수)를 설정
pos = [[1,1,0]]

while len(pos) > 0:
    x, y, depth = pos.pop(0)

    # 목표에 도달하면 종료
    if maze[x][y] == 1:
        print(depth)
        break

    # 탐색 완료로 설정
    maze[x][y] = 2

    # 상하좌우 탐색
    if maze[x-1][y] < 2:
        pos.append([x-1, y, depth + 1])
    if maze[x+1][y] < 2:
        pos.append([x+1, y, depth + 1])
    if maze[x][y-1] < 2:
        pos.append([x, y-1, depth + 1])
    if maze[x][y+1] < 2:
        pos.append([x, y+1, depth + 1])

# %%
maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,9,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]

# 깊이 우선 탐색
def search(x, y, depth):
    # 목표에 도달하면 종료
    if maze[x][y] == 1:
        print(depth)
        exit()

    # 탐색 완료로 설정
    maze[x][y] = 2

    # 상하좌우 탐색
    if maze[x-1][y] < 2:
        search(x-1, y, depth + 1)
    if maze[x+1][y] < 2:
        search(x+1, y, depth + 1)
    if maze[x][y-1] < 2:
        search(x, y-1, depth + 1)
    if maze[x][y+1] < 2:
        search(x, y+1, depth + 1)

    # 탐색 전으로 되돌리기
    maze[x][y] = 0

# 시작 위치에서 출발
print()
search(1, 1, 0)

# %%
maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,9,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]

# 우수법에서의 이동 방향(하, 우, 상, 좌) 설정
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 시작 위치(x좌표, y좌표, 이동 횟수, 방향) 설정
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    # 탐색 완료로 설정
    maze[x][y] = 2

    # 우수법으로 탐색
    for i in range(len(dir)):
        # 진행 방향의 오른쪽부터 순서대로 탐험
        j = (d + i - 1) % len(dir)

        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            # 방문하지 않은 경우에는 진행하여 이동 횟수를 늘림
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
            # 이미 방문한 경우에는 진행하여 이동 횟수를 줄임
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break

print(depth)

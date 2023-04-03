# 5.2 선택정렬

# 5.2.1 작은 요소 고르기
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
min = 0

for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i

print(min)

# 5.2.2 선택 정렬의 구현
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    min = i
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j

    # 최솟값의 위치에 현재의 요소를 교환
    data[i], data[min] = data[min], data[i]

print(data)

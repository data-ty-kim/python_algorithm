# 5.5 힙 정렬

# 5.5.10 힙 정렬 구현하기
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
        j = (j - 1) // 2

# 정렬 실행
for i in range(len(data), 0, -1):
    # 힙의 맨 앞과 교환
    data[i - 1], data[0] = data[0], data[i -]

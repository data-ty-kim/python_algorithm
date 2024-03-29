# 5.5 힙 정렬

# 5.5.11 범용적인 힙 정렬 구현하기
def heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    size = len(data) - 1
    min = i
    if left <= size and data[min] > data[left]:
        min = left
    if right <= size and data[min] > data[right]:
        min = right
    if min != i:
        data[i], data[min] = data[min], data[i]
        heapify(data, min)

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in reversed(range(len(data) // 2)):
    heapify(data, i)

# 정렬 실행
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0]
    sorted_data.append(data.pop())
    heapify(data, 0)

print(sorted_data)

# 5.5 힙 정렬

# 5.5.12 라이브러리 활용
import heapq

def heap_sort(array):
    h = array.copy()
    heapq.heapify(h)    # 힙구성
    return [heapq.heappop(h) for _ in range(len(array))]

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

print(heap_sort(data))

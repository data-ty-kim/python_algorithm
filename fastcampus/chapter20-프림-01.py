# 프림 알고리즘 (Prim's algoritm)

import heapq
from collections import defaultdict

# 참고 1: heapq 라이브러리
# heappush, heappop
queue = []
graph_data = [[2, 'A'], [5, 'B'], [3,'C']]

for edge in graph_data:
    heapq.heappush(queue, edge)

for index in range(len(queue)):
    print(heapq.heappop(queue))

# heapify
graph_data_0 = [[7, 'A'], [10, 'B'], [8,'C']]

heapq.heapify(graph_data_0)

for index in range(len(graph_data_0)):
    print(heapq.heappop(graph_data_0))

# 참고 2: collections 라이브러리
# key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화하기
list_dict = defaultdict(int)
print(list_dict['key1'])

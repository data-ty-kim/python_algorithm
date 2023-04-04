# 5.5 힙 정렬

# 5.5.5 큐 구현하기
import queue

q = queue.Queue()
q.put(3)
q.put(5)
q.put(2)

temp = q.get()
print(temp)     # 3
temp = q.get()
print(temp)     # 5

q.put(4)

temp = q.get()
print(temp)     # 2

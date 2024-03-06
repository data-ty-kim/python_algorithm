# 실전코딩테스트 - 탐색 알고리즘

# 문제가 이해하기 어렵다면? 입력과 출력을 비교해가며 문제를 읽어보기!

# 수 찾기 (백준 1920번)
N = 5
N_list = [4,1,5,2,3]
M = 5
M_list = [1,3,7,9,5]

# 다음 방식은 O(n^2) 의 시간 복잡도
for item in M_list:
    if item in N_list:
        print(1)
    else:
        print(0)

# 이진 탐색 - 시간 복잡도 O(log n)
N_list.sort()

def binary_search(value, start, end):
    if start > end:
        return False

    median = (start + end) // 2
    if N_list[median] > value:
        return binary_search(value, start, median - 1)
    elif N_list[median] < value:
        return binary_search(value, median + 1, end)
    else:
        return True

for item in M_list:
    if binary_search(item, 0, N-1):
        print(1)
    else:
        print(0)

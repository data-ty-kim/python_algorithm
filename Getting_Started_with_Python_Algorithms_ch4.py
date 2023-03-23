# Chapter 3 복잡도 학습하기

# 3.1 계산 비용, 실행시간, 시간 복잡도

# 3.2 자료구조에 따른 복잡도 차이

# 3.3 알고리즘 복잡도와 문제 복잡도


# Chapter 4 다양한 검색 방법 배우기

# 4.1 선형검색

# 4.1.2 프로그래밍의 검색
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

def search_forty(data):
    found = False
    for i in range(len(data)):
        if data[i] == 40:
            print(i)
            found = True
            break
    if not found:
        print('Not Found')

search_forty(data)

# 4.1.3 선형 검색 함수 정의하기
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

print(linear_search(data, 40))

# 4.2 이진 검색

# 4.2.1 검색 범위를 반으로 나누기
sorted_data = sorted(data)

def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        pass

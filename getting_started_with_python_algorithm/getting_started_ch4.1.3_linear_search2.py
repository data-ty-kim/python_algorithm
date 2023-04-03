# 4.1.3 선형 검색 함수 정의하기
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

print(linear_search(data, 40))

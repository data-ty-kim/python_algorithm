# 4.2.1 검색 범위를 반으로 나누기
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
sorted_data = sorted(data)

def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) //2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search(sorted_data, 90))

# 병합 정렬 (merge sort)
# 분할 정복 알고리즘의 대표적인 예!

import random

# 연습1: 어떤 데이터리스트가 있을 때 리스트를 앞뒤로 자르는 코드 작성해보기
def split(data):
    medium = len(data) // 2
    left = data[:medium]
    right = data[medium:]
    print(left, right)


# data_list = [3,4,1,3,2]
# split(data_list)

# 연습2: 리스트 개수가 한 개수가 한 개이면 해당 값 리턴, 그렇지 않으면 둘로 나누기
def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = len(data) // 2
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_point, right_point = 0, 0

    # case1: left/right 아직 남아 있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2: left만 남아 있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아 있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


data_list = random.sample(range(100), 10)

print(mergesplit(data_list))

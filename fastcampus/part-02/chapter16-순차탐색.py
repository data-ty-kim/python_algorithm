# 순차 탐색
import random

rand_data_list = []
for num in range(10):
    rand_data_list.append(random.randint(1, 100))


def sequential(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1


print(rand_data_list)
print(sequential(rand_data_list, 4))

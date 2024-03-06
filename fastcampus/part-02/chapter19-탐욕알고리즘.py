# 탐욕 알고리즘 (Greedy Algorithm)

# 문제1: 동전 문제
# 지불해야 하는 값이 4720원일 때, 1원, 50원, 100원, 500원 동전으로
# 동전의 수가 가장 적게 지불하시오.
def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = []
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details


coin_list = [1, 100, 50, 500]
# print(min_coin_count(4720, coin_list))


# 문제2: 부분 배낭 문제 (Fractional Knapsack Problem)
# 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
# 물건은 쪼갤 수 있으므로 물건의 일부분을 배낭에 넣을 수 있음
# 그래서 Fractional Knapsack Problem으로 불림
def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    details = []

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], 1])
        else:
            fraction = capacity / data[0]
            capacity -= data[0] * fraction
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details


data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
# print(get_max_value(data_list, 30))

# 코딩테스트 문제 풀이

# 블랙잭 (백준 2798번)

# # test case 1
# n = 5
# m = 21
# data = [5, 6, 7, 8, 9]

# test case 2
n = 10
m = 500
data = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

# 풀이
from itertools import combinations

list_sum = list(map(sum, combinations(data, 3)))
result = max([i for i in list_sum if i <= m])

print(result)

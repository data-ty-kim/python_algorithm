# 실전코딩테스트 - 탐욕알고리즘

# 패턴이 비슷해서 많이 풀면 금방 익숙해진다.

# ATM (백준 11399번)
N = 5
N_list = [3,1,4,3,2]
minimum = 0

# # 강사 풀이
# N_list.sort()
# for index in range(N):
#     for index2 in range(index+1):
#         minimum += N_list[index2]
#
# print(minimum)

# 내 풀이
N_list.sort()
print(sum([sum(N_list[:i+1]) for i in range(N)]))

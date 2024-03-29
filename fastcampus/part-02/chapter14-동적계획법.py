# 동적계획법(Dynamic Programming; DP라고 많이 부름)

# 피보나치 수열
def fibo_dp(num):
    cache = [0 for index in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]

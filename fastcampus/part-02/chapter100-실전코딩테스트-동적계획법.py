# 실전 코딩 테스트 - 동적 계획법

# 점화식을 먼저 찾고 코드를 작성하라! (점화식? 동적 계획법!)
# dp[n] = dp[n-1] + dp[n-2]

# 2*n 타일링 (백준 11726번)
def tiling(n):
    # 1. (입력값에 따른) 빈리스트 만들기
    dp = [None for _ in range(n+1)]
    # 2. 초기값을 설정
    dp[1] = 1
    dp[2] = 2
    # 3. 점화식 기반으로 계산값 적용하기
    for index in range(3, n+1):
        dp[index] = (dp[index-1] % 10007 + dp[index-2] % 10007) % 10007
    # 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
    return dp[n]

# print(tiling(2))
# print(tiling(9))

# 파도반 수열 (백준 9461번)
def padovan(n):
    # 1. (입력값에 따른) 빈리스트 만들기
    dp = [None for _ in range(n+3)]
    # 2. 초기값을 설정
    dp[1], dp[2], dp[3] = 1, 1, 1
    # 3. 점화식 기반으로 계산값 적용하기
    for index in range(1, n-2):
        dp[index+3] = dp[index] + dp[index+1]
    # 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
    return dp[n]

# print(padovan(6))
# print(padovan(12))
# print(padovan(100))

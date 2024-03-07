# 코딩테스트 문제 풀이

# 스택 수열 (백준 1874번)
data_input = [8, 4, 3, 6, 8, 7, 5, 2, 1]
n = data_input[0]

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = data_input[i]
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')

    if stack[-1] == data:   # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else:                   # 불가능한 경우
        print('NO')
        exit(0)             # 코드 강제 종료 (0은 성공적으로 종료)

print(result)

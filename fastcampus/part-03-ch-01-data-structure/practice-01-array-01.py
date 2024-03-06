# 코딩테스트 문제 풀이

# 음계 (백준 2920번)
a = list(map(int, input().split(' ')))

ascending = True
descending = False

for i in range(1, 8):   # 다 장조는 총 8개 음이라서
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

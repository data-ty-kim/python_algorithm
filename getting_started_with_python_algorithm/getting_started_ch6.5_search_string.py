# 6.5 완전 탐색 알고리즘

text = list('DYITBOOK DYSHOP')
pattern = list('DYS')

for i in range(len(text)):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:
        print(i)
        break

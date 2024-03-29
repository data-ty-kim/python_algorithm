# 6.5 보이어-무어 알고리즘

text = list('DYITBOOK DYSHOP')
pattern = list('DYS')
skip = {}

for i in range(len(pattern) - 1):
    skip[pattern[i]] = len(pattern) - i - 1

i = len(pattern) - 1
while i < len(text):
    match = True
    for j in range(len(pattern)):
        if text[i - j] != pattern[len(pattern) - 1 - j]:
            match = False
            break
    if match:
        print(i - len(pattern) + 1)
        break
    if text[i] in skip:
        i += skip[text[i]]
    else:
        i += len(pattern)

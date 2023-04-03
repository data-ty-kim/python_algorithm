# 5.4 버블 정렬

# 5.4.2 버블 정렬 구현하기
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(data)

# 버블 정렬 개선하기
change = True
for i in range(len(data)):
    if not change:
        break
    change = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True

print(data)

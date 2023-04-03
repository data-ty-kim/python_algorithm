# 4.1.2 프로그래밍의 검색
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

def search_forty(data):
    found = False
    for i in range(len(data)):
        if data[i] == 40:
            print(i)
            found = True
            break
    if not found:
        print('Not Found')

search_forty(data)

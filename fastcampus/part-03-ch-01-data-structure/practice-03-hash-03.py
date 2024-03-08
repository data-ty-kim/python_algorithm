# 코딩테스트 문제 풀이

# 친구 네트워크 (백준 4195번)
# 합 집합 찾기(Union-Find) 알고리즘
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


# f = 3
# input_data = [('Fred', 'Barney'), ('Barney', 'Betty'), ('Betty', 'Wilma')]
input_data = [('Fred', 'Barney'), ('Betty', 'Wilma'), ('Barney', 'Betty')]

parent = {}
number = {}

for input in input_data:
    x, y = input

    if x not in parent:
        parent[x] = x
        number[x] = 1
    if y not in parent:
        parent[y] = y
        number[y] = 1

    union(x, y)

    print(number[find(x)])

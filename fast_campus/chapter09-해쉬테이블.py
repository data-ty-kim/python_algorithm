# hash table 만들기
hash_table = list([0 for i in range(10)])
# print(hash_table)


def hash_func(key):
    return key % 5


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord(): 문자의 ASCII코드 리턴 - key값으로 활용하기
print('[ASCII 코드]')
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))


# 해쉬 테이블에 값 저장
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print()
print('[해쉬 테이블 값 출력]')
print(get_data('Andy'))


# 리스트 변수를 활용해서 해쉬 테이블 구현해보기
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print()
print('[예제 출력]')
print(read_data('Dave'))
print(hash_table)


# Chaining 기법 - linked list를 써야 하지만 여기서는 Python의 list를 활용
hash_table = list([0 for i in range(8)])


# def get_key()

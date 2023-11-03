# 빈번한 충돌을 개선하는 기법
# 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대
# 예: hash_table = [0 for _ in range(16)]

# 참고: 해쉬 함수와 키 생성 함수
# SHA-1
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest() # 16진수 변환
print(hex_dig)

# SHA-256
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest() # 16진수 변환
print(hex_dig) # 역추론은 불가!

# Chaining 기법을 적용한 해쉬 테이블 코드에
# 키 생성함수를 sha256 해쉬 알고리즘을 사용하도록 변경해보기
hash_table = [0 for _ in range(8)]


def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest() # 16진수 변환
    return int(hex_dig, 16)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
                return hash_table[hash_address].append([index_key, value])
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


save_data('Dale', '01012340001')
save_data('Dallas', '01012340002')
save_data('Damon', '01012340003')
save_data('Daniel', '01012340004')
save_data('Dante', '01012340005')
save_data('Daren', '01012340006')

print(hash_table)


# 해쉬테이블의 시간 복잡도
# 일반적인 경우(collision이 없는 경우)는 O(1)
# 최악의 경우(collision이 모두 발생한 경우)는 O(n)

# 검색에서 해쉬테이블의 사용 예
# 16개의 배열에 데이터를 저장하고, 검색할 때 O(n)
# 16개의 데이터 저장공간을 가진 위의 해쉬테이블에 데이터를 저장하고 검색할 때 O(1)

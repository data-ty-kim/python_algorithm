# Chaining 기법 - linked list를 써야 하지만 여기서는 Python의 list를 활용
hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


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
save_data('David', '01012340007')
save_data('Dean', '01012340007')
save_data('Dennis', '01012340009')
save_data('Derrick', '01012340010')

print(hash_table)

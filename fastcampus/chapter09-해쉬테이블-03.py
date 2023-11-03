# Linear Probing 기법
hash_table = [0 for _ in range(8)]


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hahs_address, len(hash_table)):
            if hash_table[index] ==0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


print('Dale: ', hash('Dale')%8)
print('Dallas: ', hash('Dallas')%8)
print('Damon: ', hash('Damon')%8)
print('Daniel: ', hash('Daniel')%8)

save_data('Dale', '01012340001')
save_data('Dallas', '01012340002')
save_data('Damon', '01012340003')
save_data('Daniel', '01012340004')

print(hash_table)

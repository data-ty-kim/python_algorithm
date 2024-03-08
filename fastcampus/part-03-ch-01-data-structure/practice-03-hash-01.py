# 코딩테스트 문제 풀이

# SHA-256 (백준 10930번)
from hashlib import sha256

input_data = 'Baekjoon'
encoded_data = input_data.encode()
result = sha256(encoded_data).hexdigest()

print(result)

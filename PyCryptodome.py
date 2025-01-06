"""
pip install ..

"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 暗号化キーとデータ
key = get_random_bytes(16)
data = b'Secret Data'

# 暗号化
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(f'Ciphertext: {ciphertext}')

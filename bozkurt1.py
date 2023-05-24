from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size)
    return plaintext.decode()


# Örnek kullanım
plaintextt = "Merhaba, dünya!"
key = b"mysecret"  # 8 karakterlik bir anahtar
ciphertext = des_encrypt(plaintextt, key)
print("sifreli metin",ciphertext)
plaintext=des_decrypt(ciphertext,key)
print("çözülen sifre=",plaintext)
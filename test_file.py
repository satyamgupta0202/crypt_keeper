from crypt_keeper import CryptKeeper

k = CryptKeeper()

def test_encrypt():
    print(k.encrypt_str("name"))


test_encrypt()
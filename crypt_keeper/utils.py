import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class CryptKeeper:
    def __init__(self):
        self.__current_private_key = "aaaaaaaaaaaaaaaa".encode('utf-8')
        self.__current_identity_iv = "aaaaaaaaaaaaaaaa".encode('utf-8')

    def encrypt_str(self, value: str) -> str:
        # Convert the string to bytes and pad it to the AES block size
        data = pad(value.encode(), AES.block_size)

        # Initialize the cipher with the key and IV
        cipher = AES.new(self.__current_private_key, AES.MODE_CBC, self.__current_identity_iv)

        # Encrypt the padded data
        encrypted_data = cipher.encrypt(data)

        # Encode the encrypted data in Base64 to ensure it can be safely stored or transmitted
        encoded_base64 = base64.b64encode(encrypted_data)

        # Return the Base64 encoded string, decoding it from bytes to a string
        return encoded_base64.decode("utf-8", "ignore")

    def decrypt_str(self, value: str) -> str:

        # Decode the Base64 encoded encrypted string to get the original encrypted bytes
        enc = base64.b64decode(value)

        # Initialize the cipher with the key and IV in CBC mode
        cipher = AES.new(self.__current_private_key , AES.MODE_CBC, self.__current_identity_iv)

        # Decrypt the data and then remove the padding
        decoded_str = unpad(cipher.decrypt(enc), AES.block_size)

        # Decode the bytes to a string and return
        return decoded_str.decode("utf-8", "ignore")
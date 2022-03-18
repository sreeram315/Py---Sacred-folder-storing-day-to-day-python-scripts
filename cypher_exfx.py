from Crypto.Cipher import AES
import base64
import binascii

MASTER_KEY = "JegatheeswaranBillion@123"


def encrypt_val(clear_text):
    enc_secret 		= 	AES.new(MASTER_KEY[:16])
    tag_string 		= 	(str(clear_text) + (AES.block_size - len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text 	= 	base64.b64encode(enc_secret.encrypt(tag_string))
    return cipher_text.decode()


def decrypt_val(cipher_text):
    cipher_text 		= 	cipher_text.encode()
    dec_secret		 	= 	AES.new(MASTER_KEY[:16])
    raw_decrypted 		= 	dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val 			= 	raw_decrypted.decode().rstrip("\0")
    return clear_val


# print(encrypt_val(1))
print(decrypt_val("CmPu2xinK4cO2PRFVcRQyw=="))
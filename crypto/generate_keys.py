from common_config import RSA_KEYS
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

'''
funcion de encripcion 

              clave publica  
-> fichero ------- | ------- fichero encriptado

@:param blob -> fichero a encriptar ( tipo file)
@:public_key -> clave publica como file 
'''


def encrypt_blob(blob, public_key):
    # Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    # compress the data first
    blob = zlib.compress(blob)

    # In determining the chunk size, determine the private key length used in bytes
    # and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    # in chunks
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = ""

    while not end_loop:
        # The chunk
        chunk = blob[offset:offset + chunk_size]
        # If the data chunk is less then the chunk size, then we need to add
        # padding with " ". This indicates the we reached the end of the file
        # so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))

        # Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        # Increase the offset by chunk size
        offset += chunk_size

    # Base 64 encode the encrypted file
    return base64.b64encode(encrypted)


'''
 @:param, key(str), ruta y nombre del fichero a leer
 Se usara para leer tanto las claves como los ficheros fuentes para la encriptacion
 @:return, tipo (file)
'''


def read_file(key):
    if os.path.exists(key):
        with open(key, "rb") as fichero:
            readed_file = fichero.read()

        return readed_file

    return None


def generate_keys():
    # Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)
    # Private key PEM format
    private_key = new_key.exportKey("PEM")
    # Public key  PEM Format
    public_key = new_key.publickey().exportKey("PEM")

    return private_key, public_key


def generate_file_key(key, key_name):
    print("Generating {}".format(key_name))
    fd = open("{}{}{}.pem".format(RSA_KEYS, os.path.sep, key_name), "wb")
    fd.write(key)
    fd.close()


if __name__ == '__main__':
    private, public = generate_keys()
    generate_file_key(private, "private_key")
    generate_file_key(public, "public_key")

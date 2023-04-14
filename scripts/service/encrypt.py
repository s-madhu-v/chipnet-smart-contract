from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

directory = "./"
publicKeyFile = 'public.pem'
privteKeyFile = "private.pem"
filename = 'example.txt'

def doesFileExist(filename, directory):
    if os.path.isfile(os.path.join(directory, filename)):
        return True
    else:
        return False

def generateAndStoreKeys(n=2048):
    keyPair = RSA.generate(n)
    publicKey = keyPair.publickey().export_key()
    privateKey = keyPair.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(privateKey)
    file_out.close()
    file_out = open("public.pem", "wb")
    file_out.write(publicKey)
    file_out.close()

def generateKeysIfTheyDontExist():
    if doesFileExist(publicKeyFile, directory) == False:
        generateAndStoreKeys()
    if doesFileExist(privteKeyFile, directory) == False:
        generateAndStoreKeys()

def readPublicKey():
    publicKey = RSA.import_key(open("public.pem").read())
    return publicKey

def readPrivateKey():
    privateKey = RSA.import_key(open("private.pem").read())
    return privateKey

def encryptMsg(message, publicKey):
    cipher = PKCS1_OAEP.new(publicKey)
    encryptedMsg = cipher.encrypt(message)
    return encryptedMsg

def decryptMsg(encryptedMsg, privateKey):
    cipher = PKCS1_OAEP.new(privateKey)
    decryptedMsg = cipher.decrypt(encryptedMsg)
    return decryptedMsg
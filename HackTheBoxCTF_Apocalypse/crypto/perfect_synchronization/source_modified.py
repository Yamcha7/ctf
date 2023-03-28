from os import urandom
from Crypto.Cipher import AES
#from secret import MESSAGE
MESSAGE = "HI SOUNAK THE FLAG IS HTB{VIEW_SOURCE_CAN_BE_USEFUL} THANK YOU"

assert all([x.isupper() or x in '{_} ' for x in MESSAGE])


class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        key = urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    cipher = Cipher()
    encrypted = cipher.encrypt(MESSAGE)
    #print(encrypted)
    
    #print("\n\n")
    encrypted = "\n".join([c.hex() for c in encrypted])
    #print(encrypted)

    with open("output3.txt", 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()


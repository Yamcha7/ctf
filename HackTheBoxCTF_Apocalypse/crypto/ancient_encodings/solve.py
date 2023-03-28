from base64 import b64decode
from Crypto.Util.number import long_to_bytes

f = open("output2.txt","r")
encoded_message = f.read().splitlines()
encoded_message = " ".join(encoded_message)

#getting bytes from hex
decoded_message = bytes.fromhex(encoded_message)


#decoding base64 from the decoded hex message 
decoded_message = b64decode(decoded_message)
print(decoded_message)



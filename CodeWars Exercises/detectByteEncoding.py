import binascii

import chardet

byte = b'\xc2\x01\xbb\xd4\x81\xbb\x01\xfd\x10\x10\xff\xff\x9e\x00\x00'

#print("Converts byte to Hex: ", byte.hex())
#print("Converts Hex to str: ", byte.fromhex(byte.hex()).decode('utf-8'))
#print(byte.decode("latin-1"))
#print(type(byte))

the_encoding = chardet.detect(b'\xce\x9c\xce\xb9\xce\xb1 \xce\xb3\xcf\x81\xce\xae\xce\xb3\xce\xbf\xcf\x81\xce\xb7 \xce\xba\xce\xb1\xcf\x86\xce\xad \xce\xb1\xce\xbb\xce\xb5\xcf\x80\xce\xbf\xcf\x8d')['encoding']
print(the_encoding)
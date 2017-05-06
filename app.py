import time, hashlib, binascii, struct

key = 'test key'
t0 = 0
ti = 30
t_now = time.time()
N = 6

C = str(int(t_now / ti))
H = hashlib.pbkdf2_hmac('sha256', bytes(C, encoding='utf-8'), bytes(key, encoding='utf-8'), 100000)
O = ord(H[-1:]) & 0b00001111
I = struct.unpack(">I", H[O:O+4])[0] & 0x7ffffffff
token = I % 10**N
print(token)

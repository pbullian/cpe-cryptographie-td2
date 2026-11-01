"""Dechiffre le message de la capture DH une fois le secret partage trouve.

Usage : python3 dechiffrer.py <secret_partage>
"""
import hashlib, re, sys
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

if len(sys.argv) != 2:
    sys.exit('usage : python3 dechiffrer.py <secret_partage>')
cap = open(__file__.replace('dechiffrer.py', 'capture_dh.txt')).read()
iv = bytes.fromhex(re.search(r'^iv = (\w+)', cap, re.M).group(1))
ct = bytes.fromhex(re.search(r'^ct = (\w+)', cap, re.M).group(1))
key = hashlib.sha256(sys.argv[1].encode()).digest()[:16]
try:
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    up = padding.PKCS7(128).unpadder()
    print((up.update(dec.update(ct) + dec.finalize()) + up.finalize()).decode())
except Exception:
    print('Echec : ce secret ne dechiffre pas le message.')

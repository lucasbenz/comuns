#!pip install cryptography

from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"string teste")
c= digest.finalize()

print(c)

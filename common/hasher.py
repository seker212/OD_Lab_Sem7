from hashlib import sha256

def GetSHA256(data: bytes) -> bytes:
    hasher = sha256()
    hasher.update(data)
    return hasher.digest()
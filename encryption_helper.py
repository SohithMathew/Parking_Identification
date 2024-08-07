from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os
from base64 import urlsafe_b64encode, urlsafe_b64decode

def hash_password(password: str, salt: bytes = None) -> tuple:
    if not salt:
        salt = os.urandom(16)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return urlsafe_b64encode(salt).decode(), urlsafe_b64encode(key).decode()

def verify_password(stored_password: str, provided_password: str, salt: str) -> bool:
    try:
        salt_bytes = urlsafe_b64decode(salt.encode())
        stored_password_bytes = urlsafe_b64decode(stored_password.encode())
        kdf = Scrypt(
            salt=salt_bytes,
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
        )
        kdf.verify(provided_password.encode(), stored_password_bytes)
        return True
    except Exception as e:
        return False

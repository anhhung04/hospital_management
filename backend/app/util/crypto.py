import uuid
from hashlib import sha256

def random_key() -> str:
    return uuid.uuid4().hex


def hash_password(password: str, salt: str) -> str:
    return sha256(password.encode() + salt.encode()).hexdigest()


def verify_password(hashed_password: str, password: str, salt: str) -> bool:
    return hashed_password == hash_password(password, salt)

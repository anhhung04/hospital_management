import uuid
from passlib.context import CryptContext

def random_key() -> str:
    return uuid.uuid4().hex

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


__all__ = ["random_key", "password_context"]
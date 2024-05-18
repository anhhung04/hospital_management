import uuid
from hashlib import sha256


class PasswordContext:
    @staticmethod
    def rand_key() -> str:
        return uuid.uuid4().hex

    def __init__(self, password: str, salt: str):
        self._salt: str = salt
        self._password = password

    def hash(self) -> str:
        return sha256(self._password.encode() + self._salt.encode()).hexdigest()

    def verify(self, hashed_password: str) -> bool:
        return hashed_password == self.hash()

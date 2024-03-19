import uuid

def random_key() -> str:
    return uuid.uuid4().hex
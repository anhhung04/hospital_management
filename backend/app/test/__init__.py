import random
import string


def gen_username():
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def gen_password():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

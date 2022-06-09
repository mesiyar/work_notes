import random
import string
import uuid
from functools import partial
from os import urandom
from struct import unpack

ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase
ALPHABET_UPPER = string.digits + string.ascii_uppercase


def get_uuid():
    return uuid.uuid4().hex


def generate_short_id(is_upper=False):
    """
     Short ID generator base62-encoded Urandom
    """
    num = unpack('<Q', urandom(8))[0]
    return base62_encode(num) if not is_upper else base36_encode(num)


def _inner_encode(num, alphabet):
    if isinstance(num, str) and num.isdigit():
        num = int(num)

    if not isinstance(num, int):
        return '0'

    alphabet_len = len(alphabet)
    if num <= 0:
        result = '0'
    else:
        key = []
        while num > 0:
            num, rem = divmod(num, alphabet_len)
            key.append(alphabet[rem])

        result = ''.join(reversed(key))

    return result


def _inner_decode(val, alphabet):
    if not isinstance(val, str):
        return 0

    alphabet_len = len(alphabet)
    num = 0
    for idx, ele in enumerate(reversed(val)):
        tmp = alphabet.index(ele)
        num += pow(alphabet_len, idx) * tmp

    return num


base62_encode = partial(_inner_encode, alphabet=ALPHABET)
base62_decode = partial(_inner_decode, alphabet=ALPHABET)

base36_encode = partial(_inner_encode, alphabet=ALPHABET_UPPER)
base36_decode = partial(_inner_decode, alphabet=ALPHABET_UPPER)


def random_str(length=16):
    random_string = string.digits + string.ascii_letters
    return ''.join(random.sample(random_string, length))


if __name__ == '__main__':
    for _ in range(10):
        print(generate_short_id())

import random
import string

DEFAULT_ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'

def base62_encode(string, alphabet=None, length=5):
    """Encode a string in Base62 with a custom alphabet and fixed length."""
    if alphabet is None:
        alphabet = DEFAULT_ALPHABET
    prime = len(alphabet)
    
    # Generate a random starting value for hash_value
    random.seed()
    hash_value = random.randint(0, prime ** (length - 1))
    
    encoded = ''
    for _ in range(length - 1):
        hash_value, rem = divmod(hash_value, prime)
        encoded = alphabet[rem] + encoded
    return alphabet[0] + encoded

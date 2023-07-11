import string

def base62_encode(num, alphabet=string.ascii_letters + string.digits):
    """Encode a number in Base62 with custom alphabet."""
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)
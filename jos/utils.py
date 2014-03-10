import hashlib
from datetime import datetime


def gen_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def sign(secret, params):
    """generate signature based on app secret and parameters.

    :param secret: a valid app secret
    :param params: parameters which are required to generate valid signature.
                   should be a dict.
    """
    keys = params.keys()
    keys.sort()

    p_string = ''.join('%s%s' % (key, params[key]) for key in keys)
    p_string = ''.join([secret, p_string, secret])

    sign = hashlib.md5(p_string).hexdigest().upper()

    return sign

import hashlib

def sign(secret, params):
    '''
        params目前只支持字典类型
    '''

    keys = parameters.keys()
    keys.sort()

    p_string = "%s%s%s" % (secret, \
            ''.join('%s%s' % (key, params[key]) for key in keys), \
            secret)

    sign = hashlib.md5(p_string).hexdigest().upper()

    return sign

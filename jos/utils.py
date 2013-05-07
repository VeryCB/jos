#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime

def gen_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def sign(secret, params):
    '''
        params目前只支持字典类型
    '''

    keys = params.keys()
    keys.sort()

    p_string = "%s%s%s" % (secret, \
            ''.join('%s%s' % (key, params[key]) for key in keys), \
            secret)

    sign = hashlib.md5(p_string).hexdigest().upper()

    return sign

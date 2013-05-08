#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import APP_KEY, APP_SECRET, BASE_URL
from utils import sign, gen_timestamp

import requests
import json

class JOS(object):

    def __init__(self):
        self.key = APP_KEY
        self.secret = APP_SECRET

    def get(self, method, app_params=None):
        params = {
                    'method': method,
                    'app_key': self.key,
                    'timestamp': gen_timestamp(),
                    'v': '2.0',
                    '360buy_param_json': json.dumps(app_params),
                 }

        params['sign'] = sign(self.secret, params)
        res = requests.get(BASE_URL, params=params)
        return json.loads(res.content)


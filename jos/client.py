import requests

import json

from .utils import sign, gen_timestamp


__all__ = ('JDClient',)


class JDClient(object):
    """Jingdong API Client"""

    BASE_URL = 'http://gw.api.360buy.com/routerjson'

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def call(self, method, app_params=None):
        """Call specific method to fetch data returned by API.

        :param method: the method to be called.
        :param app_params: application parameters which are required
                           to call the specific method.
        """
        params = {
            'method': method,
            'app_key': self.key,
            'timestamp': gen_timestamp(),
            'v': '2.0',
            '360buy_param_json': json.dumps(app_params),
        }
        params['sign'] = sign(self.secret, params)
        res = requests.get(self.BASE_URL, params=params)
        res.raise_for_status()
        return json.loads(res.content, strict=False)

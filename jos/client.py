import json

import requests

from .utils import sign, gen_timestamp


__all__ = ('JDClient',)


class JDClient(object):
    """Jingdong API Client"""

    BASE_URL = 'https://api.jd.com/routerjson'

    def __init__(self, key, secret, token=None):
        self.key = key
        self.secret = secret
        self.token = token

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
        if self.token is not None:
            params['access_token'] = self.token
        params['sign'] = sign(self.secret, params)
        res = requests.get(self.BASE_URL, params=params)
        res.raise_for_status()
        return json.loads(res.content, strict=False)

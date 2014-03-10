JOS Python SDK
==============

JOS is an unofficial Jingdong open service Python SDK


Installation
------------

You can install jos with pip::

    $ pip install jos

Or, with setuptools easy_install in case you didn't have pip::

    $ easy_install jos


Usage
-----
::

    from jos.client import JDClient

    client = JDClient(key='your_api_key', secret='your_api_secret')

    method = 'jingdong.ware.product.detail.search.list.get'
    params = {
        'skuId': '123456',
        'isLoadWareScore': False,
        'client': 'm',
    }

    res = client.call(method, params)

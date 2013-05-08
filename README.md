JOS Python SDK
==============

unofficial Jingdong open service Python SDK

### 使用说明

目前只实现了`面向用户服务`的接口，具体接口就参阅<http://help.jd.com/jos>

    from jos import JOS
    
    client = JOS()
    res = client.get('jingdong.ware.get', {'ware_id': 863393, 'region_id': 1})

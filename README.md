```
________    _________   _____    _________
\______ \  /   _____/  /     \  /   _____/
 |    |  \ \_____  \  /  \ /  \ \_____  \
 |    `   \/        \/    Y    \/        \
/_________/_________/_____|____/_________/
 Dead      Simple    Monitoring Solution
```

DSMS
====
This is is a small project i developed to monitor some servers at my drom.  

Why
---
You go out on weekend and in some spare time you check the server, because you rebooted them earlier that day.  
While you are checking you notice that some services aren't up.  
So you are sitting in a bar an fix that stuff.

Wouldn't it be great if you have been notified ealier?

How
---
DSMS uses HTTP to comunicate with nodes.
 1. you can define the nodes on an master and check there endpoints with all the config stored on the master  
 2. you can define the nodes and only check the ```health``` endpoint while defining the config just on the node itself
 3. you can chain nodes to gain an tree by checking the ```all``` endpoint
 
Config
------
The config is a Json File located at ```/etc/dsms/dsms.json``` or given by an argument.
(see [dsms_dis.json](./dsms_dist.json))

Own Endpoint
------------
The endpoints are just python files located at [modules](./dsmsMods/modules).  
The config for an endpoint will be submitted within the query.  
A basic endpoint accepts a ```string``` representing the given config (In my cases a JSON String),
but the string could also be empty when there is no query arg.
And the endpoint will return a dictionary containing an ```ok``` boolean and the ```endpoint```.

Example:
```python
import json


def handle(config):
    conf = json.loads(config)
    res = {'ok': True, 'pong': 'pong', 'endpoint': 'ping'}
    if conf is not None and "pong" in conf:
        res['pong'] = conf['pong']
    return res
```

TODO
----
* Endpoints
    - [ ] md Softraid Endpoint Replaced By arcconf
    - [x] arcconf Raid
    
* Server
    - [x] fix query arg (useing q as query arg)
    - [ ] harden (hardened host creation, by returning None)
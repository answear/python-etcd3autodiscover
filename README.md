python-etcd3autodiscover
========================

Wrapper around python-etcd3 to support DNS SRV discovery of endpoints 

Usage
=====

Assume you have SRV record `_etcd._tcp.svc.internal` defined as:

```
Server:		127.0.0.1
Address:	127.0.0.1#53

_etcd._tcp.svc.internal	service = 0 0 2379 etcd0.internal.
_etcd._tcp.svc.internal	service = 0 0 2379 etcd1.internal.
_etcd._tcp.svc.internal	service = 0 0 2379 etcd2.internal.
```

```
from etc3autodiscover import Etcd3Autodiscover

etcd = Etcd3Autodiscover(host='svc.internal', port=2379, timeout=5)
client = etcd.connect()

if client is None:
	print(etcd.errstr())
else:
	client.put('/key', 'val')
	print(client.get('/key'))
```

python-etcd3autodiscover
========================

Wrapper around python-etcd3 to support DNS SRV discovery of endpoints 

Usage
=====

```
from etc3autodiscover import Etcd3Autodiscover

etcd = Etcd3Autodiscover(host='etcd.svc.internal', port=2379, timeout=5)
client = etcd.connect()

if client is None:
	print(etcd.errstr())
else:
	client.put('/key', 'val')
	print(client.get('/key'))
```

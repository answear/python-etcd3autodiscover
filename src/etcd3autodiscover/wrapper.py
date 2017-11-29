import sys
from etcd3 import Etcd3Client
import dns.resolver
from socket import gethostbyname
from time import time, sleep
from collections import namedtuple

class Etcd3Autodiscover(object):
    def __init__(self, host='localhost', port=2379,
                 ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
                 user=None, password=None):
        self.SRV = namedtuple('SRV', ['host', 'port', 'priority', 'weight'])
        self._endpoints = self._discover(host)
        self._etcd = None
        self._error = None

        self.host = host
        self.port = port
        self.ca_cert = ca_cert
        self.cert_key = cert_key
        self.cert_cert = cert_cert
        self.timeout = timeout
        self.user = user
        self.password = password

    def connect(self):
        endpoints = []
        if len(self._endpoints) == 0:
            endpoints.append(
                    self.SRV(self.host, self.port, 0, 0)
            )
        else:
            endpoints = self._endpoints
        
        for endpoint in endpoints:
            host = gethostbyname(endpoint[0])
            port = endpoint[1]
            try:
                self._etcd = Etcd3Client(host, port,
                                 self.ca_cert, self.cert_key, self.cert_cert,
                                 self.timeout,
                                 self.user, self.password)
                with self._etcd.lock('health.lock') as lock:
                    self._etcd.put('/health', str(time()))
                lock.release()
            except Exception as e:
                self._error = str(e)
                self._etcd = None
            break
        return self._etcd

    def _discover(self, domain):
        hosts = []
        fqdn = "_etcd._tcp.{}".format(domain)
        try:
            answer = dns.resolver.query(fqdn, 'SRV')
            for resource in answer:
                target = resource.target.to_text(omit_final_dot=True)
                hosts.append(
                    self.SRV(target, resource.port, resource.priority, resource.weight)
                )
            results = tuple(hosts)
        except dns.resolver.NXDOMAIN as e:
            return hosts
        return sorted(results, key=lambda r: (r.priority, -r.weight, r.host))

    def errstr(self):
        return self._error

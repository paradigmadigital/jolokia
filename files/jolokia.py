#!/usr/bin/env python2

from pyjolokia import Jolokia

j4p = Jolokia('http://localhost:8080/jolokia/')
data = j4p.request(type = 'read', mbean='java.lang:type=Memory', attribute='HeapMemoryUsage')
used = data['value']['used'] / 1024 / 1024
max = data['value']['max']

print used, max/1024/1024

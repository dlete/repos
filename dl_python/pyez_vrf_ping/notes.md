# In this directory

Script to ping IPv4/IPv6 addresses in a VRF

## Directories

* `archive`, old working copies of the scripts. They work, but will have functionalities in different stages of implementation, less features, less robust, etc. They do work though, they were production versions at the time.
* `development`, work in progress. Anything in this directory is not production. Do not consider robust, or finished.
* `production`, use it in production. At this point in time, as good as it gets. Consider finished product, robust.
* `sandbox`, rough and ready, by no means production. Test and discard. Do not even consider.

## Bugs

## How to

### execute

Invoke as:

```bash
python icinga_junos_vrf_ping.py \
    -H dist2-testlab.nn.hea.net \
    -u heanet -p '$!3u$uxqDMTXzw9' \
    -f lab_l3vpn_monitor \
    -l 10.11.12.13 10.11.12.13 10.11.12.13 10.11.12.13 fd00:10:11:12::13 13.13.13.13 \
    -d

Invoke as:
python icinga_junos_vrf_ping.py \
    -H dist1-testlab.nn.hea.net \
    -u heanet -p '$!3u$uxqDMTXzw9' \
    -f monitoring.2020081013 \
    -l 87.44.68.38 87.44.68.42 87.44.68.46 2001:0770:0100:6836::2 2001:0770:0100:6840::2 2001:0770:0100:6844::2 \
    -d

Invoke as:
python production/icinga_junos_vrf_ping.py \
    -H dist2-testlab.nn.hea.net \
    -u heanet -p '$!3u$uxqDMTXzw9' \
    -f testlab.2020081013 \
    -l 87.44.68.38 87.44.68.42 87.44.68.46 2001:0770:0100:6836::2 2001:0770:0100:6840::2 2001:0770:0100:6844::2 \
    -d
```

### data plane

Execute from `dist1-testlab.nn.hea.net` in configuration mode

```bash
# loopback to loopback from CE2 to CEx, ipv4 -> MUST PASS
run ping 10.10.12.1 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 10.10.13.1 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 10.10.14.1 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid

# loopback to loopback from CE3 to CEx, ipv4 -> MUST PASS
run ping 10.10.12.1 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid
run ping 10.10.13.1 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid
run ping 10.10.14.1 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid

# loopback to loopback from CE4 to CEx, ipv4 -> MUST PASS
run ping 10.10.12.1 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid
run ping 10.10.13.1 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid
run ping 10.10.14.1 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid


# loopback to loopback from CE2 to CEx, ipv6 -> MUST PASS
run ping fd00:10:10:12::1 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping fd00:10:10:13::1 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping fd00:10:10:14::1 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid

# loopback to loopback from CE3 to CEx, ipv6 -> MUST PASS
run ping fd00:10:10:12::1 source fd00:10:10:13::1 logical-system test-l3vpn-ce3 count 3 rapid
run ping fd00:10:10:13::1 source fd00:10:10:13::1 logical-system test-l3vpn-ce3 count 3 rapid
run ping fd00:10:10:14::1 source fd00:10:10:13::1 logical-system test-l3vpn-ce3 count 3 rapid

# loopback to loopback from CE4 to CEx, ipv6 -> MUST PASS
run ping fd00:10:10:12::1 source fd00:10:10:14::1 logical-system test-l3vpn-ce4 count 3 rapid
run ping fd00:10:10:13::1 source fd00:10:10:14::1 logical-system test-l3vpn-ce4 count 3 rapid
run ping fd00:10:10:14::1 source fd00:10:10:14::1 logical-system test-l3vpn-ce4 count 3 rapid


# loopback to CE end of UNI, from CE2 to CEx, ipv4 -> MUST PASS
run ping 87.44.68.38 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 87.44.68.42 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 87.44.68.46 source 10.10.12.1 logical-system test-l3vpn-ce2 count 3 rapid

# loopback to CE end of UNI, from CE3 to CEx, ipv4 -> MUST PASS
run ping 87.44.68.38 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid
run ping 87.44.68.42 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid
run ping 87.44.68.46 source 10.10.13.1 logical-system test-l3vpn-ce3 count 3 rapid

# loopback to CE end of UNI, from CE4 to CEx, ipv4 -> MUST PASS
run ping 87.44.68.38 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid
run ping 87.44.68.42 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid
run ping 87.44.68.46 source 10.10.14.1 logical-system test-l3vpn-ce4 count 3 rapid


# loopback to CE end of UNI, from CE2 to CEx, ipv6 -> MUST PASS
run ping 2001:0770:0100:6836::2 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6840::2 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6844::2 source fd00:10:10:12::1 logical-system test-l3vpn-ce2 count 3 rapid

# loopback to CE end of UNI, from CE3 to CEx, ipv6 -> MUST PASS
run ping 2001:0770:0100:6836::2 source fd00:10:10:13::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6840::2 source fd00:10:10:13::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6844::2 source fd00:10:10:13::1 logical-system test-l3vpn-ce2 count 3 rapid

# loopback to CE end of UNI, from CE4 to CEx, ipv6 -> MUST PASS
run ping 2001:0770:0100:6836::2 source fd00:10:10:14::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6840::2 source fd00:10:10:14::1 logical-system test-l3vpn-ce2 count 3 rapid
run ping 2001:0770:0100:6844::2 source fd00:10:10:14::1 logical-system test-l3vpn-ce2 count 3 rapid


# dist1-testlab, from Monitoring PE1 to CE loopback
# -> FAILS if not import loopacks
run ping 10.10.12.1 routing-instance test_monitoring count 3 rapid
run ping 10.10.13.1 routing-instance test_monitoring count 3 rapid
run ping 10.10.14.1 routing-instance test_monitoring count 3 rapid
# -> FAILS if not import loopacks
run ping 10.10.12.1 routing-instance monitoring.2020081013 count 3 rapid
run ping 10.10.13.1 routing-instance monitoring.2020081013 count 3 rapid
run ping 10.10.14.1 routing-instance monitoring.2020081013 count 3 rapid


# dist1-testlab, Monitoring to CE-PE link -> MUST PASS
run ping routing-instance monitoring.2020081013 87.44.68.38 count 3 rapid
run ping routing-instance monitoring.2020081013 87.44.68.42 count 3 rapid
run ping routing-instance monitoring.2020081013 87.44.68.46 count 3 rapid

run ping routing-instance test_monitoring 87.44.68.38 count 3 rapid
run ping routing-instance test_monitoring 87.44.68.42 count 3 rapid
run ping routing-instance test_monitoring 87.44.68.46 count 3 rapid


# edge4-testlab, Monitoring to CE-PE link -> MUST PASS
run ping routing-instance monitoring.2020081013 87.44.68.38 count 3 rapid
run ping routing-instance monitoring.2020081013 87.44.68.42 count 3 rapid
run ping routing-instance monitoring.2020081013 87.44.68.46 count 3 rapid


# dist2-teslab, testlab vrf to CE-PE link -> MUST PASS
run ping routing-instance testlab.2020081013 87.44.68.38 count 3 rapid
run ping routing-instance testlab.2020081013 87.44.68.42 count 3 rapid
run ping routing-instance testlab.2020081013 87.44.68.46 count 3 rapid

# dist2-teslab, Monitoring to CE-PE link -> MUST PASS
run ping routing-instance test_monitoring 87.44.68.38 count 3 rapid
run ping routing-instance test_monitoring 87.44.68.42 count 3 rapid
run ping routing-instance test_monitoring 87.44.68.46 count 3 rapid
```

### IPv4 and IPv4 UNI allocation, resource tables

In Technical Services -> Production Services -> Networks -> RMAN Project Doc Store -> Design Planning

### Compile Python module

See the question in Stackoverflow: [how to compile python script](https://stackoverflow.com/questions/52478939/how-to-compile-python-program-convert-to-pyc-in-python3)

```bash
import py_compile
py_compile.compile("file.py")
```

and then Python3 creates the file "file.pyc" in a folder named __pycache__ inside the same directory.

## Monitoring options

* one ip
* list of ip, sequential
* list of ip, parallel
* probe with physical interface in pe, uni exported to each vpn, import all vpn
* probe with phy if in pe, 1 uni per vpn
* prove with phy if in pe, 1 dedicated loopback in each ce; either of approaches above

### Explore

* Parallel execution of open device and ping one single device. Will open as many devices/netconf to the same router as IP are to be pinged. This may overload the router; say we have to ping 79 IP, that means to log into the router 79 times simultaneously.
* Open one device and then parallel execution of ping command. Does not work, gives this error.

### Export

export policy when created in CSD

1) several community adds -> BUG, only adds one community
2) several terms -> "BUG? Import/Export RT Policy should be specified for all the devices or none of the devices"
3) community with various members -> cannot delete members of a community in CSD
4) several chained export policies -> cannot delete policies in CSD (does not have the functionality)

### Performance

```bash
hosts sequential parallel CPU
10  12.02   15.68   8
20  20.13   24.35   8
30  28.31   30.48   8
40  36.41   37.96   8
50  46.54   45.07   8
60  58.16   57.58   4
80  88.69   68.97   6
80  89.94   67.27   8
100 87.30   94.90   8
100 86.26   82.53   8
```

## how failure looks like

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$ python checks_vrf.py
{'packet-size': [{'data': '56'}],
 'ping-failure': [{'data': 'no response'}],
 'probe-results-summary': [{'packet-loss': [{'data': '100'}],
                            'probes-sent': [{'data': '1'}],
                            'responses-received': [{'data': '0'}]}],
 'rpc-error': [{'error-message': [{'data': 'sendto: No route to host'}],
                'error-severity': [{'data': 'warning'}],
                'source-daemon': [{'data': 'ping'}]}],
 'target-host': [{'data': '1.1.1.1'}],
 'target-ip': [{'data': '1.1.1.1'}]}
Time to execute the script, begin to end: 15.21 seconds
FAILURE
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$
```

## how success looks like

```bash
dlete@TICTAC:/workspace/sandbox_pyez$ source .venv/bin/activate
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$ python checks_vrf.py
{'packet-size': [{'data': '56'}],
 'ping-success': [{'data': [None]}],
 'probe-result': [{'attributes': {'date-determined': '1595001015'},
                   'ip-address': [{'data': 'fd00:10:11:12::13'}],
                   'probe-index': [{'data': '1'}],
                   'probe-success': [{'data': [None]}],
                   'response-size': [{'data': '16'}],
                   'rtt': [{'data': '2080'}],
                   'sequence-number': [{'data': '0'}],
                   'time-to-live': [{'data': '64'}]}],
 'probe-results-summary': [{'packet-loss': [{'data': '0'}],
                            'probes-sent': [{'data': '1'}],
                            'responses-received': [{'data': '1'}],
                            'rtt-average': [{'data': '2080'}],
                            'rtt-maximum': [{'data': '2080'}],
                            'rtt-minimum': [{'data': '2080'}],
                            'rtt-stddev': [{'data': '0'}]}],
 'source': [{'data': 'fd00:10:11:12::13'}],
 'target-host': [{'data': 'fd00:10:11:12::13'}],
 'target-ip': [{'data': 'fd00:10:11:12::13'}]}
Time to execute the script, begin to end: 6.40 seconds
SUCCESS
(.venv) dlete@TICTAC:/workspace/sandbox_pyez$
```

## References

[PyEz examples from vnitinv](https://github.com/vnitinv/pyez-examples)

```bash
Traceback (most recent call last):
  File "checks_vrf_list_v0.2.py", line 224, in <module>
    outcome = ping_vrf(ne, os_username, os_password, vrf, hosts, 'DEBUG')
  File "checks_vrf_list_v0.2.py", line 165, in ping_vrf
    results = [pool.apply(global_my_time, args=(dev, host)) for host in hosts]
  File "checks_vrf_list_v0.2.py", line 165, in <listcomp>
    results = [pool.apply(global_my_time, args=(dev, host)) for host in hosts]
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 259, in apply
    return self.apply_async(func, args, kwds).get()
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 644, in get
    raise self._value
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 424, in _handle_tasks
    put(task)
  File "/usr/lib/python3.6/multiprocessing/connection.py", line 206, in send
    self._send_bytes(_ForkingPickler.dumps(obj))
  File "/usr/lib/python3.6/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
  File "/workspace/sandbox/.venv/lib/python3.6/site-packages/ncclient/manager.py", line 270, in _missing
    root = new_ele(m)
  File "/workspace/sandbox/.venv/lib/python3.6/site-packages/ncclient/xml_.py", line 227, in <lambda>
    new_ele = lambda tag, attrs={}, **extra: etree.Element(qualify(tag), attrs, **extra)
  File "src/lxml/etree.pyx", line 3022, in lxml.etree.Element
  File "src/lxml/apihelpers.pxi", line 101, in lxml.etree._makeElement
  File "src/lxml/apihelpers.pxi", line 1734, in lxml.etree._tagValidOrRaise
ValueError: Invalid tag name '--getstate--'
(.venv) dlete@CALCULUS:/workspace/sandbox/sandbox_pyez$
```

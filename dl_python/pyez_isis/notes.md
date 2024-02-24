# In this directory

Script to check the IS-IS consistency between the router configurtion and the live state

## About the script

JUNOS does not report and IS-IS adjacency as down. If that is the state, is just does not appear in the output of the command 'show isis adjacency'. Hence, you must delve into the output of 'show isis interfaces detail' to find out if the interface is/how configured for IS-IS and reconcile with the number of adjancencies seen, or whether the interface is passive.

## Directories

* `archive`, old working copies of the scripts. They work, but will have functionalities in different stages of implementation, less features, less robust, etc. They do work though, they were production versions at the time.
* `development`, work in progress. Anything in this directory is not production. Do not consider robust, or finished.
* `production`, use it in production. At this point in time, as good as it gets. Consider finished product, robust.
* `sandbox`, rough and ready, by no means production. Test and discard. Do not even consider.

## Execute, how to

Check the modules themselves, they will instruct you how to execute.

## RPC commands

### `show isis adjacency extensive | display xml rpc`

```bash
heanet@edge3-testlab> show isis adjacency extensive | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.4R2/junos">
    <rpc>
        <get-isis-adjacency-information>
                <verbosity_level>extensive</verbosity_level>
        </get-isis-adjacency-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>

heanet@edge3-testlab>
```

## Outputs

### raw output IS-IS interface, extensive=False and NO instance

```bash
logger.debug("Will now issue command 'show isis interface extensive'")
        isis_interfaces = (dev.rpc.
                           get_isis_interface_information({'format': 'json'},
                                                        extensive=False))
```

This is what `isis_interfaces` looks like

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ python checks_junos_isis.py 
2021-03-30 11:02:58,215: check_junos_isis_adjacencies: line: 162: DEBUG: Time to open Netconf session with dist1-testlab.nn.hea.net on 87.44.48.99: 2.59 seconds
2021-03-30 11:02:58,215: check_junos_isis_adjacencies: line: 185: DEBUG: Will now issue command 'show isis interface extensive'
isis instance is NOT defined
2021-03-30 11:03:01,629: check_junos_isis_adjacencies: line: 193: DEBUG: Time to retrieve IS-IS interfaces in dist1-testlab.nn.hea.net on 87.44.48.99: 3.41 seconds
{'isis-interface-information': [{'isis-interface': [{'attributes': {'heading': 'IS-IS '
                                                                               'interface '
                                                                               'database:'},
                                                     'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'interface-name': [{'data': 'lo0.0'}],
                                                     'isis-interface-state-one': [{'data': 'Passive'}],
                                                     'isis-interface-state-two': [{'data': 'Passive'}],
                                                     'metric-one': [{'data': '0'}],
                                                     'metric-two': [{'data': '0'}]},
                                                    {'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'interface-name': [{'data': 'xe-0/0/0.0'}],
                                                     'isis-interface-state-one': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'isis-interface-state-two': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'metric-one': [{'data': '100'}],
                                                     'metric-two': [{'data': '100'}]},
                                                    {'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'interface-name': [{'data': 'xe-0/1/0.0'}],
                                                     'isis-interface-state-one': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'isis-interface-state-two': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'metric-one': [{'data': '100'}],
                                                     'metric-two': [{'data': '100'}]},
                                                    {'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'interface-name': [{'data': 'xe-2/0/0.0'}],
                                                     'isis-interface-state-one': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'isis-interface-state-two': [{'data': 'Point '
                                                                                           'to '
                                                                                           'Point'}],
                                                     'metric-one': [{'data': '100'}],
                                                     'metric-two': [{'data': '100'}]}]}]}
outcome is of type: <class 'dict'>
None
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ 
```

### raw output IS-IS interface, extensive=True and NO instance

```bash
logger.debug("Will now issue command 'show isis interface extensive'")
        isis_interfaces = (dev.rpc.
                           get_isis_interface_information({'format': 'json'},
                                                        extensive=True))
```

This is what `isis_interfaces` looks like

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ python checks_junos_isis.py 
2021-03-30 11:06:30,093: check_junos_isis_adjacencies: line: 162: DEBUG: Time to open Netconf session with dist1-testlab.nn.hea.net on 87.44.48.99: 3.19 seconds
2021-03-30 11:06:30,094: check_junos_isis_adjacencies: line: 185: DEBUG: Will now issue command 'show isis interface extensive'
isis instance is NOT defined
2021-03-30 11:06:32,908: check_junos_isis_adjacencies: line: 193: DEBUG: Time to retrieve IS-IS interfaces in dist1-testlab.nn.hea.net on 87.44.48.99: 2.81 seconds
{'isis-interface-information': [{'isis-interface': [{'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'attributes': {'heading': 'IS-IS '
                                                                               'interface '
                                                                               'database:'},
                                                     'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'hello-padding': [{'data': 'Loose'}],
                                                     'interface-group-holddown-delay': [{'data': '20'}],
                                                     'interface-group-holddown-left': [{'data': '0'}],
                                                     'interface-index': [{'data': '322'}],
                                                     'interface-level-data': [{'adjacency-count': [{'data': '0'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '1'}],
                                                                               'metric': [{'data': '0'}],
                                                                               'passive': [{'data': 'Passive'}]},
                                                                              {'adjacency-count': [{'data': '0'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '2'}],
                                                                               'metric': [{'data': '0'}],
                                                                               'passive': [{'data': 'Passive'}]}],
                                                     'interface-name': [{'data': 'lo0.0'}],
                                                     'interface-state-value': [{'data': '0x6'}],
                                                     'isis-layer2-map-enabled': [{'data': 'Disabled'}],
                                                     'lsp-interval': [{'data': '100'}],
                                                     'max-hello-size': [{'data': '1492'}]},
                                                    {'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'csnp-interval': [{'data': '15'}],
                                                     'hello-padding': [{'data': 'Loose'}],
                                                     'interface-group-holddown-delay': [{'data': '20'}],
                                                     'interface-group-holddown-left': [{'data': '0'}],
                                                     'interface-index': [{'data': '350'}],
                                                     'interface-level-data': [{'adjacency-count': [{'data': '1'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '1'}],
                                                                               'metric': [{'data': '63'}]},
                                                                              {'adjacency-count': [{'data': '0'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '2'}],
                                                                               'metric': [{'data': '100'}]}],
                                                     'interface-name': [{'data': 'xe-0/0/0.0'}],
                                                     'interface-state-value': [{'data': '0x6'}],
                                                     'isis-layer2-map-enabled': [{'data': 'Disabled'}],
                                                     'lsp-interval': [{'data': '100'}],
                                                     'max-hello-size': [{'data': '1492'}]},
                                                    {'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'csnp-interval': [{'data': '15'}],
                                                     'hello-padding': [{'data': 'Loose'}],
                                                     'interface-group-holddown-delay': [{'data': '20'}],
                                                     'interface-group-holddown-left': [{'data': '0'}],
                                                     'interface-index': [{'data': '351'}],
                                                     'interface-level-data': [{'adjacency-count': [{'data': '1'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '1'}],
                                                                               'metric': [{'data': '63'}]},
                                                                              {'adjacency-count': [{'data': '0'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '2'}],
                                                                               'metric': [{'data': '100'}]}],
                                                     'interface-name': [{'data': 'xe-0/1/0.0'}],
                                                     'interface-protection-type': [{'data': 'Node '
                                                                                            'Link'}],
                                                     'interface-state-value': [{'data': '0x6'}],
                                                     'isis-layer2-map-enabled': [{'data': 'Disabled'}],
                                                     'lsp-interval': [{'data': '100'}],
                                                     'max-hello-size': [{'data': '1492'}]},
                                                    {'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'circuit-id': [{'data': '0x1'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'csnp-interval': [{'data': '15'}],
                                                     'hello-padding': [{'data': 'Loose'}],
                                                     'interface-group-holddown-delay': [{'data': '20'}],
                                                     'interface-group-holddown-left': [{'data': '0'}],
                                                     'interface-index': [{'data': '377'}],
                                                     'interface-level-data': [{'adjacency-count': [{'data': '1'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '1'}],
                                                                               'metric': [{'data': '63'}]},
                                                                              {'adjacency-count': [{'data': '0'}],
                                                                               'hello-time': [{'data': '9.000'}],
                                                                               'holdtime': [{'data': '27'}],
                                                                               'interface-priority': [{'data': '64'}],
                                                                               'level': [{'data': '2'}],
                                                                               'metric': [{'data': '100'}]}],
                                                     'interface-name': [{'data': 'xe-2/0/0.0'}],
                                                     'interface-protection-type': [{'data': 'Node '
                                                                                            'Link'}],
                                                     'interface-state-value': [{'data': '0x6'}],
                                                     'isis-layer2-map-enabled': [{'data': 'Disabled'}],
                                                     'lsp-interval': [{'data': '100'}],
                                                     'max-hello-size': [{'data': '1492'}]}]}]}
outcome is of type: <class 'dict'>
None
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ 
```

### raw output IS-IS adjacency, extensive=True and NO instance

```bash
logger.debug("Will now issue command 'show isis adjacencies extensive'")
        isis_adjacencies = (dev.rpc.
                           get_isis_adjacency_information({'format': 'json'},
                                                        extensive=True))
```

This is what `isis_adjacencies` looks like

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ python checks_junos_isis.py 
2021-03-30 10:42:20,454: check_junos_isis_adjacencies: line: 161: DEBUG: Time to open Netconf session with dist1-testlab.nn.hea.net on 87.44.48.99: 2.81 seconds
isis instance is NOT defined
2021-03-30 10:42:23,166: check_junos_isis_adjacencies: line: 190: DEBUG: Time to retrieve IS-IS adjacencies in dist1-testlab.nn.hea.net on 87.44.48.99: 2.71 seconds
{'isis-adjacency-information': [{'isis-adjacency': [{'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'adjacency-flag': [{'data': 'Speaks: '
                                                                                 'IP, '
                                                                                 'IPv6'}],
                                                     'adjacency-restart-capable': [{'data': 'yes'}],
                                                     'adjacency-state': [{'data': 'Up'}],
                                                     'adjacency-topologies': [{'data': 'Unicast'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'global-ipv6-address': [{'data': '2001:770:200:2004::'}],
                                                     'holdtime': [{'data': '23'}],
                                                     'interface-name': [{'data': 'xe-0/0/0.0'}],
                                                     'interface-priority': [{'data': '0'}],
                                                     'ip-address': [{'data': '87.44.51.7'}],
                                                     'ipv6-address': [{'data': 'fe80::3e8a:b0ff:fe88:50c8'}],
                                                     'isis-adjacency-log': [{'adjacency-event': [{'data': 'Seenself'}],
                                                                             'adjacency-state': [{'data': 'Up'}],
                                                                             'adjacency-when': [{'data': 'Sun '
                                                                                                         'Feb '
                                                                                                         '14 '
                                                                                                         '13:17:52'}]}],
                                                     'last-transition-time': [{'data': '6w1d '
                                                                                       '20:24:28'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'edge1-testlab'}],
                                                     'transition-count': [{'data': '1'}]},
                                                    {'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'adjacency-flag': [{'data': 'Speaks: '
                                                                                 'IP, '
                                                                                 'IPv6'}],
                                                     'adjacency-restart-capable': [{'data': 'yes'}],
                                                     'adjacency-state': [{'data': 'Up'}],
                                                     'adjacency-topologies': [{'data': 'Unicast'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'global-ipv6-address': [{'data': '2001:770:200:2004::2'},
                                                                             {'data': '2001:770:200:2005::2'}],
                                                     'holdtime': [{'data': '22'}],
                                                     'interface-name': [{'data': 'xe-0/1/0.0'}],
                                                     'interface-priority': [{'data': '0'}],
                                                     'ip-address': [{'data': '87.44.51.9'}],
                                                     'ipv6-address': [{'data': 'fe80::7ee2:caff:feff:da18'}],
                                                     'isis-adjacency-log': [{'adjacency-event': [{'data': 'Seenself'}],
                                                                             'adjacency-state': [{'data': 'Up'}],
                                                                             'adjacency-when': [{'data': 'Sun '
                                                                                                         'Feb '
                                                                                                         '14 '
                                                                                                         '13:18:18'}]}],
                                                     'last-transition-time': [{'data': '6w1d '
                                                                                       '20:24:02'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'dist2-testlab'}],
                                                     'transition-count': [{'data': '1'}]},
                                                    {'adjacency-advertisement': [{'data': 'advertise'}],
                                                     'adjacency-flag': [{'data': 'Speaks: '
                                                                                 'IP, '
                                                                                 'IPv6'}],
                                                     'adjacency-restart-capable': [{'data': 'yes'}],
                                                     'adjacency-state': [{'data': 'Up'}],
                                                     'adjacency-topologies': [{'data': 'Unicast'}],
                                                     'circuit-type': [{'data': '3'}],
                                                     'holdtime': [{'data': '25'}],
                                                     'interface-name': [{'data': 'xe-2/0/0.0'}],
                                                     'interface-priority': [{'data': '0'}],
                                                     'ip-address': [{'data': '87.44.51.11'}],
                                                     'ipv6-address': [{'data': 'fe80::ab2:58ff:feca:4e32'}],
                                                     'isis-adjacency-log': [{'adjacency-event': [{'data': 'Seenself'}],
                                                                             'adjacency-state': [{'data': 'Up'}],
                                                                             'adjacency-when': [{'data': 'Tue '
                                                                                                         'Feb '
                                                                                                         '16 '
                                                                                                         '01:29:13'}]}],
                                                     'last-transition-time': [{'data': '6w0d '
                                                                                       '08:13:07'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'edge4-testlab'}],
                                                     'transition-count': [{'data': '1'}]}]}]}
outcome is of type: <class 'dict'>
None
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$
```

### raw output IS-IS adjacencies, extensive=False and NO instance

```bash
logger.debug("Will now issue command 'show isis adjacencies extensive'")
        isis_adjacencies = (dev.rpc.
                           get_isis_adjacency_information({'format': 'json'},
                                                        extensive=False))
```

This is what `isis_adjacencies` looks like

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ python checks_junos_isis.py 
2021-03-30 10:48:59,538: check_junos_isis_adjacencies: line: 162: DEBUG: Time to open Netconf session with dist1-testlab.nn.hea.net on 87.44.48.99: 2.82 seconds
2021-03-30 10:48:59,538: check_junos_isis_adjacencies: line: 185: DEBUG: Will now issue command 'show isis adjacencies extensive'
isis instance is NOT defined
2021-03-30 10:49:04,153: check_junos_isis_adjacencies: line: 193: DEBUG: Time to retrieve IS-IS adjacencies in dist1-testlab.nn.hea.net on 87.44.48.99: 4.61 seconds
{'isis-adjacency-information': [{'isis-adjacency': [{'adjacency-state': [{'data': 'Up'}],
                                                     'holdtime': [{'data': '19'}],
                                                     'interface-name': [{'data': 'xe-0/0/0.0'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'edge1-testlab'}]},
                                                    {'adjacency-state': [{'data': 'Up'}],
                                                     'holdtime': [{'data': '25'}],
                                                     'interface-name': [{'data': 'xe-0/1/0.0'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'dist2-testlab'}]},
                                                    {'adjacency-state': [{'data': 'Up'}],
                                                     'holdtime': [{'data': '21'}],
                                                     'interface-name': [{'data': 'xe-2/0/0.0'}],
                                                     'level': [{'data': '1'}],
                                                     'system-name': [{'data': 'edge4-testlab'}]}]}]}
outcome is of type: <class 'dict'>
None
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_isis/development$ 
```

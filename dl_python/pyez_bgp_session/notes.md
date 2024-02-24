# In this directory

Script to check the BGP session with an IPv4/IPv6 peer in a VRF or the master/global tables

## Directories

* `archive`, old working copies of the scripts. They work, but will have functionalities in different stages of implementation, less features, less robust, etc. They do work though, they were production versions at the time.
* `development`, work in progress. Anything in this directory is not production. Do not consider robust, or finished.
* `production`, use it in production. At this point in time, as good as it gets. Consider finished product, robust.
* `sandbox`, rough and ready, by no means production. Test and discard. Do not even consider.

## Execute, how to

Check the modules themselves, they will instruct you how to execute.

## RPC commands

### `show bgp neighbor 87.44.48.5 | display xml rpc`

```bash
heanet@dist2-testlab> show bgp neighbor 87.44.48.5 | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/19.2R0/junos">
    <rpc>
        <get-bgp-neighbor-information>
                <neighbor-address>87.44.48.5</neighbor-address>
        </get-bgp-neighbor-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>

heanet@dist2-testlab>
```

### `show bgp neighbor 87.44.68.38 instance testlab.2020081013 | display xml rpc`

```bash
heanet@dist2-testlab> show bgp neighbor 87.44.68.38 instance testlab.2020081013 | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/19.2R0/junos">
    <rpc>
        <get-bgp-neighbor-information>
                <instance>testlab.2020081013</instance>
                <neighbor-address>87.44.68.38</neighbor-address>
        </get-bgp-neighbor-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>

heanet@dist2-testlab>
```

## Outputs

### raw output when the peer is in a vrf/routing-instance

```bash
logger.debug("Will now issue command 'show bgp neighbor {peer}'".format(peer=bgp_peer))
command_outcome = dev.rpc.get_bgp_neighbor_information({'format': 'json'}, instance=vrf, neighbor_address=bgp_peer)
```

This is what `command_outcome` looks like when the BGP peer is in a VRF

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_bgp_session$ python checks_junos_bgp_session.py 
2020-09-08 20:24:15,553: checks_junos_bgp_session: check_junos_bgp_session: 98: __main__: DEBUG: Time to open Netconf session with dist2-testlab.nn.hea.net: 1.86 seconds
2020-09-08 20:24:15,554: checks_junos_bgp_session: check_junos_bgp_session: 105: __main__: DEBUG: Will issue command show bgp neighbor for 87.44.68.38
{'bgp-information': [{'bgp-peer': [{'active-holdtime': [{'data': '90'}],
                                    'attributes': {'junos:style': 'detail'},
                                    'bgp-bfd': [{'bfd-configuration-state': [{'data': 'disabled'}],
                                                 'bfd-operational-state': [{'data': 'down'}]}],
                                    'bgp-error': [{'name': [{'data': 'Hold '
                                                                     'Timer '
                                                                     'Expired '
                                                                     'Error'}],
                                                   'receive-count': [{'data': '0'}],
                                                   'send-count': [{'data': '1'}]}],
                                    'bgp-option-information': [{'address-families': [{'data': 'inet-unicast'}],
                                                                'attributes': {'xmlns': 'http://xml.juniper.net/junos/19.2R0/junos-routing'},
                                                                'authentication-configured': [{'data': [None]}],
                                                                'bgp-options': [{'data': 'Preference '
                                                                                         'LocalAddress '
                                                                                         'AuthKey '
                                                                                         'AddressFamily '
                                                                                         'PeerAS '
                                                                                         'PrefixLimit '
                                                                                         'Refresh'}],
                                                                'bgp-options-extended': [{'data': 'GracefulShutdownRcv'}],
                                                                'bgp-options2': [{}],
                                                                'export-policy': [{'data': 'ACCEPT-ALL'}],
                                                                'gshut-recv-local-preference': [{'data': '0'}],
                                                                'holdtime': [{'data': '90'}],
                                                                'import-policy': [{'data': 'ACCEPT-ALL'}],
                                                                'local-address': [{'data': '87.44.68.37'}],
                                                                'preference': [{'data': '170'}],
                                                                'prefix-limit': [{'limit-action': [{'data': 'teardown'}],
                                                                                  'nlri-type': [{'data': 'inet-unicast'}],
                                                                                  'prefix-count': [{'data': '30'}]}]}],
                                    'bgp-output-queue': [{'count': [{'data': '0'}],
                                                          'number': [{'data': '13'}],
                                                          'rib-adv-nlri': [{'data': 'inet-unicast'}],
                                                          'table-name': [{'data': 'testlab.2020081013.inet.0'}]}],
                                    'bgp-peer-iosession': [{'iosession-state': [{'data': 'Enabled'}],
                                                            'iosession-thread-name': [{'data': 'bgpio-0'}]}],
                                    'bgp-rib': [{'accepted-prefix-count': [{'data': '1'}],
                                                 'active-prefix-count': [{'data': '1'}],
                                                 'advertised-prefix-count': [{'data': '9'}],
                                                 'attributes': {'junos:style': 'detail'},
                                                 'bgp-rib-state': [{'data': 'BGP '
                                                                            'restart '
                                                                            'is '
                                                                            'complete'}],
                                                 'name': [{'data': 'testlab.2020081013.inet.0'}],
                                                 'received-prefix-count': [{'data': '1'}],
                                                 'rib-bit': [{'data': 'e0000'}],
                                                 'send-state': [{'data': 'in '
                                                                         'sync'}],
                                                 'suppressed-prefix-count': [{'data': '0'}],
                                                 'vpn-rib-state': [{'data': 'VPN '
                                                                            'restart '
                                                                            'is '
                                                                            'complete'}]}],
                                    'flap-count': [{'data': '1'}],
                                    'group-index': [{'data': '2'}],
                                    'input-messages': [{'data': '3973'}],
                                    'input-octets': [{'data': '75530'}],
                                    'input-refreshes': [{'data': '0'}],
                                    'input-updates': [{'data': '2'}],
                                    'keepalive-interval': [{'data': '30'}],
                                    'last-checked': [{'data': '107581'}],
                                    'last-error': [{'data': 'Hold Timer '
                                                            'Expired Error'}],
                                    'last-event': [{'data': 'RecvKeepAlive'}],
                                    'last-flap-event': [{'data': 'HoldTime'}],
                                    'last-received': [{'data': '2'}],
                                    'last-sent': [{'data': '25'}],
                                    'last-state': [{'data': 'OpenConfirm'}],
                                    'local-address': [{'data': '87.44.68.37+60967'}],
                                    'local-as': [{'data': '1213'}],
                                    'local-id': [{'data': '87.44.68.37'}],
                                    'local-interface-index': [{'data': '702'}],
                                    'local-interface-name': [{'data': 'ge-0/2/7.512'}],
                                    'nlri-type-peer': [{'data': 'inet-unicast'}],
                                    'nlri-type-session': [{'data': 'inet-unicast'}],
                                    'output-messages': [{'data': '3929'}],
                                    'output-octets': [{'data': '74900'}],
                                    'output-refreshes': [{'data': '0'}],
                                    'output-updates': [{'data': '5'}],
                                    'peer-4byte-as-capability-advertised': [{'data': '65512'}],
                                    'peer-addpath-not-supported': [{'data': [None]}],
                                    'peer-address': [{'data': '87.44.68.38+179'}],
                                    'peer-as': [{'data': '65512'}],
                                    'peer-cfg-rti': [{'data': 'testlab.2020081013'}],
                                    'peer-end-of-rib-received': [{'data': 'inet-unicast'}],
                                    'peer-end-of-rib-scheduled': [{}],
                                    'peer-end-of-rib-sent': [{'data': 'inet-unicast'}],
                                    'peer-flags': [{'data': 'Sync '
                                                            'PeerIntfNoMpls'}],
                                    'peer-fwd-rti': [{'data': 'testlab.2020081013'}],
                                    'peer-group': [{'data': 'HEANET-V4'}],
                                    'peer-id': [{'data': '10.10.12.1'}],
                                    'peer-index': [{'data': '0'}],
                                    'peer-no-llgr-restarter': [{'data': [None]}],
                                    'peer-no-restart': [{'data': [None]}],
                                    'peer-refresh-capability': [{'data': '2'}],
                                    'peer-restart-flags-received': [{'data': 'Notification'}],
                                    'peer-restart-nlri-configured': [{'data': 'inet-unicast'}],
                                    'peer-restart-nlri-negotiated': [{'data': 'inet-unicast'}],
                                    'peer-stale-route-time-configured': [{'data': '300'}],
                                    'peer-state': [{'data': 'Established'}],
                                    'peer-type': [{'data': 'External'}],
                                    'snmp-index': [{'data': '4'}]}]}]}
2020-09-08 20:24:18,849: checks_junos_bgp_session: check_junos_bgp_session: 123: __main__: DEBUG: Time to execute JUNOS command: 3.30 seconds
2020-09-08 20:24:18,949: checks_junos_bgp_session: check_junos_bgp_session: 131: __main__: DEBUG: Time to execute the script, begin to end: 5.26 seconds
{}
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_bgp_session$ 
```

### raw output when the peer is in the master (`inet.0`or `inet6.0`) table

```bash
logger.debug("Will now issue command 'show bgp neighbor {peer}'".format(peer=bgp_peer))
command_outcome = dev.rpc.get_bgp_neighbor_information({'format': 'json'}, neighbor_address=bgp_peer)
# or this too!!!
command_outcome = dev.rpc.get_bgp_neighbor_information({'format': 'json'}, instance='master', neighbor_address=bgp_peer)
```

This is what `command_outcome` looks like when the BGP peer is in the `master` vrf

```bash
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_bgp_session$ python checks_junos_bgp_session.py 
2020-09-08 23:25:36,372: checks_junos_bgp_session: check_junos_bgp_session: 98: __main__: DEBUG: Time to open Netconf session with dist2-testlab.nn.hea.net: 1.67 seconds
2020-09-08 23:25:36,373: checks_junos_bgp_session: check_junos_bgp_session: 109: __main__: DEBUG: Will now issue command 'show bgp neighbor 2001:770:200::5 instance global' in dist2-testlab.nn.hea.net
{'bgp-information': [{'bgp-peer': [{'active-holdtime': [{'data': '90'}],
                                    'attributes': {'junos:style': 'detail'},
                                    'bgp-bfd': [{'bfd-configuration-state': [{'data': 'enabled'}],
                                                 'bfd-operational-state': [{'data': 'up'}]}],
                                    'bgp-option-information': [{'address-families': [{'data': 'inet6-unicast '
                                                                                              'inet6-flow'}],
                                                                'attributes': {'xmlns': 'http://xml.juniper.net/junos/19.2R0/junos-routing'},
                                                                'authentication-configured': [{'data': [None]}],
                                                                'bgp-options': [{'data': 'Preference '
                                                                                         'LocalAddress '
                                                                                         'AuthKey '
                                                                                         'LogUpDown '
                                                                                         'AddressFamily '
                                                                                         'LocalAS '
                                                                                         'Refresh'}],
                                                                'bgp-options-extended': [{'data': 'GracefulShutdownRcv'}],
                                                                'bgp-options2': [{'data': 'BfdEnabled'}],
                                                                'export-policy': [{'data': 'LOCAL-V6'}],
                                                                'gshut-recv-local-preference': [{'data': '0'}],
                                                                'holdtime': [{'data': '90'}],
                                                                'local-address': [{'data': '2001:770:200::100'}],
                                                                'local-as': [{'data': '1213'}],
                                                                'local-system-as': [{'data': '1213'}],
                                                                'preference': [{'data': '170'}]}],
                                    'bgp-output-queue': [{'count': [{'data': '0'}],
                                                          'number': [{'data': '11'}],
                                                          'rib-adv-nlri': [{'data': 'inet6-unicast'}],
                                                          'table-name': [{'data': 'inet6.0'}]},
                                                         {'count': [{'data': '0'}],
                                                          'number': [{'data': '12'}],
                                                          'rib-adv-nlri': [{'data': 'inet6-flow'}],
                                                          'table-name': [{'data': 'inet6flow.0'}]}],
                                    'bgp-peer-iosession': [{'iosession-state': [{'data': 'Enabled'}],
                                                            'iosession-thread-name': [{'data': 'bgpio-0'}]}],
                                    'bgp-rib': [{'accepted-prefix-count': [{'data': '193'}],
                                                 'active-prefix-count': [{'data': '191'}],
                                                 'advertised-prefix-count': [{'data': '2'}],
                                                 'attributes': {'junos:style': 'detail'},
                                                 'bgp-rib-state': [{'data': 'BGP '
                                                                            'restart '
                                                                            'is '
                                                                            'complete'}],
                                                 'name': [{'data': 'inet6.0'}],
                                                 'received-prefix-count': [{'data': '193'}],
                                                 'rib-bit': [{'data': 'c0000'}],
                                                 'send-state': [{'data': 'in '
                                                                         'sync'}],
                                                 'suppressed-prefix-count': [{'data': '0'}]},
                                                {'accepted-prefix-count': [{'data': '0'}],
                                                 'active-prefix-count': [{'data': '0'}],
                                                 'advertised-prefix-count': [{'data': '0'}],
                                                 'attributes': {'junos:style': 'detail'},
                                                 'bgp-rib-state': [{'data': 'BGP '
                                                                            'restart '
                                                                            'is '
                                                                            'complete'}],
                                                 'name': [{'data': 'inet6flow.0'}],
                                                 'received-prefix-count': [{'data': '0'}],
                                                 'rib-bit': [{'data': 'd0000'}],
                                                 'send-state': [{'data': 'in '
                                                                         'sync'}],
                                                 'suppressed-prefix-count': [{'data': '0'}]}],
                                    'flap-count': [{'data': '0'}],
                                    'group-index': [{'data': '1'}],
                                    'input-messages': [{'data': '21297'}],
                                    'input-octets': [{'data': '413496'}],
                                    'input-refreshes': [{'data': '0'}],
                                    'input-updates': [{'data': '100'}],
                                    'keepalive-interval': [{'data': '30'}],
                                    'last-checked': [{'data': '623948'}],
                                    'last-error': [{'data': 'None'}],
                                    'last-event': [{'data': 'RecvKeepAlive'}],
                                    'last-received': [{'data': '6'}],
                                    'last-sent': [{'data': '16'}],
                                    'last-state': [{'data': 'OpenConfirm'}],
                                    'local-address': [{'data': '2001:770:200::100+58005'}],
                                    'local-as': [{'data': '1213'}],
                                    'local-ext-nh-color-nlri': [{'data': 'inet6-unicast'}],
                                    'local-id': [{'data': '87.44.48.100'}],
                                    'nlri-type-peer': [{'data': 'inet6-unicast '
                                                                'inet6-flow'}],
                                    'nlri-type-session': [{'data': 'inet6-unicast '
                                                                   'inet6-flow'}],
                                    'output-messages': [{'data': '22756'}],
                                    'output-octets': [{'data': '432447'}],
                                    'output-refreshes': [{'data': '0'}],
                                    'output-updates': [{'data': '1'}],
                                    'peer-4byte-as-capability-advertised': [{'data': '1213'}],
                                    'peer-addpath-not-supported': [{'data': [None]}],
                                    'peer-address': [{'data': '2001:770:200::5+179'}],
                                    'peer-as': [{'data': '1213'}],
                                    'peer-cfg-rti': [{'data': 'master'}],
                                    'peer-end-of-rib-received': [{'data': 'inet6-unicast '
                                                                          'inet6-flow'}],
                                    'peer-end-of-rib-scheduled': [{}],
                                    'peer-end-of-rib-sent': [{'data': 'inet6-unicast '
                                                                      'inet6-flow'}],
                                    'peer-flags': [{'data': 'Sync'}],
                                    'peer-fwd-rti': [{'data': 'master'}],
                                    'peer-group': [{'data': 'ibgp-rr-v6'}],
                                    'peer-id': [{'data': '87.44.48.5'}],
                                    'peer-index': [{'data': '1'}],
                                    'peer-no-llgr-restarter': [{'data': [None]}],
                                    'peer-no-restart': [{'data': [None]}],
                                    'peer-refresh-capability': [{'data': '2'}],
                                    'peer-restart-flags-received': [{'data': 'Notification'}],
                                    'peer-restart-nlri-configured': [{'data': 'inet6-unicast '
                                                                              'inet6-flow'}],
                                    'peer-restart-nlri-negotiated': [{'data': 'inet6-unicast '
                                                                              'inet6-flow'}],
                                    'peer-stale-route-time-configured': [{'data': '300'}],
                                    'peer-state': [{'data': 'Established'}],
                                    'peer-type': [{'data': 'Internal'}],
                                    'snmp-index': [{'data': '3'}]}]}]}
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 133: __main__: DEBUG: BGP peer 2001:770:200::5, is in state: Established
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 141: __main__: DEBUG: BGP peer 2001:770:200::5, received prefix(es): 193
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 145: __main__: DEBUG: BGP peer 2001:770:200::5, accepted prefix(es): 193
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 149: __main__: DEBUG: BGP peer 2001:770:200::5, active prefix(es): 191
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 153: __main__: DEBUG: BGP peer 2001:770:200::5, advertised prefix(es): 2
2020-09-08 23:25:39,008: checks_junos_bgp_session: check_junos_bgp_session: 159: __main__: DEBUG: Time to execute JUNOS command: 2.64 seconds
2020-09-08 23:25:39,118: checks_junos_bgp_session: check_junos_bgp_session: 169: __main__: DEBUG: Time to execute the script, begin to end: 4.42 seconds
{'2001:770:200::5': {'peer_address': '2001:770:200::5', 'state': 'Established', 'received_prefix_count': '193', 'accepted_prefix_count': '193', 'active_prefix_count': '191', 'advertised_prefix_count': '2'}}
{'peer_address': '2001:770:200::5', 'state': 'Established', 'received_prefix_count': '193', 'accepted_prefix_count': '193', 'active_prefix_count': '191', 'advertised_prefix_count': '2'}
2001:770:200::5
{'peer_address': '2001:770:200::5', 'state': 'Established', 'received_prefix_count': '193', 'accepted_prefix_count': '193', 'active_prefix_count': '191', 'advertised_prefix_count': '2'}
(.venv) dlete@TICTAC:/workspace/sandbox_dl/pyez_bgp_session$ 
```

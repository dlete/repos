#### how failure looks like

`
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
`


#### how success looks like
`
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
`


### References

[PyEz examples from vnitinv](https://github.com/vnitinv/pyez-examples)
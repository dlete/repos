#!/usr/bin/env python3

def ping_vrf(ne, os_username, os_password, vrf, host):
    ''' Return success/failure for pinging a L3VPN host from within a vrf of a given NE

    This function logs into a router and issues a ping from within a vrf. It returns either
    success or failure in the form of a string.
    It is coded in Python 3, and does use Juniper's PyEz package.

    Timing. When the outcome is success, it takes about 4.1 to 4.3 seconds to execute.
    When the outcome is failure, it takes between 13.4 and 13.6 seconds to execute.

    Args:
        ne (str)            Network Element, Juniper router to log to
        os_username (str)   Username to log as in the router
        os_password (str)   Password for the username above
        vrf (str)           The routing-instance from which we want to ping from
        host (str)          IP address we want to ping to. Can be either IPv4, IPv6 or a FQDN

    Returns:
        String

    Requires:
        Python 3
        junos-eznc

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        improve speed (persistent session? ping fast?)
        remove name resolution? force to enter ip address??
        time it. Have knob to know how long it takes to execute, begin to end

    References:
        Using Junos PyEZ to Execute RPCs on Devices Running Junos OS
        https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-rpcs-executing.html

        Access RPC On Demand Directly
        # https://forums.juniper.net/t5/Automation/Scripting-How-To-Access-RPC-on-demand/ta-p/278823
        # parameter names that contain dashes, you swap them for underscores;
        # routing-instance becomes routing_instance

        ping_and_traceroute_from_pyez.py
        https://gist.github.com/ksator/93aea7fcba92b9db5e12d5cbdba22788

        Python Timer Functions: Three Ways to Monitor Your Code
        https://realpython.com/python-timer/#python-timers
    '''
    # imports, Python standard modules
    import time                     # if we want to time things

    # start time counter
    timer_start = time.perf_counter()

    # imports, Python packages
    from jnpr.junos import Device   # this is Juniper's PyEz

    # open Netconf session with the network element
    try:
        dev = Device(host=ne, user=os_username, password=os_password)
        dev.open(gather_facts=False)    # no need to gather facts, so to gain speed
    except Exception as err:
        return str(err)

    # execute command in NE, get the output as JSON
    outcome = dev.rpc.ping({'format': 'json'}, routing_instance=vrf, host=host)
    # FIGURE IF rapid ping makes for a faster result
    # outcome = dev.rpc.ping({'format':'json'}, routing_instance=vrf, host=host, rapid=True)

    results_dict = outcome['ping-results'][0]   # dictionary where we find the success/failure
    # from pprint import pprint       # uncomment if you want to see the output
    # pprint(results_dict)           # uncomment if you want to see the output

    if 'ping-success' in results_dict:
        outcome = "SUCCESS"
    if 'ping-failure' in results_dict:
        outcome = "FAILURE"

    # close the Netconf session with the NE
    dev.close()

    # end time counter
    timer_end = time.perf_counter()
    print(f"Time to execute the script, begin to end: {timer_end - timer_start:0.2f} seconds")

    # end
    return outcome


ne = "dist2-testlab.nn.hea.net"
os_username = "heanet"
os_password = "$!3u$uxqDMTXzw9"
vrf = "scoil_l3vpn.20200507"
host_4 = "10.11.12.13"      # does exist, should return success
#host_4 = "1.1.1.1"          # does NOT exist, should return failure
host_6 = "fd00:10:11:12::13"
host = host_4
outcome = ping_vrf(ne, os_username, os_password, vrf, host)
# from pprint import pprint
# pprint(outcome)
print(outcome)
# from lxml import etree
# pprint(etree.tostring(outcome))

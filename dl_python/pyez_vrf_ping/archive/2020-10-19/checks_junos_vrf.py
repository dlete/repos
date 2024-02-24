#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# to overcome message in Ubuntu 16.04
# /usr/local/lib/python3.5/dist-packages/paramiko/transport.py:33:
# CryptographyDeprecationWarning: Python 3.5 support will be dropped in the
# next release ofcryptography. Please upgrade your Python.
# from cryptography.hazmat.backends import default_backend
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def ping_vrf(ne: str,
             os_username: str,
             os_password: str,
             vrf: str,
             hosts: list,
             debug_level: str = 'ERROR') -> dict:
    ''' Return success/failure for pinging a L3VPN host from within a vrf of a given NE

    This function logs into a router and issues a ping from within a vrf. It returns either
    success or failure in the form of a string.
    It is coded in Python 3, and does use Juniper's PyEz package.

    Timing. When the outcome is success, it takes about 4.1 to 4.3 seconds to execute.
    When the outcome is failure, it takes between 13.4 and 13.6 seconds to execute.

    Args:
    Required:
        ne (str)            Network Element, Juniper router to log to
        os_username (str)   Username to log as in the router
        os_password (str)   Password for the username above
        vrf (str)           The routing-instance from which we want to ping from
        hosts (list)        List of IP addresses we want to ping to.
                            Can be either IPv4, IPv6 or a FQDN
    Optional:
        debug_level(str)    Python logging level, if not set it defaults to 'WARNING'.
                            Set to 'DEBUG' to see verbose execution.

    Returns:
        dictionary. The keys are the IP addresses in the hosts input variable. The values are
        either 'sucess' or 'failure' depending on whether ping was successful or not.

    Version:
        2020-10-15

    Requires:
        Python 3.5
        junos-eznc 2.5

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        improve speed (persistent session? ping fast?)
        remove name resolution? force to enter ip address??
        parallel processing

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
    #
    # imports
    #
    # imports, Python standard modules
    import logging                          # for debugging
    import socket                           # to resolve FQDN to IPv4
    import time                             # to time spans of code
    # imports, Python third party modules
    from jnpr.junos import Device           # this is Juniper's PyEz

    # to overcome message in Ubuntu 16.04
    # /usr/local/lib/python3.5/dist-packages/paramiko/transport.py:33:
    # CryptographyDeprecationWarning: Python 3.5 support will be dropped in the
    # next release ofcryptography. Please upgrade your Python.
    # from cryptography.hazmat.backends import default_backend
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    #
    # Create a custom logger and set debug level
    #
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)              # will get annoyed is not set to DEBUG here!!
    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()         # console handler
    c_handler.setLevel(debug_level)             # set debug level
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  'line: ' + '%(lineno)d: %(levelname)s: %(message)s'))
    c_handler.setFormatter(c_format)            # apply the formatter
    logger.addHandler(c_handler)                # add handlers to the logger

    # timers are used to measure how long it takes to execute the code
    timer_script_start = time.perf_counter()    # start timer for whole script
    timer_netconf_start = time.perf_counter()   # start timer to open Netconf

    #
    # Compose the request and open Netconf session
    #
    try:                                        # open Netconf session with the NE
        # ne_ipv4 = socket.getaddrinfo(ne, None, socket.AF_INET)[0][4][0]     # resolve FQDN to IPv4
        # ne_ipv6 = socket.getaddrinfo(ne, None, socket.AF_INET6)[0][4][0]    # resolve FQDN to IPv6
        # ne_ip = ne_ipv6                        uncomment if want to ensure the use of IPv4 or IPv6
        ne_ip = socket.gethostbyname(ne)
        dev = Device(host=ne_ip, user=os_username, password=os_password)
        dev.open(gather_facts=False)            # no need to gather facts, so to gain speed
    except Exception as err:
        raise Exception(err)                    # can't connect -> Exception

    # if debugging, report how long it takes to open the Netconf session
    timer_netconf_end = time.perf_counter()                     # end timer to open Netconf session
    timer_netconf = timer_netconf_end - timer_netconf_start     # compute time open Netconf session
    logger.debug(('Time to open Netconf session with {ne} on {ne_ip}: {timer_netconf:0.2f} seconds'
                 .format(ne=ne, ne_ip=ne_ip, timer_netconf=timer_netconf)))

    #
    # issue the ping command and record responses
    #
    ping_results = {}       # initialize. This will be the return. It will be a dictionary

    for host in hosts:      # iterate through the hosts, ping each and add to the return
        timer_command_start = time.perf_counter()               # start timer to ping host

        # execute command in NE, get the output as JSON
        outcome = dev.rpc.ping({'format': 'json'}, routing_instance=vrf, host=host)
        # rapid ping takes the same amount of time to execute!! how come??
        # outcome = dev.rpc.ping({'format':'json'}, routing_instance=vrf, host=host, rapid=True)

        results_dict = outcome['ping-results'][0]   # dictionary where we find the success/failure
        # from pprint import pprint      # uncomment if you want to see the output
        # pprint(results_dict)           # uncomment if you want to see the output

        if 'ping-success' in results_dict:
            ping_results[host] = 'success'
            timer_command_end = time.perf_counter()                 # end timer to ping host
        if 'ping-failure' in results_dict:
            ping_results[host] = 'failure'
            timer_command_end = time.perf_counter()                 # end timer to ping host

        # if debugging, report how long it takes to ping the host
        timer_command = timer_command_end - timer_command_start     # compute time to ping host
        logger.debug(('Time to ping host {host}: {timer_command:0.2f} seconds'
                     .format(host=host, timer_command=timer_command)))

    dev.close()     # leave orderly. Properly close the Netconf session with the NE

    # if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()                  # end timer for whole script
    timer_script = timer_script_end - timer_script_start    # compute time execute the whole script
    logger.debug("Time to execute the script, begin to end: {timer_whole_script:0.2f} seconds"
                 .format(timer_whole_script=timer_script))

    # from pprint import pprint     # uncomment if you want to see the final output
    # pprint(ping_results)          # command_outcome is a dictionary
    # end, return outcome of each ping in a dictionaries
    # of the shape:
    #{
    # '1.1.1.1': 'success',
    # '10.11.12.13': 'failure',
    # 'fd00:10:11:12::13': 'success'
    # }

    # end, return outcome of each ping in a dictionary of the shape {$host: success/failure}
    return ping_results


if __name__ == '__main__':
    # to overcome message in Ubuntu 16.04
    # /usr/local/lib/python3.5/dist-packages/paramiko/transport.py:33:
    # CryptographyDeprecationWarning: Python 3.5 support will be dropped in the
    # next release ofcryptography. Please upgrade your Python.
    # from cryptography.hazmat.backends import default_backend
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    os_username = "heanet"
    os_password = "$!3u$uxqDMTXzw9"

    #ne = "dist2-testlab.nn.hea.net"
    ne = "edge3-testlab.nn.hea.net"
    #ne = "edge4-testlab.nn.hea.net"

    vrf = "scoil_l3vpn.20200507"
    vrf = "testlab.2020081013"

    host_4 = "10.11.12.13"          # does exist, should return success
    host_4_bogus = "1.1.1.1"        # does NOT exist, should return failure
    host_6 = "fd00:10:11:12::13"
    host = host_4
    #hosts = ["10.11.12.13", host_6, host_4, host_6, host_4, host_6, host_4, host_6,
    #         host_4, host_6, host_4_bogus]
    hosts_4 = [host_4] * 5
    hosts_6 = [host_6] * 5
    hosts_4_bogus = [host_4_bogus] * 1
    #hosts = hosts_4 + hosts_6 + hosts_4_bogus
    hosts = [item for pair in zip(hosts_4, hosts_6) for item in pair] + hosts_4_bogus

    # test L3VPN for testlab development of SHIBA
    test_l3vpn_ipv4s = ["87.44.68.38", "87.44.68.42", "87.44.68.46"]
    test_l3vpn_ipv6s = ["2001:0770:0100:6836::2",
                        "2001:0770:0100:6840::2",
                        "2001:0770:0100:6844::2"]
    test_l3vpn_ips = test_l3vpn_ipv4s + test_l3vpn_ipv6s

    hosts = test_l3vpn_ips
    #outcome = ping_vrf(ne, os_username, os_password, vrf, host)
    outcome = ping_vrf(ne, os_username, os_password, vrf, hosts, 'DEBUG')
    print(outcome)

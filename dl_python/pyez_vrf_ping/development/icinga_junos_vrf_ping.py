#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is an Icinga check to verify ICMP ping reachability to hosts within a router VRF.
The module is built to be invoked from CLI.

Invoke as:

python icinga_junos_vrf_ping.py \
    -H edge3-testlab.nn.hea.net \
    -u heanet -p 'substiteWithActualPassword' \
    -f testlab.2020081013 \
    -l "87.44.68.38 87.44.68.42 87.44.68.46 \
       2001:0770:0100:6836::2 2001:0770:0100:6840::2 2001:0770:0100:6844::2" \
    -d

OR, if you want to ignore warnings (for example: "CryptographyDeprecationWarning: Python 3.5
support will be dropped in the next release ofcryptography. Please upgrade your Python.).
Then invoke as:

python -W ignore icinga_junos_vrf_ping.py \
    -H edge3-testlab.nn.hea.net \
    -u heanet -p 'substiteWithActualPassword' \
    -f testlab.2020081013 \
    -l "87.44.68.38 87.44.68.42 87.44.68.46 \
       2001:0770:0100:6836::2 2001:0770:0100:6840::2 2001:0770:0100:6844::2" \
    -d

Note this:
* the password has to be enclosed in single ''
* the IP addresses to ping are to be writen separated by a single space, without ", or '
  between them, but fully enclosed in ""

Version:
    2020-12-15

The module is organized in three functions
* get_args(). Parses the arguments passed by the user from CLI
* ping_vrf(). This does the actual work of logging to a router and pinging hosts from there
* run_script(). Glues the two above. Gets the CLI arguments, passes them to the working function
  and returns the outcome to the user.
* __if_main__. So that serves as initiator.
"""


def get_args() -> tuple:
    '''Parses arguments passed to the script on CLI'''

    # imports, Python standard modules
    import argparse

    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Script to probe Juniper Router Power')

    # Add arguments
    parser.add_argument('-H', '--hostname', help='Router name',
                        required=True, type=str)
    parser.add_argument('-u', '--username', help='NETCONF Username',
                        required=True, type=str)
    # nargs='+' used because current password has several special characters....
    parser.add_argument('-p', '--password', help='NETCONF Password in single quotes...',
                        required=True, type=str, nargs='+')
    parser.add_argument('-f', '--vrf', help='VRF name',
                        required=True, type=str)
    parser.add_argument('-l', '--hosts', help='list of IP hosts to ping',
                        required=True, nargs='+')    # works
    parser.add_argument("-d", "--debug", help="enable debug mode",
                        required=False, action="store_true")

    # Array for all arguments passed to script
    args = parser.parse_args()

    # Assign args to variables
    hostname = args.hostname
    username = args.username
    password = args.password[0]         # because when using nargs='+', it returns a list
    vrf = args.vrf
    ips = ''.join(args.hosts).split()   # this is a list, each IP is an element
    debug = args.debug

    # Return all variable values
    return hostname, username, password, vrf, ips, debug


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
        2020-12-15

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


def run_script() -> str:
    """Invokes the other functions and returns outcome values to Icinga"""

    #
    # imports
    #
    # Python standard modules
    #import socket      # in case IPv6 connectivity to Netconf port is blocked
    import sys
    from enum import Enum

    # to overcome message in Ubuntu 16.04
    # /usr/local/lib/python3.5/dist-packages/paramiko/transport.py:33:
    # CryptographyDeprecationWarning: Python 3.5 support will be dropped in the
    # next release ofcryptography. Please upgrade your Python.
    # from cryptography.hazmat.backends import default_backend
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    class IcingaState(Enum):    # Icinga Status values
        ok = 0
        warning = 1
        critical = 2
        unknown = 3

    # Read arguments passed to the script
    ne, os_username, os_password, vrf, hosts, debug = get_args()

    # uncomment if it is necessary to use IPv4; e.g. IPv6 connectivity to Netconf port is blocked
    # ne = (socket.gethostbyname(ne))

    # Whether we want console output while the script progresses. In production do not use DEBUG
    if debug is True:
        debug_level = 'DEBUG'
    else:
        debug_level = 'WARNING'

    # go and ping
    try:
        ping_results = ping_vrf(ne, os_username, os_password, vrf, hosts, debug_level)
        if 'failure' in ping_results.values():
            outcome = IcingaState.critical
        else:
            outcome = IcingaState.ok

        # The following line will be rendered in the Icinga GUI for the check
        print(ping_results)
    except Exception as err:
        # The following line will be rendered in the Icinga GUI for the check
        print('The following error prevents me from executing the script: ' + str(err))
        outcome = IcingaState.critical

    # print(outcome.value)       # uncomment if debuging and want to see the integer value returned
    sys.exit(outcome.value)     # will be given to Icinga to render green/red in GUI


if __name__ == '__main__':
    run_script()

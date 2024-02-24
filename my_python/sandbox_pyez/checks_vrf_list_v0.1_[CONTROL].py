#!/usr/bin/env python3

def ping_vrf(ne, os_username, os_password, vrf, hosts, debug_level='WARNING'):
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
        hosts (list)        List of IP addresses we want to ping to. Can be either IPv4, IPv6 or a FQDN

    Returns:
        dictionary. The keys are the IP addresses in the hosts input variable. The values are either 'sucess'
        or 'failure' depending on whether ping was successful or not.

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
    import logging
    import time                             # to time spans of code

    # Create a custom logger and set debug level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()     # console handler
    c_handler.setLevel(debug_level)         # set debug level

    # Create formatter(s) and add to handlers
    # see available fields here:
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    c_format = logging.Formatter('%(asctime)s: %(module)s: %(funcName)s: %(lineno)d: %(name)s: %(levelname)s: %(message)s')
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)

    # start time counter
    timer_start = time.perf_counter()

    # imports, Python third party modules
    from jnpr.junos import Device   # this is Juniper's PyEz

    timer_netconf_start = time.perf_counter()
    # open Netconf session with the network element
    try:
        dev = Device(host=ne, user=os_username, password=os_password)
        dev.open(gather_facts=False)    # no need to gather facts, so to gain speed
    except Exception as err:
        return str(err)

    timer_netconf_end = time.perf_counter()
    logger.debug(f"Time to open Netconf session with NE: {timer_netconf_end - timer_netconf_start:0.2f} seconds")

    ping_results = {}       # initialize. This will be the function return
    for host in hosts:
        timer_command_start = time.perf_counter()
        # execute command in NE, get the output as JSON
        outcome = dev.rpc.ping({'format': 'json'}, routing_instance=vrf, host=host)
        # FIGURE IF rapid ping makes for a faster result
        # outcome = dev.rpc.ping({'format':'json'}, routing_instance=vrf, host=host, rapid=True)

        results_dict = outcome['ping-results'][0]   # dictionary where we find the success/failure
        # from pprint import pprint       # uncomment if you want to see the output
        # pprint(results_dict)           # uncomment if you want to see the output

        if 'ping-success' in results_dict:
            # outcome = "SUCCESS"
            ping_results[host] = 'success'
            timer_command_end = time.perf_counter()
        if 'ping-failure' in results_dict:
            # outcome = "FAILURE"
            ping_results[host] = 'failure'
            timer_command_end = time.perf_counter()
        logger.debug(f"Time to ping host {host}: {timer_command_end - timer_command_start:0.2f} seconds")

    # close the Netconf session with the NE
    dev.close()

    # end time counter
    timer_end = time.perf_counter()
    #print(f"Time to execute the script, begin to end: {timer_end - timer_start:0.2f} seconds")
    logger.debug(f"Time to execute the script, begin to end: {timer_end - timer_start:0.2f} seconds")

    # end
    # return outcome
    return ping_results


if __name__ == '__main__':
    ne = "dist2-testlab.nn.hea.net"
    os_username = "heanet"
    os_password = "$!3u$uxqDMTXzw9"
    vrf = "scoil_l3vpn.20200507"
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
    #outcome = ping_vrf(ne, os_username, os_password, vrf, host)
    outcome = ping_vrf(ne, os_username, os_password, vrf, hosts, 'DEBUG')
    print(outcome)

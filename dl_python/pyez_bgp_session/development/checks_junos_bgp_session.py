#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
invoke as:
# to set routing-instance and debug level explicitly
python check_junos_bgp_session(ne, os_username, os_password, bgp_peers, ri, 'WARNING')
# to set routing-instance explicitly and the default debug level
outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers, ri)
# to use both the default routing-instance and default debug level
outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers)

if you want to ignore warnings, for example:
# to overcome message in Ubuntu 16.04
# /usr/local/lib/python3.5/dist-packages/paramiko/transport.py:33:
# CryptographyDeprecationWarning: Python 3.5 support will be dropped in the
# next release ofcryptography. Please upgrade your Python.
# from cryptography.hazmat.backends import default_backend
then invoke as:

python -W ignore checks_junos_bgp_session(...)
"""


def check_junos_bgp_session(ne: str,
                            os_username: str,
                            os_password: str,
                            bgp_peers: list,
                            routing_instance: str = '',
                            debug_level: str = 'ERROR') -> dict:
    ''' Returns dictionary of dictionaries. Each dicationary contains BGP peering session
    status and prefixes received/accepted/active/sent for a given BGP peer.

    The function will check BGP in/for:
        * One or many IP/BGP peers
        * IPv4 or IPv6, or mix of IPv4 and IPv6
        * not indicating the routing-instance, or explicitly mentioning the routing-instance

    This function logs into a router and issues the JUNOS command:
    "show bgp neighbor <neighbor_ip> instance"
    Then it parses the output and stores the BGP peering session, prefixes
    received/accepted/active/sent into a dictionary. Can take as input one, or several IP.
    In the return, each input IP will be in its own dictionary.

    Timing. It takes about 4.5 seconds to execute for a single IP.

    Args:
    Required:
        ne (str)                Network Element, Juniper router to log to
        os_username (str)       Username to log as in the router
        os_password (str)       Password for the username above
        bgp_peers (list)        List of IP address for BGP peers we want to check their session.
                                Can be either an IPv4 or an IPv6 address.
                                Cannot be, of course, a FQDN.
                                Example:
                                    If:
                                    bgp_peer_4 = "87.44.68.38"
                                    bgp_peer_6 = "2001:770:100:6836::2"

                                    Then:
                                    bgp_peers = [bgp_peer_6] + [bgp_peer_4]
                                    or
                                    bgp_peers = [bgp_peer_6]
    Optional:
        routing_instance (str)  The routing-instance where the BGP session is held.
                                To explicitly check 'inet.0' or 'inet6.0', set vrf to 'master'
                                To explicilty check '<vrf>.inet.0' or '<vrf>.inet.6' set
                                routing_instance to '<vrf>'
                                If not set, it defaults to ''. JUNOS will be happy with '' whether
                                the IP is inside a routing-instance or not.
        debug_level(str)        Python logging level, if not set it defaults to 'WARNING'.
                                Set to 'DEBUG' to see verbose execution.

    Returns:
        dictionary. The keys are the IP addresses in the BGP peers input variable.
        The values are a dictionary. Each of these dicionaries then has keys for:
        'peer_address', 'state', 'received_prefix_count', 'accepted_prefix_count',
        'active_prefix_count' and 'advertised_prefix_count'

    Version:
        2021-01-21

    Requires:
        Python 3.5
        unos-eznc 2.5

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        * more meaningful error messages; e.g. if the IP we query does not exist in
          the routing-instance we pass
        * remove name resolution for NE? force to enter IP address?
          would reduce execution time?
        * Better handle of exceptions. Return always a dictionary. With keys for success/failure
          and failure message; e.g.
            command_results['execution'] = success/failure
            command_results['failure_msg'] = 'could not do this or that...'

    References:
        see available fields for the Python logging formatters here:
        https://docs.python.org/3/library/logging.html#logrecord-attributes

        Using Junos PyEZ to Execute RPCs on Devices Running Junos OS
        https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-rpcs-executing.html

        Access RPC On Demand Directly
        # https://forums.juniper.net/t5/Automation/Scripting-How-To-Access-RPC-on-demand/ta-p/278823
        # parameter names that contain dashes, you swap them for underscores;
        # routing-instance becomes routing_instance

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
    # Open Netconf session with the NE
    #
    try:
        # ne_ipv4 = socket.getaddrinfo(ne, None, socket.AF_INET)[0][4][0]     # resolve FQDN to IPv4
        # ne_ipv6 = socket.getaddrinfo(ne, None, socket.AF_INET6)[0][4][0]    # resolve FQDN to IPv6
        # ne_ip = ne_ipv6                        uncomment if want to ensure the use of IPv4 or IPv6
        # Deterministically, connect with IPv4
        ne_ip = socket.gethostbyname(ne)
        dev = Device(host=ne_ip, user=os_username, password=os_password)
        dev.open(gather_facts=False)            # no need to gather facts, so to gain speed
    except Exception as err:
        raise Exception(err)                    # can't connect -> Exception

    timer_netconf_end = time.perf_counter()                     # end timer to open Netconf
    timer_netconf = timer_netconf_end - timer_netconf_start     # calculate time to bring Netconf up
    logger.debug(('Time to open Netconf session with {ne} on {ne_ip}: {timer_netconf:0.2f} seconds'
                 .format(ne=ne, ne_ip=ne_ip, timer_netconf=timer_netconf)))

    #
    # Issue the command and record responses
    #
    # initialize the dictionry that the function will be returning
    command_results = {}

    # iterate through the BGP peers, issue the command and add to the return
    for bgp_peer in bgp_peers:
        # each bgp_peer will have its own dictionary
        peer_stats = {}

        timer_command_start = time.perf_counter()   # start timer to execute command
        logger.debug(("Will now issue command 'show bgp neighbor {peer} instance {instance}' "
                     "in {ne}".format(peer=bgp_peer, instance=routing_instance, ne=ne)))

        # Execute command in NE, seek the output as JSON
        # Unless a specific routing-instance has been passed as input,
        # # the below will default to "".
        # JUNOS will be happy with "", the use/not of routing-instance name
        # is optional.
        command_outcome = (dev.rpc.
                           get_bgp_neighbor_information({'format': 'json'},
                                                        instance=routing_instance,
                                                        neighbor_address=bgp_peer))

        try:
            # The BGP peering session (the TCP session) state is at this height
            # in the outcome and it is a dictionary.
            # Put in its own variable so that lines do not grow forever in lenght, that is all.
            dict_peer_state = command_outcome['bgp-information'][0]['bgp-peer'][0]['peer-state'][0]
        except Exception as err:
            # for example, covers the eventuality of having been passed and
            # incorrectly formed IP address (e.g.: 2001:0770:0100:6844:::::2,
            # or 2001:0770:0100:6844:2, note how there are too many or too little :?)
            command_error_message = command_outcome['error'][0]['message'][0]['data']
            raise Exception(err, command_error_message)

        # Populate the dictionary for this given BGP peer
        peer_stats['peer_address'] = bgp_peer
        peer_stats['state'] = dict_peer_state['data']
        logger.debug("BGP peer {peer}, is in state: {state}"
                     .format(peer=bgp_peer, state=peer_stats['state']))

        if peer_stats['state'] == 'Established':
            # if the peer is up, then include information on prefixes exchanged

            # Prefixes, received/accepted/active/sent are at this height
            # in the outcome and it is a dictionary.
            # Use? so that lines do not grow forever in lenght, that is all.
            dict_peer_rib = command_outcome['bgp-information'][0]['bgp-peer'][0]['bgp-rib'][0]

            peer_stats['received_prefix_count'] = dict_peer_rib['received-prefix-count'][0]['data']
            logger.debug("BGP peer {peer}, received prefix(es): {prefixes}"
                         .format(peer=bgp_peer, prefixes=peer_stats['received_prefix_count']))

            peer_stats['accepted_prefix_count'] = dict_peer_rib['accepted-prefix-count'][0]['data']
            logger.debug("BGP peer {peer}, accepted prefix(es): {prefixes}"
                         .format(peer=bgp_peer, prefixes=peer_stats['accepted_prefix_count']))

            peer_stats['active_prefix_count'] = dict_peer_rib['active-prefix-count'][0]['data']
            logger.debug("BGP peer {peer}, active prefix(es): {prefixes}"
                         .format(peer=bgp_peer, prefixes=peer_stats['active_prefix_count']))

            peer_stats['advertised_prefix_count'] = (dict_peer_rib['advertised-prefix-count']
                                                     [0]['data'])
            logger.debug("BGP peer {peer}, advertised prefix(es): {prefixes}"
                         .format(peer=bgp_peer, prefixes=peer_stats['advertised_prefix_count']))

        # if debugging, report how long it took to execute the command
        timer_command_end = time.perf_counter()                    # end timer to execute command
        timer_command = timer_command_end - timer_command_start    # compute time to execute command
        logger.debug(('Time to execute JUNOS command: {timer_command:0.2f} seconds'
                     .format(timer_command=timer_command)))

        # add the stats of this BGP peer to the overall dictionary
        command_results[bgp_peer] = peer_stats

    # leave orderly. Properly close the Netconf session with the NE
    dev.close()

    # if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()                  # end timer for whole script
    timer_script = timer_script_end - timer_script_start    # compute time execute the whole script
    logger.debug("Time to execute the script, begin to end: {timer_whole_script:0.2f} seconds"
                 .format(timer_whole_script=timer_script))

    # return dictionary of dictionaries
    return command_results


def example_of_use():
    """example of how to use"""

    # set variables
    #ne = "dist2-testlab.nn.hea.net"
    ne = "edge3-testlab.nn.hea.net"
    # ne = "edge4-testlab.nn.hea.net"
    os_username = "heanet"
    os_password = "$!3u$uxqDMTXzw9"
    # vrf = "testlab.2020081013"
    # vrf = ""
    # vrf = "master"
    bgp_peer_40 = "87.44.48.5"              # does exist, should return success
    bgp_peer_42 = "87.44.68.38"             # does exist, should return success
    bgp_peer_62 = "2001:770:100:6836::2"    # does exist, should return success
    bgp_peer_43 = "87.44.68.42"             # does exist, should return success
    bgp_peer_63 = "2001:770:100:6840:2"    # does exist, should return success
    bgp_peer_44 = "87.44.68.46"             # does exist, should return success
    bgp_peer_64 = "2001:770:100:6844::2"    # does exist, should return success
    # bgp_peer_442 = "87.44.68.50"             # does exist, should return success
    # bgp_peer_642 = "2001:770:100:6848::2"    # does exist, should return success
    bgp_peers = ([bgp_peer_40] + [bgp_peer_42] + [bgp_peer_62] + [bgp_peer_43]
                 + [bgp_peer_63] + [bgp_peer_44] + [bgp_peer_64])
    bgp_peers = [bgp_peer_63]

    # invoke function
    # outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers, vrf, 'WARNING')
    # outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers, vrf, 'DEBUG')
    # outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers, vrf)
    outcome = check_junos_bgp_session(ne, os_username, os_password, bgp_peers)

    # display the outcome
    from pprint import pprint
    pprint(outcome)


if __name__ == '__main__':
    """
    triggers execution of this module when invoked from CLI

    Execute when run the script from the command line but
    not when the Python interpreter imports the file.
    """
    example_of_use()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is an Icinga check to verify IS-IS interfaces consistency,
and hence faults, in a Juniper router.
The module is built to be invoked from CLI.

Examaples on how to invoke:
# example, most common for production:  without instance,
#                                       without interfaces,
#                                       without debug
python icinga_junos_isis_interface.py \
    -H dist2-testlab.nn.hea.net \
    -u heanet -p 'substiteWithActualPassword'

# If you want to ignore warnings (for example: "CryptographyDeprecationWarning: Python 3.5
# support will be dropped in the next release ofcryptography. Please upgrade your Python.).
# Then invoke as:
python -W ignore icinga_junos_isis_interface.py \
    -H dist2-testlab.nn.hea.net \
    -u heanet -p 'substiteWithActualPassword'

# example, most common for troubleshooting: without instance,
#                                           without interfaces,
#                                           WITH debug
python icinga_junos_isis_interface.py \
    -H dist2-testlab.nn.hea.net \
    -u heanet -p 'substiteWithActualPassword' \
    -d

Note this:
* the password has to be enclosed in single ''
* the interfaces to query are to be writen separated by a single space, without ", or '
  between them, but fully enclosed in "" or '', both " and ' work.
  Example: "ge-0/0/0 ge-1/0/0"

Version:
    2021-05-27

This module has these functions:
* get_args(). Parses the arguments passed by the user from CLI
* get_isis_interface(). This does the actual work of logging to a router
  and issuing the "show isis interface extensive (<instance>)" command
* check_isis_consistency(). Applies logic to determine if the IS-IS interfaces
  configuration and status are consistent.
* run_script(). Glues the two above. Gets the CLI arguments, passes them to the
  working function and returns the outcome to the user.
* __if_main__. So that serves as initiator.
"""

# imports
# imports, Python standard modules
from typing import Dict

# Type alias for JUNOS interface as a string
junos_if = str


def get_args() -> tuple:
    '''Returns arguments parsed from CLI when invoking the module from CLI

        Version:
            2021-04-08
        '''

    # imports, Python standard modules
    import argparse

    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Script to probe Juniper Router IS-IS interfaces')

    # Add arguments
    parser.add_argument('-H', '--hostname',
                        help='Router name',
                        required=True,
                        type=str)
    parser.add_argument('-u', '--username',
                        help='NETCONF Username',
                        required=True,
                        type=str)
    # nargs='+' used because current password has several special characters....
    parser.add_argument('-p', '--password',
                        help='NETCONF Password in single quotes...',
                        required=True,
                        type=str,
                        nargs='+')
    parser.add_argument('-i', '--instance',
                        help='IS-IS instance name',
                        required=False,
                        type=str)
    parser.add_argument('-f', '--interfaces',
                        help='list of interfaces to query',
                        required=False,
                        type=str, nargs='+')
    parser.add_argument("-d", "--debug",
                        help="enable debug mode",
                        required=False,
                        action="store_true")

    # Array for all arguments passed to the module from CLI
    args = parser.parse_args()

    # Assign args to variables
    hostname = args.hostname
    username = args.username
    # because when using nargs='+', that returns a list
    password = args.password[0]
    # if the IS-IS instance is explicitly given, take it; otherwise use empty ''
    if args.instance:
        isis_instance = args.instance
    else:
        isis_instance = ''
    # if the IS-IS interfaces is explicitly given, take it; otherwise use empty ''
    # this is a list, each element is a JUNOS interface
    if args.interfaces:
        isis_interfaces = ''.join(args.interfaces).split()
    else:
        isis_interfaces = []
    debug = args.debug

    # Return all variable values
    #return hostname, username, password, isis_instance, isis_interfaces, debug
    return hostname, username, password, isis_instance, isis_interfaces, debug


def get_junos_isis_interfaces(ne: str,
                              os_username: str,
                              os_password: str,
                              isis_interfaces: list = [],
                              isis_instance: str = '',
                              debug_level: str = 'ERROR') -> Dict[junos_if, Dict[str, str]]:
    '''
    Returns dictionary of dictionaries.
    Each dicationary contains IS-IS interface information. See the format of
    the dictionary below, in the Return section of the documentation.

    The function retrieves IS-IS information as:
        * for each IS-IS interface
        * then for each level (1 and 2) in that interface:
            * whether the interface is IS-IS enabled or not for that level,
            * whether it is passive or not
            * the number of IS-IS adjancies

    This function logs into a router and issues the JUNOS command:
    "show isis interface extensive (<instance>)"
    Then it parses the output and stores the IS-IS interface inforamtion
    mentioned above.

    Timing/performance
        It takes about 10 seconds to execute for all the interfaces in an IS-IS node.
        No known performance impact on the NE. Tested and used in MX960, MX480, MX104
        ACX5048 and ACX2200 without appreciable impact.

        The known time to open NETCONF session is 2.81 to 3.00 seconds
        with dist1-testlab.
        The first time the NETCONF session is opened it takes longer though,
        could be even between 10 to 15. Suspect this may be due to name
        resolution unitil the IP of the NE is cached in the host executing
        this function.

        There seems not to be difference in the time it takes to issue the
        command as either:
            show isis interfaces            # 2.82 to 3.94 seconds in dist1-testlab
            or
            show isis interfaces extensive  # 2.71 to 3.00 seconds in dist1-testlab
        so we use the extensive know all the time.

    Args:
    Required:
        ne (str)                Network Element, Juniper router to log to.
                                Give me the FQDN please.
        os_username (str)       Username to log as in the router
        os_password (str)       Password for the username above
    Optional:
        isis_interfaces (list)  List of interface names to check.
                                Not enabled in this version. Left as placeholder
                                for future versions if the need arises.
                                Not enabled currently.
        isis_instance (str)     Name of the IS-IS routing instance to query.
                                Not enabled in this version. Left as placeholder
                                for future versions if the need arises.
                                Most likely will never need it.
                                Not enabled currently.
        debug_level(str)        Python logging level, if not set it defaults to 'WARNING'.
                                Set to 'DEBUG' to see verbose execution.

    Returns:
        Dictionary.
        In fact, a dictionary of dictionaries. The keys are the interface
        names of the IS-IS interfaces in the NE.
        The values are a dictionary on their own with IS-IS interface
        information. Each of these dicionaries then has keys for:
        'interface_name', 'level_1' and 'level_2'.

        The shape of the return dictionary is as:
        {
            'lo0.0': {
                'interface_name': 'xe-2/0/0.0',
                'level_1': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'},
                'level_2': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'}
            },
            .
            .
            .
            'xe-0/0/0.0': {
                'interface_name': 'xe-2/0/0.0',
                'level_1': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'},
                'level_2': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'}
            },
        }

    How to use/onboarding/tweaks and possible modifications
        The auto_probe value will set how long you want to wait for the NE to
        repond to an NETCONF connection request. With the auto_prove you tune
        the timeout of NETCONF connection, NOT the timeout for the RPC command
        they are different things.

    Version:
        2021-04-08

    Requires:
        Python 3.5
        junos-eznc 2.5

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        * case when IS-IS is not enabled in the NE (low priority)
        * enable checking of a given interface input isis_interfaces: list = [],
          list of tuples? (interface, level)
        * refine the case when there is an IS-IS instance
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

        PEP 484 -- Type Hints
        https://www.python.org/dev/peps/pep-0484/
    '''

    #
    # imports
    #
    # imports, Python standard modules
    import logging                          # for debugging
    import socket                           # to resolve FQDN to IPv4
    import time                             # to time spans of code
    # imports, Python third party modules
    # Juniper's PyEZ
    from jnpr.junos import Device
    import jnpr.junos.exception as JUNOS_EXCEPTION

    #
    # Sanitize
    #
    # due diligence, verify input variables are correct, as expected.
    try:
        # Ensure ne is a string
        assert isinstance(ne, str), ('what you pass as ne is not a '
                                     'string, it is a {what_type}'
                                     .format(what_type=type(ne)))
        # Ensure os_username is a string
        assert isinstance(os_username, str), ('what you pass as os_username is not a '
                                              'string, it is a {what_type}'
                                              .format(what_type=type(os_username)))
        # Ensure os_password is a string
        assert isinstance(os_password, str), ('what you pass as os_password is not a '
                                              'string, it is a {what_type}'
                                              .format(what_type=type(os_password)))
        # Ensure isis_interfaces is a list
        assert isinstance(isis_interfaces, list), ('what you pass as isis_interfaces is not a '
                                                   'list, it is a {what_type}'
                                                   .format(what_type=type(isis_interfaces)))
        # Ensure isis_instance is a string
        assert isinstance(isis_instance, str), ('what you pass as isis_instance is not a '
                                                'string, it is a {what_type}'
                                                .format(what_type=type(isis_instance)))
        # Ensure debug_level is a string
        assert isinstance(debug_level, str), ('what you pass as debug_level is not a '
                                              'string, it is a {what_type}'
                                              .format(what_type=type(debug_level)))
    except AssertionError as err:
        raise Exception('Got error: {err}.'
                        .format(err=err))

    #
    # Create a custom logger and set debug level
    #
    logger = logging.getLogger(get_junos_isis_interfaces.__qualname__)
    logger.setLevel(logging.DEBUG)          # Gets annoyed DEBUG is not here!!
    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()     # console handler
    c_handler.setLevel(debug_level)
    # Create formatter and apply formatter and handler
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  'line: ' + '%(lineno)d: '
                                  '%(levelname)s: %(message)s'))
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    #
    # time
    #
    # timer to measure how long it takes to execute the whole function
    timer_script_start = time.perf_counter()    # start timer for whole script

    #
    # Open Netconf session with the NE
    #
    # timer to measure how long it takes to open Netconf session
    timer_netconf_start = time.perf_counter()
    try:
        # ne_ipv4 = socket.getaddrinfo(ne, None, socket.AF_INET)[0][4][0]   # resolve FQDN to IPv4
        # ne_ipv6 = socket.getaddrinfo(ne, None, socket.AF_INET6)[0][4][0]  # resolve FQDN to IPv6
        # uncomment if want to deterministically use of IPv4 or IPv6 for NETCONF session
        # ne_ip = ne_ipv4
        #
        # Deterministically, connect with IPv4
        ne_ip = socket.gethostbyname(ne)

        dev = Device(host=ne_ip, user=os_username, password=os_password, auto_probe=29)
        # no need to gather facts, so to gain speed
        dev.open(gather_facts=False)

        # if debugging, report on parameters of the NETCONF connection
        logger.debug('Netconf connection state with {ne} is {connect_status}. '
                     'The connection is with IP: {ip}. '
                     'The RPC timeout is {timeout_rpc} seconds. '
                     'The user accessing the NE is {user}.'
                     .format(ne=ne,
                             connect_status=dev.connected,
                             ip=dev.hostname,
                             timeout_rpc=dev.timeout,
                             user=dev.user))
    except JUNOS_EXCEPTION.ConnectAuthError as err:
        # case for incorrect username/password
        related_information = ('https://github.com/Juniper/py-junos-eznc'
                               '/issues/780 or '
                               'https://pyez.readthedocs.io/en/latest/'
                               'jnpr.junos.html#module-jnpr.junos.exception')
        raise Exception('Cannot connect to device {ne}: {0}. '
                        'Maybe the username/password used are incorrect?. '
                        'Generated if the user-name, password is invalid. '
                        'Check this, it may help: {related_information}'
                        .format(err, ne=ne, related_information=related_information))
    except JUNOS_EXCEPTION.ConnectRefusedError as err:
        # possibly netconf is not enabled, or access to netconf is denied
        # Note if the connection is on IPv4 or IPv6 and verifiy port/acl.
        related_information = ('https://www.juniper.net/documentation/en_US/'
                               'junos-pyez/topics/task/troubleshooting/'
                               'junos-pyez-connection-errors-troubleshooting.html or '
                               'https://pyez.readthedocs.io/en/latest/'
                               'jnpr.junos.html#module-jnpr.junos.exception')
        raise Exception('Cannot connect to device {ne}: {0}. '
                        'Maybe an access list in the NE control plane '
                        'to NETCONF port? or NETCONF not enabled?. '
                        'Generated if the specified host denies the NETCONF; '
                        'could be that the NETCONF service is not enabled, '
                        'or the host has too many connections already. '
                        'Check this, it may help: {related_information}'
                        .format(err, ne=ne, related_information=related_information))
    except JUNOS_EXCEPTION.ConnectTimeoutError as err:
        # may be an ACL in an intermediate router in the the path to ne_ip
        # Note if the connection is on IPv4 or IPv6 and verify port/acl.
        related_information = ('https://github.com/Juniper/py-junos-eznc'
                               '/issues/780')
        raise Exception('Cannot connect to device {ne}: {0}. Maybe an access list '
                        'along the path in an intermediate NE blocking the '
                        'source IP and/or destination to NETCONF IP/port?. '
                        'Could be also happen if the device is not ip '
                        'reachable; bad ipaddr or just due to routing. '
                        'Check this, it may help: {related_information}'
                        .format(err, ne=ne, related_information=related_information))
    except JUNOS_EXCEPTION.ProbeError as err:
        # may be an ACL in an intermediate router in the the path to ne_ip
        # Note if the connection is on IPv4 or IPv6 and verify port/acl.
        related_information = ('https://github.com/Juniper/py-junos-eznc'
                               '/issues/780 or '
                               'https://pyez.readthedocs.io/en/latest/'
                               'jnpr.junos.html#module-jnpr.junos.exception')
        raise Exception('Cannot connect to device {ne}: {0}. Maybe an access list '
                        'along the path in an intermediate NE blocking the '
                        'source IP and/or destination to NETCONF IP/port?. '
                        'or maybe the NE is sluggish and need more time?. '
                        'Generated if auto_probe is enabled and the probe action fails. '
                        'Check this, it may help: {related_information}'
                        .format(err, ne=ne, related_information=related_information))
    except Exception as err:
        # catch all
        related_information = ('https://pyez.readthedocs.io/en/latest/'
                               'jnpr.junos.html#module-jnpr.junos.exception')
        raise Exception('Error connecting to {ne}: {0}. Precise cause is unknown. '
                        'Check this, it may help: {related_information}'
                        .format(err, ne=ne, related_information=related_information))

    # if debugging, report how long it took to open Netconf session with the NE
    timer_netconf_end = time.perf_counter()
    timer_netconf = timer_netconf_end - timer_netconf_start
    logger.debug(('Time to open Netconf session with {ne} on {ne_ip}: '
                 '{timer_netconf:0.2f} seconds'.format(ne=ne, ne_ip=ne_ip,
                  timer_netconf=timer_netconf)))

    #
    # Issue the command and record responses
    #
    # timer to measure JUNOS command execution, to retrieve IS-IS interfaces
    timer_isis_interface_start = time.perf_counter()
    if isis_instance:
        # This is the case when the query is for a specific IS-IS instance
        # this section is pending to develop. Not enabled for the time being.
        logger.debug(('Issue command "show isis interface extensive instance '
                      '{isis_instance}"'.format(isis_instance=isis_instance)))
        # outcome is a dictionary
        isis_interfaces = (dev.rpc.get_isis_interface_information({'format': 'json'},
                                                                  extensive=True,
                                                                  instance=isis_instance))
    else:
        # This is the case when the query is for the default IS-IS instance
        logger.debug("Issue command 'show isis interface extensive'")
        # outcome is a dictionary
        isis_interfaces = (dev.rpc.get_isis_interface_information({'format': 'json'},
                                                                  extensive=True))

    # # if debugging, report how long it took to execute the command
    # to retrieve IS-IS interfaces
    timer_isis_interface_end = time.perf_counter()
    timer_isis_interface = timer_isis_interface_end - timer_isis_interface_start
    logger.debug(('Time to retrieve IS-IS interfaces in {ne} on {ne_ip}: '
                 '{timer_netconf:0.2f} seconds'.format(ne=ne, ne_ip=ne_ip,
                  timer_netconf=timer_isis_interface)))

    # done with the NE. Leave orderly. Properly close the Netconf session.
    dev.close()

    #
    # auxiliary variables and intializations
    #
    # initialize dictionary. Each interface will have its own dictionary
    #my_isis_interface = {}
    # this dictionary will have the shape:
    # my_isis_interface = {
    #                      {'interface_name': 'xe-2/0/0.0',
    #                       'level_1': {'adjacencies': '0',
    #                                   'enabled': 'yes',
    #                                   'level': '2',
    #                                   'passive': 'no'},
    #                       'level_2': {'adjacencies': '0',
    #                                   'enabled': 'yes',
    #                                   'level': '2',
    #                                   'passive': 'no'}
    #                      }
    # }

    # initialize dictionary. This will be the return.
    # It will be a dictionary of dictionaries. A dictionary with all the
    # IS-IS interfaces (each interface in its own dictionary).
    my_isis_interfaces = {}

    # this is a list. Relevant information for IS-IS interface is at this level in the hierarchy
    isis_interfaces = isis_interfaces['isis-interface-information'][0]['isis-interface']

    # iterate over the IS-IS interfaces to extract and package information
    for (i, isis_interface) in enumerate(isis_interfaces):
        # Each interface will have its own dictionary. Initialize for each interface
        my_isis_interface = {}
        # this dictionary will have the shape:
        # my_isis_interface = {
        #   'interface_name': 'xe-2/0/0.0',
        #   'level_1': {'adjacencies': '0',
        #               'enabled': 'yes',
        #               'level': '2',
        #               'passive': 'no'
        #   },
        #   'level_2': {'adjacencies': '0',
        #               'enabled': 'yes',
        #               'level': '2',
        #               'passive': 'no'}
        #   }
        # }

        # populate the interface dictionary with the key interface_name
        my_isis_interface['interface_name'] = isis_interface['interface-name'][0]['data']

        # iterate over the IS-IS levels of each IS-IS interface
        for (j, level) in enumerate(isis_interface['interface-level-data']):
            # Each level will have its own dictionary.

            # reset on each loop. Reason: in case JUNOS does not report on the
            # specific level 1 or 2 and the level_1 or level_2 dictionaries
            # are left with values from the previous loop.
            level_1 = {}
            level_2 = {}
            my_level = {}

            # initialize on each loop. Reason: we start from a default of
            # 'disabled' (not 'enabled'), and once/if the level is rendeded
            # by JUNOS, then set to 'enabled'. Otherwise the default will
            # prevail.
            level_1['enabled'] = 'no'
            level_2['enabled'] = 'no'
            my_level['enabled'] = 'no'

            # populate the level dictionary with the key number of IS-IS adjacencies
            my_level['adjacencies'] = level['adjacency-count'][0]['data']

            # check whether the dictioary key 'passive' does exist or not
            if 'passive' in level:
                # The level in the interface is EITHER enabled and passive OR it is disabled.
                # Both are shown within the same element "passive"
                #
                # Either
                # a given level is enabled and configured as passive (<passive>Passive</passive>),
                # OR
                # the level is disabled (<passive>Disabled</passive>', that is how JUNOS shows
                # disabled levels in xml)
                passive_status = level['passive'][0]['data']
                if passive_status == 'Passive':
                    # case: this level is enabled in this interface and it is configured as passive
                    # populate keys accordingly
                    my_level['enabled'] = 'yes'
                    my_level['passive'] = 'yes'
                if passive_status == 'Disabled':
                    # case: this level is disabled in this interface
                    # populate keys accordingly
                    my_level['enabled'] = 'no'
                    my_level['passive'] = 'n/a'
            else:
                # case: this level is enabled in this interface and it is configured as active
                # populate keys accordingly
                my_level['enabled'] = 'yes'
                my_level['passive'] = 'no'

            # now figure if we the level is 1 or 2 and populate the key for level
            interface_level = level['level'][0]['data']
            if interface_level == '1':
                my_level['level'] = '1'
                my_isis_interface['level_1'] = my_level
            if interface_level == '2':
                my_level['level'] = '2'
                my_isis_interface['level_2'] = my_level

        # add this interface dictionary to the overall return dictionary
        my_isis_interfaces[my_isis_interface['interface_name']] = my_isis_interface

    # if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()
    timer_script = timer_script_end - timer_script_start
    logger.debug('Time to execute the function {this_function}, begin to end: '
                 '{timer_whole_script:0.2f} seconds'
                 .format(timer_whole_script=timer_script,
                         this_function=get_junos_isis_interfaces.__qualname__))

    # return dictionary of dictionaries and end
    return my_isis_interfaces


def check_isis_consistency(isis_interfaces: dict,
                           debug_level: str = 'ERROR') -> dict:
    '''
    Checks consistency between the IS-IS router configuration
    and the IS-IS live status.

    The IS-IS router configuration and IS-IS live status have to be
    passed to this function as inputs. The role of this function is to do
    the analysis of the data, not the collection.

    At the IS-IS interface hierarchy it checks this:
    If level x is disabled -> consistent
    If level x is enabled AND passive -> consistent
    If level x is enabled AND active AND has >0 adjacencies -> consistent
    If level x is enabled AND active AND has =  adjacencies -> inconsistent

    IS-IS global -> not implemented
    If level x is disabled in all the interfaces -> consistent
    If level x is enabled in any interface AND
        all interfaces in that level are consistent -> consistent
    If level x is enabled in any interface AND
        is only the loopback -> inconsistent

    Args:
    Required:
        isis_interfaces (dict): Dictionary of IS-IS interfaces.
    Optional:
        debug_level(str)        Python logging level, if not set it defaults to 'WARNING'.
                                Set to 'DEBUG' to see verbose execution.

    The isis_interfaces dictionary must have this format:
        isis_interfaces =
        {
            'lo0.0': {
                'interface_name': 'xe-2/0/0.0',         # optional key
                'level_1': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'},
                'level_2': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'}
            },
            .
            .
            .
            'xe-0/0/0.0': {
                'interface_name': 'xe-2/0/0.0',         # optional key
                'level_1': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'},
                'level_2': {'adjacencies': '0',
                            'enabled': 'yes',
                            'level': '2',
                            'passive': 'no'}
            },
        }

    Returns
        Dictionary. To the input dictionary isis_interfaces it adds the status
        of consitent or inconsistent to each interface and IS-IS level in that
        interface.
        Then it adds a single key with an overall consistent/inconsistent at
        the top of the dictionary hierarchy.
        For the benefit of the operator, it renders a SUMMARY key with a message
        indicating what to do.
        {
        SUMMARY': 'There are IS-IS fault(s) or the configuration is not consistent. '
            "Review the lines with 'isis_if_level_consistency: False'. If an "
            'adjacency is expected in that interface/level then there is a '
            'fault, otherwise the interface/level is misconfigured and needs '
            'correction.',
        'isis_interfaces_consistency': True,
        'lo0.0': {'interface_name': 'lo0.0',
                   'level_1': {'adjacencies': '0',
                               'enabled': 'yes',
                               'isis_if_level_consistency': True,
                               'level': '1',
                               'passive': 'yes'},
                   'level_2': {'adjacencies': '0',
                               'enabled': 'yes',
                               'isis_if_level_consistency': True,
                               'level': '2',
                               'passive': 'yes'}},
        'xe-0/3/1.0': {'interface_name': 'xe-0/3/1.0',
               'level_1': {'adjacencies': '0',
                           'enabled': 'yes',
                           'isis_if_level_consistency': False,
                           'level': '1',
                           'passive': 'no'},
               'level_2': {'adjacencies': '0',
                           'enabled': 'no',
                           'isis_if_level_consistency': True,
                           'level': '2',
                           'passive': 'n/a'}}
         'xe-0/1/0.0': {'interface_name': 'xe-0/1/0.0',
                        'level_1': {'adjacencies': '1',
                                    'enabled': 'yes',
                                    'isis_if_level_consistency': True,
                                    'level': '1',
                                    'passive': 'no'},
                        'level_2': {'adjacencies': '0',
                                    'enabled': 'no',
                                    'isis_if_level_consistency': True,
                                    'level': '2',
                                    'passive': 'n/a'}}}

    Version:
        2021-04-08

    Requires:
        Python 3.5

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        * IS-IS overall logic, e.g.
          lo0, must be passive
          do something with all interfaces
          if all nni are 2, then lo0 must be 2 (1, 1)
          if some 1 and some 2, then 1 or 2 in lo0 is ok
          something along the lines a matrix (pandas?)
            lo0	1/1/1	2/2/2	3/3/3
            1	1   	1   	1           -> looks like a matrix!!
            2	1	    0	    0           ->

    References:
        see available fields for the Python logging formatters here:
        https://docs.python.org/3/library/logging.html#logrecord-attributes

        Python Timer Functions: Three Ways to Monitor Your Code
        https://realpython.com/python-timer/#python-timers

        PEP 484 -- Type Hints
        https://www.python.org/dev/peps/pep-0484/
    '''

    #
    # imports
    #
    # imports, Python standard modules
    import logging                          # for debugging
    import time                             # to time spans of code

    #
    # Sanitize
    #
    # due diligence, verify input variables are correct, as expected.
    try:
        # Ensure isis_interfaces is a dict
        assert isinstance(isis_interfaces, dict), ('what you pass as isis_interfaces is not a '
                                                   'dictionary, it is a {what_type}'
                                                   .format(what_type=type(isis_interfaces)))
        # Ensure debug_level is a string
        assert isinstance(debug_level, str), ('what you pass as debug_level is not a '
                                              'string, it is a {what_type}'
                                              .format(what_type=type(debug_level)))
    except AssertionError as err:
        raise Exception('Got error: {err}.'
                        .format(err=err))

    #
    # Create a custom logger and set debug level
    #
    logger = logging.getLogger(check_isis_consistency.__qualname__)
    logger.setLevel(logging.DEBUG)          # Gets annoyed DEBUG is not here!!
    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()     # console handler
    c_handler.setLevel(debug_level)
    # Create formatter and apply formatter and handler
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  'line: ' + '%(lineno)d: '
                                  '%(levelname)s: %(message)s'))
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    #
    # time
    #
    # timer to measure how long it takes to execute the whole function
    timer_script_start = time.perf_counter()    # start timer for whole script

    # Start with benefit of doubt.
    # Assume IS-IS router configuration and IS-IS live state are consistent.
    # Later on, if/anywhere the state is non-consistent, we will modify.
    isis_if_level_consistency = True

    for isis_if_key, isis_if_value in isis_interfaces.items():
        logger.debug('CHECK IS-IS CONSISTENCY IN: '
                     '{interface}'.format(interface=isis_if_key))
        # KEY
        #print('this is the key')
        #print(isis_if_key)             # prints this: xe-0/1/0.0
        #print(type(isis_if_key))       # this is: <class 'str'>
        # VALUE
        # print('this is the value)
        #from pprint import pprint
        #pprint(isis_if_value)
        #{'interface_name': 'xe-0/1/0.0',
        # 'level_1': {'adjacencies': '1',
        #             'enabled': 'yes',
        #             'level': '1',
        #             'passive': 'no'},
        # 'level_2': {'adjacencies': '0',
        #             'enabled': 'no',
        #             'level': '2',
        #             'passive': 'n/a'}}
        #print(type(isis_if_value))  # this is: <class 'dict'>

        # check IS-IS interface consistency
        # iterate through interfaces, and check consistency in each of them
        # mark each interface/level as consistent or inconsistent
        for if_key, if_value in isis_if_value.items():
            # only focus on the level information
            if 'level' in if_key:
                # this key is a level
                #
                # if_key has the format below and it is a string
                # 'level_1'
                # if_value has the format below and it is a dictionary
                # {'enabled': 'yes', 'adjacencies': '1', 'passive': 'no', 'level': '1'}
                logger.debug('Check IS-IS consistency in: {interface}, LEVEL {level}'
                             .format(interface=isis_if_key, level=if_value['level']))
                if if_value['enabled'] == 'no':
                    logger.debug('{interface} level {level} is NOT enabled'
                                 .format(interface=isis_if_key, level=if_value['level']))
                    # IS-IS not enabled for this level, in this interface.
                    # => consistent
                    if_value['isis_if_level_consistency'] = True
                if if_value['enabled'] == 'yes':
                    logger.debug('{interface} IS-IS level {level} is YES enabled'
                                 .format(interface=isis_if_key, level=if_value['level']))
                    if if_value['passive'] == 'yes':
                        logger.debug('{interface} IS-IS level {level} is YES passive'
                                     .format(interface=isis_if_key, level=if_value['level']))
                        # IS-IS is enabled for this level, in this interface, but it is passive
                        # => consistent
                        if_value['isis_if_level_consistency'] = True
                    if if_value['passive'] == 'no':
                        logger.debug('{interface} IS-IS level {level} is NO passive'
                                     .format(interface=isis_if_key, level=if_value['level']))
                        logger.debug('{interface} IS-IS level {level} has this number'
                                     'of adjacencies: {adjacencies}'
                                     .format(interface=isis_if_key,
                                             level=if_value['level'],
                                             adjacencies=if_value['adjacencies']))
                        if int(if_value['adjacencies']) > 0:
                            # IS-IS is enabled for this level, in this interface,
                            # it is not passive, and has adjacencies
                            # => consistent
                            if_value['isis_if_level_consistency'] = True
                        else:
                            # IS-IS is enabled for this level, in this interface,
                            # it is not passive, but and has NO adjacencies
                            # inconsistent
                            if_value['isis_if_level_consistency'] = False   # interface status
                            isis_if_level_consistency = False               # overall status

                if if_value['isis_if_level_consistency'] is True:
                    status = 'CONSISTENT'
                else:
                    status = 'INCONSISTENT'
                    # only set the status is non consistent.
                    # Approach is:
                    #   assume it all is fine (implicit)
                    #   If not, say (explicilty) so.
                    isis_if_level_consistency = False
                logger.debug('IS-IS interface {interface} level {level} '
                             'configuration and status are: {consistency}'
                             .format(interface=isis_if_key,
                                     level=if_value['level'],
                                     consistency=status))
            else:
                # this key is NOT a level, ignore it
                continue

    if isis_if_level_consistency is True:
        isis_overall_status = 'CONSISTENT'
        isis_overall_consistency = {'isis_interfaces_consistency': True}
    else:
        isis_overall_status = 'INCONSISTENT'
        isis_overall_consistency = {'isis_interfaces_consistency': False}
    logger.debug('OVERALL IS-IS interface consistency is: {consistency}'.
                 format(consistency=isis_overall_status))

    # if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()
    timer_script = timer_script_end - timer_script_start
    logger.debug('Time to execute the function {this_function}, begin to end: '
                 '{timer_whole_script:0.2f} seconds'
                 .format(timer_whole_script=timer_script,
                         this_function=check_isis_consistency.__qualname__))

    # Package nicely, with overall status on the top
    isis_overall_consistency.update(isis_interfaces)
    isis_interfaces_outcome = isis_overall_consistency

    # return and end
    return isis_interfaces_outcome


def run_script(debug_level: str = 'ERROR') -> str:
    """
    Invokes the other functions, glues their logic,
    and returns outcome values to Icinga

    Version:
        2021-05-27
    
    To-do:
        * Move the 'my_outcome_message' piece to the function check_isis_consistency.
          The reason it is in this run_script function is that HEAnet runs Ubuntu 16.04
          and hence the dictionaries do not preserve order on input of keys. That is why
          we have to create the auxiliary dictionary my_outcome_message and then merge
          them. All, so that the interpreted message about the output comes first in the
          order rendered in the GUI.
    """

    #
    # imports
    #
    # Python standard modules
    import logging                          # for debugging
    #import socket      # in case IPv6 connectivity to Netconf port is blocked
    import sys
    import time                             # to time spans of code
    from enum import Enum
    from pprint import pprint

    #
    # Create a custom logger and set debug level
    #
    logger = logging.getLogger(get_junos_isis_interfaces.__qualname__)
    logger.setLevel(logging.DEBUG)          # Gets annoyed DEBUG is not here!!
    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()     # console handler
    c_handler.setLevel(debug_level)
    # Create formatter and apply formatter and handler
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  'line: ' + '%(lineno)d: '
                                  '%(levelname)s: %(message)s'))
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    #
    # time
    #
    # timer to measure how long it takes to execute the whole function
    timer_script_start = time.perf_counter()    # start timer for whole script

    # Icinga Status values
    class IcingaState(Enum):
        ok = 0
        warning = 1
        critical = 2
        unknown = 3

    # Read arguments passed to the script
    ne, os_username, os_password, isis_instance, isis_interfaces, debug = get_args()

    # uncomment if it is necessary to deterministically use IPv4;
    # e.g. IPv6 connectivity to Netconf port is blocked
    #ne = (socket.gethostbyname(ne))

    # Whether we want console output while the script progresses.
    # In production do not use DEBUG
    if debug is True:
        debug_level = 'DEBUG'
    else:
        debug_level = 'WARNING'

    # go and issue the commands
    try:
        # get the IS-IS interfaces
        my_isis_interfaces = get_junos_isis_interfaces(ne=ne,
                                                       os_username=os_username,
                                                       os_password=os_password,
                                                       isis_instance=isis_instance,
                                                       isis_interfaces=isis_interfaces,
                                                       debug_level=debug_level)
        # check if the IS-IS interfaces and overall status is consistent
        my_isis_consistency = check_isis_consistency(isis_interfaces=my_isis_interfaces,
                                                     debug_level=debug_level)
    except Exception as err:
        # The following line will be rendered in the Icinga GUI
        # as visual aid to the operator
        print('The following error prevents me from executing the script: ' + str(err))
        outcome = IcingaState.critical
        sys.exit(outcome.value)

    # Read, analize the data we got
    if 'isis_interfaces_consistency' in my_isis_consistency:
        # we have an overall consistency status, let's get it
        if my_isis_consistency['isis_interfaces_consistency'] is True:
            outcome = IcingaState.ok
            my_outcome_message = {
                'SUMMARY': ("There are no IS-IS faults and all the "
                            "interfaces/levels configurations are consistent.")
            }
            # so that the SUMMARY comes on top of the rendered output
            my_outcome_message.update(my_isis_consistency)
        else:
            outcome = IcingaState.critical
            my_outcome_message = {
                'SUMMARY': ("There are IS-IS fault(s) or the configuration is "
                            "not consistent. Review the lines with "
                            "'isis_if_level_consistency: False'. If an "
                            "adjacency is expected in that interface/level then "
                            "there is a fault, otherwise the interface/level "
                            "is misconfigured and needs correction.")
            }
            # so that the SUMMARY comes on top of the rendered output
            my_outcome_message.update(my_isis_consistency)
    else:
        outcome = IcingaState.unknown
        my_outcome_message = {
            'SUMMARY': "Something is preventing the script from executing or the output is not "
                       "within parameters. This output does not mean there is a fault in "
                       "the network. Review Icinga, and Icinga/network combination."
        }

    # if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()
    timer_script = timer_script_end - timer_script_start
    logger.debug('Time to execute the function {this_function}, begin to end: '
                 '{timer_whole_script:0.2f} seconds'
                 .format(timer_whole_script=timer_script,
                         this_function=run_script.__qualname__))

    # The following line will be rendered in the Icinga GUI
    # as visual aid to the operator
    pprint(my_outcome_message)

    # Integer returned by this function
    logger.debug('The integer value returned to Icinga is: {icinga_code}, '
                 'which should render a {icinga_state} state for this check.'
                 .format(icinga_code=outcome.value, icinga_state=IcingaState(outcome.value)))

    # Return and end
    # The integer returned by this function will be picked up by
    # Icinga and rendered accordingly as green/red/purple in GUI
    sys.exit(outcome.value)


if __name__ == '__main__':
    """execute when the module is invoked from cli"""
    run_script()

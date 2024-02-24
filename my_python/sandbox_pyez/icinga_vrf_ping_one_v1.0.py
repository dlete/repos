#!/usr/bin/env python3

import argparse
import socket
import sys

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError


# Icinga Status values
ICINGA_OK = 0
ICINGA_WARNING = 1
ICINGA_CRITICAL = 2
ICINGA_UKNOWN = 3


def get_args():
    '''Parses arguments passed to the script'''

    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Script to ping host within a L3VPN')
    # Add arguments
    parser.add_argument('-H', '--hostname', type=str, help='Router name', required=True)
    parser.add_argument('-u', '--username', type=str, help='NETCONF Username', required=True)
    # nargs='+' used because current password has several special characters....
    parser.add_argument('-p', '--password', type=str, help='NETCONF Password in single quotes...',
                        required=True, nargs='+')
    parser.add_argument('-f', '--vrf', type=str, help='VRF name', required=True)
    parser.add_argument('-t', '--destination', type=str, help='IP address to ping', required=True)
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")

    # Array for all arguments passed to script
    args = parser.parse_args()
    # print (args)
    # Assign args to variables
    hostname = args.hostname
    username = args.username
    password = args.password
    vrf = args.vrf
    destination = args.destination
    debug = args.debug
    # Return all variable values
    return hostname, username, password, vrf, destination, debug


# Read in Arguments passed to the script
remote_host, remote_username, remote_password, vrf, destination, debug = get_args()
print(type(remote_password))
remote_password = remote_password[0]
print(type(destination))
# use IPv4 because IPv6 connectivity to netconf port is currently blocked.....
remote_host_ipv4 = (socket.gethostbyname(remote_host))

# invoke as
# (.venv) dlete@TICTAC:/workspace/sandbox_pyez$ python incinga_vrf_ping.py -H dist2-testlab.nn.hea.net -u heanet -p '$!3u$uxqDMTXzw9' -f scoil_l3vpn.20200507 -t 10.11.12.13
print(remote_host, remote_username, remote_password, vrf, destination, debug)
print(remote_host_ipv4, remote_username, remote_password, vrf, destination, debug)


### Connect to box
try:
  dev=Device(host=remote_host, user=remote_username, password=remote_password, gather_facts=False, normalize=True)
  dev.open()
except ConnectError as err:
  print("Cannot connect to device: {0}".format(err))
  powerStatus = ICINGA_CRITICAL
  sys.exit(powerStatus)
except Exception as err:
  print(err)
  powerStatus = ICINGA_WARNING
  sys.exit(powerStatus)


# execute command in NE, get the output as JSON
#outcome = dev.rpc.ping({'format': 'json'}, routing_instance=vrf, host=host)

outcome = dev.rpc.ping({'format': 'json'}, routing_instance=vrf, host=destination)
results_dict = outcome['ping-results'][0]   # dictionary where we find the success/failure

if 'ping-success' in results_dict:
    # outcome = "SUCCESS"
    outcome = ICINGA_OK
if 'ping-failure' in results_dict:
    # outcome = "FAILURE"
    outcome = ICINGA_CRITICAL

print(outcome)
dev.close()
sys.exit(outcome)
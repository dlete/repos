#!/usr/bin/env python3

def parallel_work_function(i, ne, username, password, vrf, hosts, debug_level='WARNING'):
    """Loops and waits in each loop

    Args:
        i(int): counter for parallel processing
    """

    import logging
    import time

    # Create a custom logger and set debug level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(debug_level)
    c_format = logging.Formatter('%(asctime)s: %(module)s: %(funcName)s: '
                                 + '%(lineno)d: %(name)s: %(levelname)s: %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    logger.debug("Start base common setup")
    time.sleep(2)

    dict_of_outcomes = {}
    for host in hosts:
        time.sleep(1)
        # print(host)
        dict_of_outcomes[host] = 'pass/fail'
    return (i, dict_of_outcomes)


def collect_result(result):
    global results
    results.append(result)


if __name__ == '__main__':
    import math
    import multiprocessing as mp
    import time

    i = 0
    ne = "dist2-testlab.nn.hea.net"
    username = "heanet"
    password = "$!3u$uxqDMTXzw9"
    vrf = "scoil_l3vpn.20200507"
    host_4 = "10.11.12.13"          # does exist, should return success
    host_4_bogus = "1.1.1.1"        # does NOT exist, should return failure
    host_6 = "fd00:10:11:12::13"

    hosts_4 = [host_4] * 15
    hosts_6 = [host_6] * 15
    hosts_4_bogus = [host_4_bogus] * 1
    # hosts = hosts_4 + hosts_6 + hosts_4_bogus
    hosts = [item for pair in zip(hosts_4, hosts_6) for item in pair] + hosts_4_bogus
    debug_level = 'DEBUG'
    debug_level = 'INFO'

    print(f"We will be processing {len(hosts)} hosts")

    # ONE SESSION, ALL HOSTS
    print("Start ONE SESSION, ALL HOSTS")
    timer_one_start = time.perf_counter()
    results = parallel_work_function(i, ne, username, password, vrf, hosts, debug_level)
    print("Results of ONE SESSION, ALL HOSTS")
    print(results)
    timer_one_end = time.perf_counter()
    print(("Time to execute ONE session, ALL hosts, begin to end: "
          + f"{timer_one_end - timer_one_start:0.2f} seconds"))

    # PARALLEL
    number_of_cpu = int(mp.cpu_count())
    print(f"we will be using {number_of_cpu} CPU")
    number_of_hosts = int(len(hosts))
    hosts_per_sublist = math.ceil(number_of_hosts/number_of_cpu)

    # https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    list_of_lists = [hosts[i:i + hosts_per_sublist]
                     for i in range(0, len(hosts), hosts_per_sublist)]
    print("This is the list of sublists")
    print(list_of_lists)

    # ASYNCHRONOUS
    print("Start parallel ASYNCHRONOUS")
    timer_async_start = time.perf_counter()
    results = []
    pool = mp.Pool(number_of_cpu)
    for i, sublist in enumerate(list_of_lists):
        pool.apply_async(parallel_work_function,
                         args=(i, ne, username, password, vrf, sublist, debug_level),
                         callback=collect_result)

    pool.close()
    pool.join()
    print("Results of Parallel Asynchronous")
    print(results)
    timer_async_end = time.perf_counter()
    print(("Time to execute in parallel asynchronous, begin to end: "
          + f"{timer_async_end - timer_async_start:0.2f} seconds"))

    # SYNCHRONOUS
    print("Start parallel SYNCHRONOUS")
    timer_sync_start = time.perf_counter()
    pool = mp.Pool(number_of_cpu)
    results = [pool.apply(parallel_work_function,
                          args=(i, ne, username, password, vrf, sublist, debug_level))
               for sublist in list_of_lists]
    pool.close()
    print("Results of Parallel Asynchronous")
    print(results)
    timer_sync_end = time.perf_counter()
    print(("Time to execute in parallel Synchronous, begin to end: "
          + f"{timer_sync_end - timer_sync_start:0.2f} seconds"))

# Troubleshoot multicast

pim joins with
show pim neighbor detail
look for "Rx Join: Group"

## HEAnet groups

```vim
233.4.189.33
233.4.189.34
233.4.189.35
233.4.189.36
233.4.189.37
233.4.189.38
233.4.189.39
```

## find UNI

```vim
dlete@core1-cwt> show bgp summary | find 20965

62.40.125.125         20965    3593419    1308243       0       1 61w3d 19:45:08 Establ
  inet.0: 16421/18709/18709/0
  inet.2: 2139/2196/2196/0
83.97.88.73           21320   19554630    1307752       0       1 61w3d 19:45:00 Establ
  inet.0: 214676/317832/317826/0
87.44.48.5             1213  222177117   30526709       0       6 72w5d 23:03:10 Establ
  inet.0: 479327/479327/479327/0
  inet.2: 1081/1081/1081/0
  inet.3: 0/1/1/0
  inetflow.0: 19/19/19/0
```

```bash
{master}
dlete@core1-cwt> show pim interfaces ae200.12

Stat = Status, V = Version, NbrCnt = Neighbor Count,
S = Sparse, D = Dense, B = Bidirectional,
DR = Designated Router, DDR = Dual DR, DistDR = Distributed DR,
P2P = Point-to-point link, P2MP = Point-to-Multipoint,
Active = Bidirectional is active, NotCap = Not Bidirectional Capable

Name               Stat Mode IP V State        NbrCnt JoinCnt(sg/*g) DR address
ae200.12           Up   S     4 2 DR,NotCap         1 1/0            62.40.125.126
ae200.12           Up   S     6 2 NotDR,NotCap      1 0/0            fe80::ae4b:c800:c43:7fc2

{master}
dlete@core1-cwt>
```

## find what groups are joined by neighbor

```bash
{master}
dlete@core1-cwt> show pim neighbors detail | find ae200.12
Interface: ae200.12

    Address: 62.40.125.125,     IPv4, PIM v2, sg Join Count: 1, tsg Join Count: 0
        BFD: Disabled
        Hello Option Holdtime: 105 seconds 100 remaining
        Hello Option DR Priority: 1
        Hello Option Generation ID: 256022011
        Hello Option LAN Prune Delay: delay 500 ms override 2000 ms
                                      Join Suppression supported
        Hello Option Join Attribute supported
    Rx Join: Group           Source          Timeout
             224.2.127.254   193.1.186.55        192
             224.2.127.254   193.1.186.56        192
             224.2.127.254   193.1.186.57        192
             224.2.127.254   193.1.186.58        192
             224.2.127.254   193.1.186.59        192
             224.2.127.254   193.1.186.60        192

    Address: 62.40.125.126,     IPv4, PIM v2, Mode: Sparse, sg Join Count: 0, tsg Join Count: 0
        Hello Option Holdtime: 65535 seconds
        Hello Option DR Priority: 1
        Hello Option Generation ID: 41307739
        Hello Option LAN Prune Delay: delay 500 ms override 2000 ms
                                      Join Suppression supported
        Hello Option Join Attribute supported

Interface: ae3.0

    Address: 87.44.56.221,      IPv4, PIM v2, Mode: Sparse, sg Join Count: 0, tsg Join Count: 0
        Hello Option Holdtime: 65535 seconds
        Hello Option DR Priority: 254
        Hello Option Generation ID: 647183224
        Hello Option LAN Prune Delay: delay 500 ms override 2000 ms
                                      Join Suppression supported
        Hello Option Join Attribute supported

    Address: 87.44.56.222,      IPv4, PIM v2, sg Join Count: 0, tsg Join Count: 0
        BFD: Disabled
        Hello Option Holdtime: 105 seconds 89 remaining
        Hello Option DR Priority: 1

{master}
dlete@core1-cwt>
```

## who is joining what groups

```bash
{master}
dlete@core1-cwt> show pim join extensive | find 233.4.189.33

Pattern not found
{master}
dlete@core1-cwt>

{master}
dlete@core1-cwt>

{master}
dlete@core1-cwt> show pim join extensive
Instance: PIM.master Family: INET
R = Rendezvous Point Tree, S = Sparse, W = Wildcard

Group: 224.0.1.140
    Source: 193.147.114.5
    Flags: sparse
    Upstream interface: ae200.12
    Upstream neighbor: 62.40.125.125
    Upstream state: Local RP, Join to Source
    Keepalive timeout:
    Uptime: 7w6d 14:07:45
    Downstream neighbors:
        Interface: et-8/0/0.0
            87.44.50.5 State: Join Flags: S Timeout: 186
            Uptime: 7w6d 14:07:45 Time since last Join: 00:00:24
    Number of downstream interfaces: 1
    Number of downstream neighbors: 1

Group: 224.2.127.254
    Source: 193.1.186.55
    Flags: sparse,spt
    Upstream interface: et-8/0/0.0
    Upstream neighbor: 87.44.50.5
    Upstream state: Local RP, Join to Source
    Keepalive timeout: 313
    Uptime: 1d 15:35:33
    Downstream neighbors:
        Interface: ae200.12
            62.40.125.125 State: Join Flags: S Timeout: 205
            Uptime: 1d 15:35:33 Time since last Join: 00:00:05
    Number of downstream interfaces: 1
    Number of downstream neighbors: 1

Group: 224.2.127.254
    Source: 193.1.186.56
    Flags: sparse,spt
    Upstream interface: et-8/0/0.0
    Upstream neighbor: 87.44.50.5
    Upstream state: Local RP, Join to Source
    Keepalive timeout: 313
    Uptime: 1d 15:35:33
    Downstream neighbors:
        Interface: ae200.12
            62.40.125.125 State: Join Flags: S Timeout: 205
            Uptime: 1d 15:35:33 Time since last Join: 00:00:05
    Number of downstream interfaces: 1
    Number of downstream neighbors: 1

Group: 224.2.127.254
    Source: 193.1.186.57
```

## show multicast route

```bash
dlete@core1-blanch> show multicast route active detail
Instance: master Family: INET

Group: 233.4.189.33
    Source: 193.1.186.55/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 528 kBps, 570 pps, 658342824 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.34
    Source: 193.1.186.56/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 585 kBps, 548 pps, 548703233 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.35
    Source: 193.1.186.57/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 164 kBps, 312 pps, 456644573 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.36
    Source: 193.1.186.58/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 487 kBps, 488 pps, 588473592 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.37
    Source: 193.1.186.59/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 394 kBps, 407 pps, 688127503 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.38
    Source: 193.1.186.60/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 560 kBps, 545 pps, 701026303 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 233.4.189.39
    Source: 193.1.186.61/32
    Upstream interface: et-0/0/0.0
    Downstream interface list:
        ae2.0
    Session description: GLOP Block
    Statistics: 441 kBps, 415 pps, 606998964 packets
    Next-hop ID: 1048578
    Upstream protocol: PIM

Group: 239.255.255.250
    Source: 193.1.219.10/32
    Upstream interface: ae2.0
    Downstream interface list:
        et-0/0/0.0
    Session description: Organisational Local Scope
    Statistics: 0 kBps, 0 pps, 2 packets
    Next-hop ID: 1048701
    Upstream protocol: PIM

Instance: master Family: INET6

dlete@core1-blanch>
```

## MSDP own cache

```bash
dlete@core1-pw> show msdp source-active local
Global active source limit exceeded: 0
Global active source limit maximum: 25000
Global active source limit threshold: 24000
Global active source limit log-warning: 100
Global active source limit log interval: 0

Group address   Source address  Peer address    Originator      Flags
224.2.127.254   193.1.186.55    local           87.44.48.2      Accept
224.2.127.254   193.1.186.56    local           87.44.48.2      Accept
224.2.127.254   193.1.186.57    local           87.44.48.2      Accept
224.2.127.254   193.1.186.58    local           87.44.48.2      Accept
224.2.127.254   193.1.186.59    local           87.44.48.2      Accept
224.2.127.254   193.1.186.60    local           87.44.48.2      Accept
228.1.255.5     193.1.255.4     local           87.44.48.2      Accept
233.4.189.33    193.1.186.55    local           87.44.48.2      Accept
233.4.189.34    193.1.186.56    local           87.44.48.2      Accept
233.4.189.35    193.1.186.57    local           87.44.48.2      Accept
233.4.189.36    193.1.186.58    local           87.44.48.2      Accept
233.4.189.37    193.1.186.59    local           87.44.48.2      Accept
233.4.189.38    193.1.186.60    local           87.44.48.2      Accept
233.4.189.39    193.1.186.61    local           87.44.48.2      Accept
239.174.90.209  134.226.249.158 local           87.44.48.2      Accept
239.255.2.2     134.226.4.118   local           87.44.48.2      Accept
239.255.250.250 10.13.1.158     local           87.44.48.2      Accept
239.255.250.251 10.13.1.7       local           87.44.48.2      Accept
239.255.250.251 10.13.1.9       local           87.44.48.2      Accept
239.255.250.251 10.23.16.16     local           87.44.48.2      Accept
239.255.250.251 10.23.32.15     local           87.44.48.2      Accept
239.255.250.251 10.23.32.17     local           87.44.48.2      Accept
239.255.255.250 10.7.160.95     local           87.44.48.2      Accept
239.255.255.250 10.10.152.27    local           87.44.48.2      Accept
239.255.255.250 10.10.180.13    local           87.44.48.2      Accept
239.255.255.250 10.10.226.14    local           87.44.48.2      Accept
239.255.255.250 10.10.226.15    local           87.44.48.2      Accept
239.255.255.250 10.23.0.111     local           87.44.48.2      Accept
239.255.255.250 10.23.0.113     local           87.44.48.2      Accept
239.255.255.250 10.23.0.114     local           87.44.48.2      Accept
239.255.255.250 10.23.0.115     local           87.44.48.2      Accept
239.255.255.250 10.23.0.128     local           87.44.48.2      Accept
239.255.255.250 10.23.0.129     local           87.44.48.2      Accept
```

## MSDP source-active

```bash
{master}
dlete@core1-pw> show msdp source-active
```

and

```bash
{master}
dlete@core1-pw> show route table inet.4

```

are equivalent

## MSDP see what SA we send

```bash
msdp {
    traceoptions {
        file msdp-debug;
        flag general detail;
        flag source-active detail;
    }
}
```

## Links

[Juniper KB, Resolution Guide - Troubleshoot Multicast issue with Junos OS device configured as Layer 3 (running PIM protocol)](https://kb.juniper.net/InfoCenter/index?page=content&id=KB21586&actp=METADATA)

<https://archive.nanog.org/meetings/nanog27/presentations/caron.pdf>

<http://hydra.ck.polsl.pl/~helot/ipad/JNCIE/Ch4_from_JNCIE_studyguide.pdf>

<https://www.juniper.net/documentation/en_US/junos/topics/topic-map/mcast-msdp.html#jd0e1945>

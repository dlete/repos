
def my_function(ne):
    import socket
    print(ne)
    ne_ext = socket.getaddrinfo(ne, None, socket.AF_INET6)
    print(ne_ext)
    ne_ext = socket.getaddrinfo(ne, None)
    print(ne_ext)
    ne_ipv6 = socket.getaddrinfo(ne, None, socket.AF_INET6)[0][4][0]
    print(ne_ipv6)
    ne_ipv4 = socket.getaddrinfo(ne, None, socket.AF_INET)[0][4][0]
    print(ne_ipv4)


if __name__ == '__main__':
    ne = 'edge3-testlab.nn.hea.net'

    my_function(ne)

from ipaddress import ip_address

file_nets = open('ip_solve.log', 'w')

mask = int(ip_address(input()))

for i in open("ip.log").readlines():
    i = i.replace('\n', '')
    i = int(ip_address(i))
    net = ip_address(i & mask)
    file_nets.write(str(net) + '\n')


#  255.255.254.0
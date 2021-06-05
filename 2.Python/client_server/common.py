import netifaces
IPADDR = netifaces.ifaddresses("wlp0s20f3")[2][0]['addr']
PORT = 6677


# import argparse
import datetime
import psutil
import time
import sys
import numpy as np
import pandas as pd
import ipaddress as ipa
import collections as cl
from scanner.models import DataTemp
import json

from socket import AF_INET, AF_INET6, SOCK_DGRAM, SOCK_STREAM

if sys.platform.startswith('linux') or sys.platform == 'darwin':
    PLATFORM = 'nix'
    from os import geteuid
elif sys.platform.startswith('win'):
    PLATFORM = 'win'
    from ctypes import *
else:
    print('Error: Platform unsupported.')
    sys.exit(1)

PROTOCOLS = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6'
}
FIELDS = ['proto', 'laddr', 'lport', 'raddr', 'rport', 'status', 'pid',
          'pname', 'time', 'date', 'user', 'command']
P_FIELDS = '{:<5} {:<15.15} {:<5} {:<15.15} {:<5} {:<11} {:<5} {:<20.20} ' \
           '{:<8} {:<8} {:<20.20} {}'


def histinit():
    header = ''
    root_check = False

    if PLATFORM == 'nix':
        if geteuid() == 0:
            root_check = True
    elif PLATFORM == 'win':
        if windll.shell32.IsUserAnAdmin() == 0:
            root_check = True

    if not root_check:
        header += '(Not all process information could be determined, run' \
                  ' at a higher privilege level to see everything.)\n'


        # if prettify:
        #     header += P_FIELDS.format(*FIELDS)
        # else:
        #     header += '\t'.join(FIELDS)
        # histlog(header)


def histmain(interval):
    connections_A = psutil.net_connections()
    for c in connections_A:
        if c.status == "ESTABLISHED":
            process_conn(c)
    
    start = time.time()
    while time.time() - start <=10:
        # time.sleep(interval)

        connections_B = psutil.net_connections()
        for c in connections_B:
            if c not in connections_A:
                if c.status == "ESTABLISHED":
                    process_conn(c)

        connections_A = connections_B


def process_conn(c):
    date, time = str(datetime.datetime.now()).split()

    proto = PROTOCOLS[(c.family, c.type)]
    raddr = rport = ' '
    status = pid = pname = user = command = ' '
    laddr, lport = c.laddr

    if c.raddr:
        raddr, rport = c.raddr
    if c.pid:
        try:
            pname, pid = psutil.Process(c.pid).name(), str(c.pid)
            user = psutil.Process(c.pid).username()
            command = ' '.join(psutil.Process(c.pid).cmdline())
        except:  # if process closes too quickly
            pass
    if c.status != 'NONE':
        status = c.status

    cfields = [proto, laddr, lport, raddr, rport, status, pid, pname,
               time[:8], date, user, command]

    date_str = date
    date_formatter_string = "%Y-%m-%d"
    date_datetime_object = datetime.datetime.strptime(date_str, date_formatter_string)
    date_object = date_datetime_object.date()

    time_str = time[:8]
    time_formatter_string = "%H:%M:%S"
    time_datetime_object = datetime.datetime.strptime(time_str, time_formatter_string)
    time_object = time_datetime_object.time()

    ob = DataTemp()
    ob.Protocol = proto
    ob.Date = date_object
    ob.ListenAddress = laddr
    ob.ListenPort = lport
    ob.RemoteAddress = raddr
    ob.RemotePort = rport
    ob.Status = status
    ob.Time = time_object
    ob.save();
def stop():
    sys.exit()

#     if prettify:
#         line = P_FIELDS.format(*cfields)
#     else:
#         line = '\t'.join(map(str, cfields))
#     return line
#
#
# def histlog(line):
#     print(line)
#     a=5





def main():
    # global ob

    while DataTemp.objects.count():
        ids = DataTemp.objects.values_list('pk', flat=True)[:100]
        DataTemp.objects.filter(pk__in=ids).delete()

    global interval
    interval = 1

    global prettify
    prettify = False

    histinit()
    histmain(interval)
    # return DataTemp.objects.all()
    # data_port = DataTemp.objects.values('RemotePort')
    # data_ip = DataTemp.objects.values('RemoteAddress')
    port_dict = {20: 'ftp1', 21: 'ftp2', 22: 'ssh', 23: 'telnet', 25: 'smtp', 53: 'dns', 67: 'dhcp1', 68: 'dhcp2',
                 69: 'tftp', 80: 'http', 110: 'pop3', 123: 'ntp', 143: 'imap', 161: 'snmp1', 162: 'snmp2', 179: 'bgp',
                 389: 'ldap', 443: 'https'}
    names = []
    names_public = ["Local", "Remote"]
    addr = DataTemp.objects.values('RemoteAddress')
    addr2=[]
    port = DataTemp.objects.values('RemotePort')
    port2 = []
    for addr1 in addr:
        addr2 = addr2+[addr1['RemoteAddress']]
    for port1 in port:
        port2 = port2+[port1['RemotePort']]
    # print(arr.values())
    # print(type(arr.values))
    # time.sleep(5)
    aa = np.array(addr2)
    bb = np.array(port2)
    names = []
    private_ports = []
    public_ports = []
    local = 0
    remote = 0
    for i in range(0, len(aa)):
        if ipa.ip_address(aa[i]).is_private:
            private_ports = private_ports + [bb[i]]
            local = local + 1
        else:
            public_ports = public_ports + [bb[i]]
            remote = remote + 1
    # count=[local,remote]

    cnt_dict_public = cl.Counter(public_ports)
    cnt_dict_private = cl.Counter(private_ports)
    cnt_dict_result = cnt_dict_private + cnt_dict_public
    public = []
    private = []
    # print(cnt_dict_result)

    for key in cnt_dict_result.keys():
        if (port_dict.get(key) == None):
            names = names + [str(key)]
        else:
            names = names + [port_dict[key]]
        if (cnt_dict_public.get(key) == None):
            public = public + [0]
        else:
            public = public + [cnt_dict_public[key]]
        if (cnt_dict_private.get(key) == None):
            private = private + [0]
        else:
            private = private + [cnt_dict_private[key]]
    # print(names)
    # print(public)
    # print(private)
    dicta = {}
    for i in range(0, len(names)):
        s1 = {"Local": str(private[i]), "Remote": str(public[i])}
        # s1 = {"Local": private[i], "Remote": public[i]}
        dicta[names[i]] = s1
    dicta = json.dumps(dicta)
    # print(dicta)
    return dicta
if __name__ == '__main__':
    main()

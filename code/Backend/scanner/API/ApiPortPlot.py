import collections as cl
import numpy as np
import pandas as pd
# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.offline as poff
# import ipaddress as ipa
from scanner.models import Data
def plotting():

    #sample=pd.read_csv("I:\\SIH Project\\Navneet\\hc\\sample2.csv")
    # print(sample)
    data1 = Data.objects.values('RemotePort')

    # port_dict={20:'ftp1',21:'ftp2',22:'ssh',23:'telnet',25:'smtp',53:'dns',67:'dhcp1',68:'dhcp2',69:'tftp',80:'http',110:'pop3',123:'ntp',143:'imap',161:'snmp1',162:'snmp2',179:'bgp',389:'ldap',334:'trojan',443:'https'}
    # names = [""]
    # a=[]
    # for datap in data1:
    #     a=a+[datap['RemotePort']]
    # # print(a)
    # cnt_dict=cl.Counter(a)
    # port_num = list(cnt_dict.keys())
    # port_count =list(cnt_dict.values())
    #
    # l=len(port_num)
    # names=names*l
    # print(names)
    #
    # for i in range(0,l):
    #     x=port_num[i]
    #     print(x)
    #     if port_dict.get(x,None)!=None:
    #         names[i]=port_dict[port_num[i]]
    #         print("iffffff")
    #         # print(names[i])
    #     else:
    #         names[i]='others'
    #
    # fig = {
    #     "data": [
    #     {
    #         "values": port_count,
    #         "labels": names,
    #         "domain": {"x": [0.33, .66]},
    #         "name": "Share",
    #         "hoverinfo":"label+percent+name+value",
    #         "hole": .3,
    #         "type": "pie"
    #     }],
    #     "layout": {
    #         "title":"Share of ports from 00:00 to 24:59",
    #         "annotations": [
    #         {
    #             "font": {
    #                 "size": 20,
    #                 "color": '#AAAAAA'
    #             },
    #             "showarrow": False,
    #             "text": "protocols",
    #             "x": 0.5,
    #             "y": 0.5
    #         }]
    #     }
    # }
    # poff.plot(fig)

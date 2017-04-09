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
    data1 = Data.objects.values('RemoteAddress')
    # print(data1)
    # for data in data1:
    #     print (data['RemoteAddress'])
    # names=["Local","Remote"]
    # local=0
    # remote=0
    # # srcIp = ipaddress.ip_network(u'10.0.0.0/24')
    # for data in data1:
    #     if ipa.ip_address(data['RemoteAddress']).is_private:
    #         local=local+1
    #     else:
    #         remote=remote+1
    # count=[local, remote]
    # fig = {
    #   "data": [
    #     {
    #       "values": count,
    #       "labels": names,
    #       "domain": {"x": [0.33, .66]},
    #       "name": "IP Share",
    #       "hoverinfo":"label+percent+name+value",
    #       "hole": .3,
    #       "type": "pie"
    #     }],
    #   "layout": {
    #         "title":"Share of local and remote from 00:00 to 24:59",
    #         "annotations": [
    #             {
    #                 "font": {
    #                     "size": 20,
    #                     "color": '#AAAAAA'
    #                 },
    #                 "showarrow": False,
    #                 "text": "User type share",
    #                 "x": 0.5,
    #                 "y": 0.5
    #             }
    #         ]
    #     }
    # }
    # poff.plot(fig)

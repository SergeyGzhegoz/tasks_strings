model = {"TE100-S5":
             {"product Title": "5-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1Gbps",
              "MAC adress entries": "2k",
              "Enclozure Material": "Plactic"},
         "TE100-S8":
             {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1.6Gbps",
              "MAC adress entries": "2k",
              "Enclozure Material": "Plactic"},
         }

for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]['MAC adress entries'] == "2k":
        print(model[switch])

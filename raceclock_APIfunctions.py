# Script with functions to interact with the raceresult API through requests
# Created 20-9-2026 by Jan

import requests
import json
import xml.etree.ElementTree as ET

# Inputs
# None

# Example get eventid: http://192.168.12.11/api/local/eventlist?&lang=en
# Result: [{"ID":"414218","FileName":"VMC_2026-2027_Nunspeet Werk.ses","EventName":"Veluwse MTB Competitie 2026/2027","EventDate":"2026-10-24","CheckedOut":false,"Participants":208,"NotActivated":0,"EventLogo":"logo_VMC.png","EventType":2}]

# Example url2 get API key: http://192.168.12.11/_414218/api/simpleapi/get?&lang=en&pw=0
# Result: [{"Disabled":false,"Key":"MOQVKU55PZPUR0I0SK5TE64AR2J664RY","URL":"data/list?\u0026fields=HeatFinished,HeatCountUp,HeatCountDown,HeatLaps\u0026filter=[ID]=1","Label":""}]

# Example url API request initiated in raceclock_webinterface.py
# http://192.168.12.11/_414218/api/MOQVKU55PZPUR0I0SK5TE64AR2J664RY
#Result:
# <list>
#  <record>
#   <HeatFinished>0</HeatFinished>
#   <HeatCountUp>00:28:05</HeatCountUp>
#   <HeatCountDown>01:21:54</HeatCountDown>
#   <HeatLaps>03:00:00</HeatLaps>
#  </record>
# </list>

def fetcheventidAPIkey(IP):
    eventid = "0"
    APIkey = "0"
    url1 = f"http://{IP}/api/local/eventlist"
    foundAPI = True

    try:
        r = requests.get(url1, params={"lang": "en"}, timeout=5)
        eventid = str(r.json()[0]["ID"])
        print(eventid)

    except Exception as e:
        print(e)
        foundAPI = False
        
    if foundAPI:
        url2 = f"http://{IP}/_{eventid}/api/simpleapi/get"

        try:
            r = requests.get(url2, params={"lang": "en", "pw": "0"}, timeout=5)
            APIkey = str(r.json()[0]["Key"])
            print(APIkey)

        except Exception as e:
            print(e)
            foundAPI = False

    return foundAPI, eventid, APIkey


def fetchdata(url):
    foundAPI = True
    
    try:
        response = requests.get(url,timeout=1)
        content = response.content
        root = ET.fromstring(content)

    except Exception as e:
        print(e)
        foundAPI = False  

    if foundAPI:
        elem = root[0]
        HF = bool(int(elem[0].text))
        HCUtxt= elem[1].text
        if HCUtxt is not None:
            HCU = HCUtxt[0:8]
        else:
            HCU = "00:00:00"
        HCDtxt= elem[2].text
        if HCDtxt is not None:
            HCD = HCDtxt[0:8]
        else:
            HCD = "00:00:00"
        HLtxt= elem[3].text
        if HLtxt is not None:
            HL = HLtxt[0:8]
        else:
            HL = "00:00:00"
    else:
        HF = 0
        HCU = "00:00:00"
        HCD = "00:00:00"
        HL = "00:00:00"

    return foundAPI, HF, HCU, HCD, HL

# foundAPI, eventid, APIkey = fetcheventidAPIkey()
# url = "http://"+IP+"/_"+eventid+"/api/"+APIkey

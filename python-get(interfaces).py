import requests
import json
from requests import auth
import urllib3, xmltodict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.0.100"
authdata=('admin','cisco123')
headers = {'Accept': 'application/yang-data+json','Content-Type':'application/yang-data+json'}

def uri(host,parameters):
        baseUri = "https://"+ host + parameters
        return baseUri

baseUri=uri(host,"/restconf/data/ietf-interfaces:interfaces-state/")
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
print ("All Interfaces")
print (json.dumps(data, indent=4))
#Data type List [0] = GigabitEhternet1
print ("Interface G1")
print (json.dumps((data["interfaces-state"]["interface"][0]),indent=4))

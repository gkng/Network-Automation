import requests
import json
from requests import auth
import urllib3, xmltodict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.0.100"
intfname="GigabitEthernet2"
enstatus=False

authdata=('admin','cisco123')
headers = {'Accept': 'application/yang-data+json','Content-Type':'application/yang-data+json'}

def uri(host,parameters):
        baseUri = "https://"+ host + parameters
        return baseUri

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": intfname,
    "enabled": enstatus
  }
})

baseUri=uri(host,"/restconf/data/ietf-interfaces:interfaces/interface")
getdata = requests.request("PATCH", baseUri, headers=headers, data=payload, auth=authdata, verify=False)

#Check interface status
baseUri=uri(host,"/restconf/data/ietf-interfaces:interfaces/interface=") + intfname
getdata = requests.request("GET", baseUri, headers=headers, auth=authdata, verify=False)
jdata=json.loads(getdata.text)
#print (json.dumps(jdata , indent=4))
print (f"Interface {intfname} 'Enabled' Status: ")
print (jdata["ietf-interfaces:interface"]["enabled"])
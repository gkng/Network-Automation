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

baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native")
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
#print (json.dumps(data, indent=2))
print ("Hostname:" + host )
print ("ios :" + data["native"]["version"])
print ("Cisco Module:" + data["native"]["license"]["udi"]["pid"])
print ("Serial Number:" + data["native"]["license"]["udi"]["sn"])
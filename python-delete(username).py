import requests
import json
from requests import auth
import urllib3, xmltodict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.0.100"
authdata=('admin','cisco123')
headers = {'Accept': 'application/yang-data+json','Content-Type':'application/yang-data+json'}

def uri(host,parameters,username):
        baseUri = "https://"+ host + parameters + username
        return baseUri

username = input ("Enter user to delete:")

baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native/username=",username)
print(baseUri)

payload={}
deletedata = requests.request("DELETE", baseUri, auth=authdata, headers=headers, data=payload, verify=False)



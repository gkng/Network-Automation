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

username = input ("Enter new user:")
#print(f"new user: {username}")


baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native/")
payload = json.dumps({
  "Cisco-IOS-XE-native:username": [
    {
      "name": username,
      "privilege": 15,
      "password": {
        "encryption": "0",
        "password": "cisco123"
      }
    }
  ]
})

postdata = requests.request("POST", baseUri, headers=headers, auth=authdata, data=payload ,  verify=False)
print(f"Added user {username}")




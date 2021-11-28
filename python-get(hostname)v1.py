import requests
import json
from requests import auth
import urllib3, xmltodict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.0.100"
baseUri = "https://"+ host +"/restconf/data/Cisco-IOS-XE-native:native"
headers = {"Content-Type":"application/json"}

#print (baseUri)
getdata = requests.get(baseUri, auth=('admin','cisco123'), verify=False)
data=(xmltodict.parse(getdata.content))
#print (data)
print (json.dumps(data, indent=2))
print (data["native"]["hostname"])
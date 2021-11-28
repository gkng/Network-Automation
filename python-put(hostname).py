import requests
import json
from requests import auth
import urllib3, xmltodict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host="192.168.0.100"
hostname = "myRouter"
authdata=('admin','cisco123')
headers = {'Accept': 'application/yang-data+json','Content-Type':'application/yang-data+json'}

#Hostname before change
baseUri = "https://"+ host +"/restconf/data/Cisco-IOS-XE-native:native/"
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
#print (json.dumps(data, indent=2))
print ("hostname before change :" + data["native"]["hostname"])

#Change hostname
baseUri = "https://"+ host +"/restconf/data/Cisco-IOS-XE-native:native/hostname"
payload = json.dumps({
  "Cisco-IOS-XE-native:hostname": hostname
})
putdata = requests.request("PUT", baseUri, headers=headers, auth=authdata, data = payload, verify=False)
#Verify hostname change
baseUri = "https://"+ host +"/restconf/data/Cisco-IOS-XE-native:native"
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
print ("hostname:" + data["native"]["hostname"])

#Save Configuration
baseUri = "https://"+ host +"/restconf/operations/cisco-ia:save-config/"
payload={}
savedata = requests.request("POST", baseUri, headers=headers, auth=authdata,data = payload, verify=False)

print(savedata.text)
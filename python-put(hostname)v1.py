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

hostname = input ("Enter new hostname:")
print(f"new hostname: {hostname}")

#Hostname before change
baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native/")
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
#print (json.dumps(data, indent=2))
print ("hostname before change :" + data["native"]["hostname"])

#Change hostname
baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native/hostname")
payload = json.dumps({
  "Cisco-IOS-XE-native:hostname": hostname
})
putdata = requests.request("PUT", baseUri, headers=headers, auth=authdata, data = payload, verify=False)
#Verify hostname change
baseUri=uri(host,"/restconf/data/Cisco-IOS-XE-native:native/")
getdata = requests.get(baseUri, auth=authdata, verify=False)
data=(xmltodict.parse(getdata.content))
print ("hostname:" + data["native"]["hostname"])

#Save Configuration
baseUri=uri(host,"/restconf/operations/cisco-ia:save-config/")
payload={}
savedata = requests.request("POST", baseUri, headers=headers, auth=authdata,data = payload, verify=False)
#print(savedata.text)

jsavedata = json.loads(savedata.text)
print(jsavedata["cisco-ia:output"]["result"])
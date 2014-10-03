#######################################
# Title: Get group place ID
# Description: Gets a list places and their palceIDs for use in other URIs
#           Update community base URL, username, and password.
# Author: Timothy Hales
# Date: 10/3/2014
# Version: 1.0
# Python Version: 2.7
# Jive Rest API: v3
# GitHub Repository: https://github.com/thales007/Jive-Community-Management
#######################################
import json, base64, requests

#Search keyword
keyword = "training,example"
maxReturn = 100 #100 is the max for returned groups.

uri = "/api/core/v3/places?filter=search({})&count={}".format(keyword,maxReturn)
base_url = "https://community.com" #Community base URL
url = base_url + uri

#Define headers
user = "username" #User must have social group permissions
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");
headers = { "Content-Type": "application/json", "Authorization": auth }

#Send get request
req = requests.get(url, headers=headers )
data = req.content

#Remove security header
data2 = data.replace("throw 'allowIllegalResourceCall is false.';", "")
#print data2
jsonData = json.loads(data2)

#print jsonData
#Add place name and placeID to a dictionary.
placeDict = {}
for dataItem in jsonData["list"]:
    name = dataItem["displayName"]
    name2 = name.encode('ascii', 'replace')
    placeID = dataItem["placeID"]
    #print "{}: {}".format(name2, "placeID") 
    #spaceList.append(placeID)
    placeDict.update({name2: placeID})

#Print the place and placeID in a dictionary
print placeDict

 


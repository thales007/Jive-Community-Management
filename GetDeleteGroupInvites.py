#######################################
# Title: Get and Delete group invites
# Description: Gets a list of invite IDs and deletes them from the group.
#       There is no notification to the user of the invited being recinded.
#       Update community base URL, username, and password.
# Author: Timothy Hales
# Date: 10/6/2014
# Version: 1.1
# Python Version: 2.7
# Jive Rest API: v3
# GitHub Repository: https://github.com/thales007/Jive-Community-Management
#######################################
import json, base64, requests

#Variables
placeID = "2322" #Place id from GetGroupInfo.py
maxReturn = 100 #Max number of invites to process. 100 is max.
totalInvites = 391 #Number of invites in group. Loops through invites based upon maxReturn value untill all invites are gotten.
listInvites = False #List invite IDs
removeInvites = True #Remove invites
start = 0 #startIndex
inviteList = []
name = ""

#Define headers
user = "username" #User must have social group permissions
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");
headers = { "Content-Type": "application/json", "Authorization": auth }


#Group invites uri
uri = "/api/core/v3/invites/places/{}?count={}".format(placeID,maxReturn)
base_url = "https://community.com" #Community base URL
url = base_url + uri


#Loop through and compile all invites
while (start < totalInvites):
    #Group invites uri
    uri = "/api/core/v3/invites/places/{}?count={}&startIndex={}".format(placeID,maxReturn,start)
    base_url = "https://geonet.esri.com"
    url = base_url + uri
    start += maxReturn
    #Define headers

    try:
        #Create list of invite IDs
        req = requests.get(url, headers=headers)
        data = req.content

        #Remove security header
        data2 = data.replace("throw 'allowIllegalResourceCall is false.';", "")
        #Load json with request text
        jsonData = json.loads(data2)
        #print jsonData

        if jsonData["list"]:
            if name != "":
                pass
            else:
                name = jsonData["list"][0]["place"]["name"]
                name2 = name.encode('ascii', 'replace')
                print "Group: {}".format(name2)

        #If there json data exists continue process
            for dataItem in jsonData["list"]:
               
                inviteList.append(dataItem["id"])
            
        else:
            print "No invites exist for group: {}".format(group)

    except requests.HTTPError, e:
        print e.code
        print e.read()
        print unicode(req.message, errors="ignore")
        json.decoder.errmsg
    print "{} invites compiled".format(len(inviteList))

if listInvites == True:
    print "{} invites compiled".format(len(inviteList)) 
    print inviteList

#Delete invites from list
if removeInvites == True:
    
    print "Removing {} invites".format(len(inviteList))

    nInvites = len(inviteList)
    remaining = 0
    for i in inviteList:
        uri2 = "/api/core/v3/invites/{}".format(i)
        url2 = base_url + uri2
        req2 = requests.delete(url2, headers=headers)
        remaining = remaining + 1
        print "Removed invite {} of {}".format(remaining, nInvites)

    print "Removed all group invites"
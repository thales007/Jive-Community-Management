#######################################
# Title: Get and Delete group invites
# Description: Gets a list of invite IDs and deletes them from the group.
#       There is no notification to the user of the invited being recinded.
#       Update community base URL, username, and password.
# Author: Timothy Hales
# Date: 10/3/2014
# Version: 1.0
# Python Version: 2.7
# Jive Rest API: v3
# GitHub Repository: https://github.com/thales007/Jive-Community-Management
#######################################
import json, base64, requests

#Variables
group = 1090 #Group ID from
placeID = "2322" #Place id from GetGroupInfo.py
maxReturn = 100 #Max number of invites to process. 100 is max.
listInvites = True #List invite IDs
removeInvites = False #Remove invites


#Group invites uri
#uri = "/api/core/v2/invites?groupID={}&limit={}".format(group, maxReturn)
uri = "/api/core/v3/invites/places/{}?count={}".format(placeID,maxReturn)
base_url = "https://community.com" #Community base URL
url = base_url + uri

#Define headers
user = "username" #User must have social group permissions
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");
headers = { "Content-Type": "application/json", "Authorization": auth }

try:
    #Create list of invite IDs
    req = requests.get(url, headers=headers)
    data = req.content

    #Remove security header
    data2 = data.replace("throw 'allowIllegalResourceCall is false.';", "")
    ##Load json with request return text
    jsonData = json.loads(data2)
    #print jsonData

    inviteList = []

    if jsonData["list"]:
        name = jsonData["list"][0]["place"]["name"]
        name2 = name.encode('ascii', 'replace')
        print "Group: {}".format(name2)

    #If there json data exists continue process
        for dataItem in jsonData["list"]:
           
            inviteList.append(dataItem["id"])

        if listInvites == True:
            print "{} Invites".format(len(inviteList)) 
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
        
    else:
        print "No invites exist for group: {}".format(group)

except requests.HTTPError, e:
    print e.code
    print e.read()
    print unicode(req.message, errors="ignore")
    json.decoder.errmsg

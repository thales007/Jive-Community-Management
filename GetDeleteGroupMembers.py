#######################################
# Title: Get and Delete group members
# Description: Gets a list of member IDs and deletes them from the group.
#       Update community base URL, username, and password.
# Author: Timothy Hales
# Date: 10/7/2014
# Version: 1.0
# Python Version: 2.7
# Jive Rest API: v3
# GitHub Repository: https://github.com/thales007/Jive-Community-Management
#######################################
import json, base64, requests, time

group = "1000"
placeID = "1000"
maxReturn = 100 #Max number of members to process per loop. 100 is max.
totalMembers = 100 #Number of members in group. Loops through members based upon maxReturn value untill all invites are gotten.
#listInvites = False #List invite IDs
#removeInvites = True #Remove invites
start = 0 #startIndex
memberList = []
name = ""

startTime = time.time()

#Define Headers
user = "username" #User must have social group permissions
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");
headers = { "Content-Type": "application/json", "Authorization": auth }

while (start < totalMembers): 
    #Group members uri
    uri = "/api/core/v3/members/places/{}?count={}&startIndex={}".format(placeID,maxReturn,start)
    base_url = "https://community.com"
    url = base_url + uri
    start += maxReturn

    try:
        #Create list of member IDs
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
                name = jsonData["list"][0]["group"]["name"]
                name2 = name.encode('ascii', 'replace')
                print "Group: {}".format(name2)

            for dataItem in jsonData["list"]:
                if dataItem["state"] == "member":
                    memberList.append(dataItem["id"])

        else:
            print "No members exist for group: {}".format(group)

    except:
        pass
    print "Removing {} members".format(len(memberList))

startDeleteTime = time.time()
compileTime = startDeleteTime - startTime


nMembers = len(memberList)
remaining = 0
for m in memberList:
    uri2 = "/api/core/v3/members/{}".format(m)
    url2 = base_url + uri2
    req2 = requests.delete(url2, headers=headers)
    remaining = remaining + 1
    print "Removed member {} of {}".format(remaining, nMembers)
    
print "Removed all members"

finishedDeleteTime = time.time()
print "Compile Time: {}".format(compileTime/60)
print "Delete Time: {}".format((finishedDeleteTime - startDeleteTime)/60)
print "Total Time: {}".format((finishedDeleteTime - startTime)/60)


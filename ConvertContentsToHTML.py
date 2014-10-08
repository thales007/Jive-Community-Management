#######################################
# Title: Convert Content to HTML
# Description: Concerts content from a space and creates HTML files.
# Author: Timothy Hales
# Date: 10/7/2014
# Version: 1.0
# Python Version: 2.7
# Jive Rest API: v3
#######################################
import json, base64, requests, time, string

#Variables
placeID = "1045"
maxReturn = 100 #Max number of content items to process at one time
totalContent = 577 #Number of content items in place
start = 0 #startIndex
cCount = 0 
contentType = "document" #content filter
workspace = r"C:\folder" #folder to put files

startTime = time.time()

user = "username" #User must have admin permissions
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");
headers = { "Content-Type": "application/json", "Authorization": auth }

#Loop through and compile all invites
while (start < totalContent):
    #Group invites uri
    uri = "/api/core/v3/places/{}/contents?count={}&startIndex={}".format(placeID,maxReturn,start)
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

        for dataItem in jsonData["list"]:
            if dataItem["type"] == contentType:
                cCount += 1
                subject = dataItem["subject"]
                
                #Remove punctuation from subject to be used in file name
                exclude = set(string.punctuation)
                subject = ''.join(ch for ch in subject if ch not in exclude)                
                body = dataItem["content"]["text"]

                #Create HTML files                
                htmlFile = open("{}\\{}.html".format(workspace,subject),"w")               
                htmlFile.write(body)
                htmlFile.close()

    except requests.HTTPError, e:
        print e.code
        print e.read()
        print unicode(req.message, errors="ignore")
        print json.decoder.errmsg

#Calculate processing time
finishTime = time.time()
totalTime = finishTime - startTime

print "Converted {} files in {} seconds".format(cCount,round(totalTime),2)
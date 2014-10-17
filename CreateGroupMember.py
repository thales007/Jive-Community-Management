#######################################
# Title: Create Group Member
# Description: Creates an group member.
#           There cannot be an outstanding invite for the person.
# Author: Timothy Hales
# Date: 10/17/2014
# Version: 1.0
# Python Version: 2.7
# Jive Rest API: v3
#######################################
import requests, json, base64

placeID = 2322
personID = 72898 


uri = "/api/core/v3/members/places/{}".format(placeID)
base_url = "https://geonet.esri.com"
url = base_url + uri

user = "username"
password = "password"

auth = "Basic " + base64.encodestring('%s:%s' % (user, password)).replace("\n","");

headers = { "Content-Type": "application/json", "Authorization": auth }

data = json.dumps(
     {
      "person" : "https://example.jiveon.com/api/core/v3/people/{}".format(personID),
      "state" : "member"
  })

try:
    req = requests.post(url, data=data, headers=headers )
    print "Member Created"
except:
    print req.text

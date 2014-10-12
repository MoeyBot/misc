#!/usr/bin/env python

# This is a test script to verify 
# access to Dropbox

#  Make sure you install the dropbox module first of course, pip install dropbox.

 #   Create an app under your own dropbox account in the "App Console". (https://www.dropbox.com/developers/apps)

#    a. App Type as "Dropbox API APP".

#    b. Type of data access as "Files & Datastores"

#   c. Folder access as "My app needs access to files already on Dropbox". (ie: Permission Type as "Full Dropbox".)

# Then click the "generate access token" button and cut/paste into the python example below in place of <auth_token>:


import dropbox, os

client = dropbox.client.DropboxClient('<auth-token')


filelist = [ f for f in os.listdir(".") if f.endswith(".zip") ]
# f = open(str(filelist), 'rb')
# response = client.put_file('/', f)
for f in filelist:
        i = open
        response = client.put_file

print "uploaded:", response


#!/usr/bin/env python

# This is a test script to verify 
# access to Dropbox

#  Make sure you install the dropbox module first of course, pip install dropbox.

 #   Create an app under your own dropbox account in the "App Console". (https://www.dropbox.com/developers/apps)

#    a. App Type as "Dropbox API APP".

#    b. Type of data access as "Files & Datastores"

#   c. Folder access as "My app needs access to files already on Dropbox". (ie: Permission Type as "Full Dropbox".)

#    Then click the "generate access token" button and cut/paste into the python example below in place of <auth_token>:

# v01 - Moey

import dropbox

client = dropbox.client.DropboxClient(<auth_token>)
print 'linked account: ', client.account_info()

f = open('working-draft.txt', 'rb')
response = client.put_file('/moey.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/moey.txt')
out = open('moey.txt', 'wb')
out.write(f.read())
out.close()
print metadata

#!/usr/bin/env python
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
 
# Get your app key and secret from the Dropbox developer website
APP_KEY = 'fill here'
APP_SECRET = 'fill here'
 
# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'
 
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
request_token = sess.obtain_request_token()
url = sess.build_authorize_url(request_token)
 
# Make the user sign in and authorize this token
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()
 
# This will fail if the user didn't visit the above URL
access_token = sess.obtain_access_token(request_token)
 
#Print the token for future reference
print access_token.key
print access_token.secret
#!/usr/bin/env python
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
 
# Get your app key and secret from the Dropbox developer website
APP_KEY = 'fill here'
APP_SECRET = 'fill here'
 
# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'
 
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
 
# We will use the OAuth token we generated already. The set_token API
# accepts the oauth_token and oauth_token_secret as inputs.
sess.set_token("fill here","fill here")
 
# Create an instance of the dropbox client for the session. This is
# all we need to perform other actions
client = client.DropboxClient(sess)
 
# Let's upload a file!
f = open('dropbox-upload.py')
response = client.put_file('/dropbox-upload.py', f)
print "uploaded:", response
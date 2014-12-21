#!/usr/bin/env python

# Master script to backup my home directory
# upload to dropbox and delete the file
# written by Moey

# Let's get the things we are going to use
import zipfile, os, datetime
from dropbox import client, rest, session

# Grab today's date
today = datetime.date.today()
 
 # First things first let's backup everything in our home directory
def makeArchive(fileList, archive):
    try:
        a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
        for f in fileList:
            a.write(f)
        a.close()
        return True
    except: return False
 
def dirEntries(dir_name, subdir, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not args:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
        # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and subdir:
            print "Accessing directory:", dirfile
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList

# These are the backup directly and file name info here....edit at your discretion 
if __name__ == '__main__':
    folder = r'/home/username'
    zipname = r'vpsbu_'
    zipname += str(today)
    zipname += r".zip"
    makeArchive(dirEntries(folder, True), zipname)
 
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
f = open("zipname")
response = client.put_file(zipname, f)

# Let's delete the local file which we just created
filelist2 = [ f for f in os.listdir(".") if f.endswith(".zip") ]
for f in filelist2:
    os.remove(f)
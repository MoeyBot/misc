#!/usr/bin/env python

# Master script to backup my home directory upload
# to dropbox and delete the file

# ################################################
# Updated Feb 2017                              ## 
# Changes due to Dropbox API v1 Depreciation    ## 
# ################################################

# written by Moey

# Let's get the things we are going to use
import zipfile, os, datetime, dropbox, urllib3
urllib3.disable_warnings()


# Grab today's date
today = datetime.date.today()
 
# First things first let's backup everything in our home directory
def makeArchive(fileList, archive):
    """
    'fileList' is a list of file names - full path each name
    'archive' is the file name for the archive with a full path
    """
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
 
if __name__ == '__main__':
    folder = r'/home/secmoey/'
    zipname = r'vpsbu_'
    zipname += str(today)
    zipname += r".zip"
    makeArchive(dirEntries(folder, True), zipname)
 
# Alright let's start doing our Dropbox Stuff
access_token = 'your_token_here'

# Create a dropbox object using an API v2 key
dbx = dropbox.Dropbox(access_token)

# open the file and upload it
dbx.files_upload("zipname", '/APIv2/backup')

# Done with the Dropbox stuff - Finishing up
# Let's delete this file locally now
filelist2 = [ f for f in os.listdir(".") if f.endswith(".zip") ]
for f in filelist2:
    os.remove(f)
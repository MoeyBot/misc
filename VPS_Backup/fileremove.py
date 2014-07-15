#!/usr/bin/env python

import glob, os

filelist = glob.glob(".zip")
for f in filelist:
	os.remove(f)
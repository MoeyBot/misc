#!/usr/bin/env python

# This script pulls from Amazon EC2
# Security Groups and all the ingress
# rules for the enviroments

# written by Moey 
# 09/12/2013

# Let's start this

import boto
import os
import pprint

# We have to specify our credentials

ACCESS_KEY="#youraccesskey#"
SECRET_KEY="#yoursecretkey#"

# This is how we connect to EC2
ec2 = boto.connect_ec2(ACCESS_KEY, SECRET_KEY)

# Let's make this pretty
pp = pprint.PrettyPrinter(indent=5)
pq = pprint.PrettyPrinter(indent=10)

# For each Security Group let's get name and Rules
rs = ec2.get_all_security_groups()
for sg in rs:
	sgn = sg.name
	sgr = sg.rules
	pp.pprint(sgn)
	pq.pprint(sgr)

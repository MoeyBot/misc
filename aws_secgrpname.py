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

# Let's tell them our secrets

ACCESS_KEY="#youraccesskey#"
SECRET_KEY="#yoursecretkey#"

# This is how we connect to EC2
ec2 = boto.connect_ec2(ACCESS_KEY, SECRET_KEY)

# Let's make this pretty
pp = pprint.PrettyPrinter(indent=5)

# Let's get all the groups and print them
rs = ec2.get_all_security_groups()
i = 0
opts = {}
print "\nCurrent list of Security Groups."
pp.pprint(rs)

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
import sys

#Let's tell them our secrets

ACCESS_KEY="#youraccesskey#"
SECRET_KEY="#yoursecretkey#"

# This is how we connect to EC2
ec2 = boto.connect_ec2(ACCESS_KEY, SECRET_KEY)

# Let's get all the instance info and when it was launched.
instances = ec2.get_all_instances()
i = 0
opts = {}
print "\nCurrently running instances:"
for r in instances:
  for inst in r.instances:
    opts[i] = (inst.id, inst.instance_type, inst.public_dns_name, inst.launch_time)
    print "\t%d:" % i + " %s - %s : %s (Running since: %s)" % opts[i]
    i += 1

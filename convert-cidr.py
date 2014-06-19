#!/usr/bin/env python3
import ipaddress
import sys
import argparse

parser = argparse.ArgumentParser(description='Split cidr network. Example: echo 192.168.1.0/24 | ./convert-cidr.py -n 25')
parser.add_argument('-n', '--netmask', type=int, help='Subnetwork netmask. ie. 32 or 24')

args = parser.parse_args()

line = input()
try:
   for subnet in ipaddress.ip_network(line.strip()).subnets(new_prefix=args.netmask):
       print(subnet)
except ValueError:
  print('Value Error: New prefix must be longer')

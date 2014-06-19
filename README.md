python
======

PinGwynn's python scripts

convert-cidr.py - split some CIDR network to smoller networks with specified prefix

example:
  
    $ echo 192.168.1.0/24 | ./convert-cidr.py -n 25
    192.168.1.0/25
    192.168.1.128/25

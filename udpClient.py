#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import argparse

parser = argparse.ArgumentParser(description='This is a simple script of UDP client')
parser.add_argument("-t", metavar="TARGET HOST", help="target host", required=True)
parser.add_argument("-p", metavar="TARGET PORT", type=int, help="target port", required=True)

args = parser.parse_args()

target_host = args.t
target_port = args.p

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect to server
client.connect((target_host,target_port))

# send data
client.send(b"Hello World!\r\n")

# response data
response = client.recv(4096)

print(response)

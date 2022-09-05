# Docker Monitoring Code 
# Imported libraries
from socket import *
import subprocess
import time
import pandas as pd
import re
import sys
import pickle
from collections import defaultdict
import json

# Initalizes variable on the client side to connect with main manager mgr-1
hosts = "34.72.103.76"
port = 5678
addr = (hosts, port)
usc = socket(AF_INET, SOCK_DGRAM)

# Initalize present time for 3 second loop as well as keys for the data dictionary
starttime=time.time()
data_keys = ['WorkerID','ImageID','ContainerID','CPU Usuage','Memory Usuage','Network Usuage I/O','Block Usuage I/O','Dominate Type']
#data_keys2 = ['ImageID','CPU Usuage','Memory Usuage','Network Usuage I/O','Block Usuage I/O','Dominate Type']

itime = 3#float(sys.argv[2])
while True:
        # Runs the docker stats command with no stream and puts it's output into text
        command  = ['sudo', 'docker', 'stats', '--no-stream']
        command2 = ['sudo', 'docker', 'container', 'ls']

        p = subprocess.Popen(command,stdout=subprocess.PIPE)
        p2 = subprocess.Popen(command2,stdout=subprocess.PIPE)

        # For docker stats read text and split by line
        text = p.stdout.read()
        retcode = p.wait()
        textsplit = text.splitlines()

        # For docker container ls read and split text
        ctext = p2.stdout.read()
        cretcode = p2.wait()
        ctextsplit = ctext.splitlines()

        # Initalize the data dictionary and the data frame to empty 
        images = defaultdict(list)
        data = dict((x,[]) for x in data_keys)
        df = pd.DataFrame(data, columns=data_keys)
        # For every line in text 
        for element in textsplit[1:]:
                # Every line is split by word 
                x = element.split()
                for line in ctextsplit[1:]:
                        y = line.split()
                        if y[0] == x[0]:
                                data["ImageID"].append(y[1])
                data["WorkerID"].append("w1")
                # Check if ContainerID is already in data
                if x[0] not in data["ContainerID"]:
                        # If a new Container calculate the dominate resource between CPU and Memory
                        dom = "Equal Usuage"
                        if float(x[2].strip('%')) > float(x[6].strip('%')) :
                                dom = "CPU"
                        if float(x[2].strip('%')) < float(x[6].strip('%')):
                                dom = "Memory"
                        # Add values to data dictionary with respective keys
                        data["ContainerID"].append(x[0])
                        data["CPU Usuage"].append(x[2])
                        data["Memory Usuage"].append(x[6])
                        data["Network Usuage I/O"].append(x[7]+x[8]+x[9])
                        data["Block Usuage I/O"].append(x[10]+x[11]+x[12])
                        data["Dominate Type"].append(dom)

        # Recalualte the new dataframe based on the data
        df = pd.DataFrame(data, columns=data_keys)
        # Print statement for testing
        print(df)
        bits = df.to_json().encode()
        usc.sendto(bits,addr)
        time.sleep(itime)
usc.close()

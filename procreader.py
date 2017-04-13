import os,datetime

def answer1(): # Number of cpus clock speed number of cores
    with open("/proc/cpuinfo","r") as infile:
        numberofcpus=0
        clockspeeds=[]
        numberofcores=[]
        for line in infile.readlines():
            if(line=='\n'):
                numberofcpus+=1
            elif(line.split()[0]=="cpu" and line.split()[1]=="MHz"):
                clockspeeds.append(line.split()[3])
            elif(line.split()[0]=="cpu" and line.split()[1]=="cores"):
                numberofcores.append(line.split()[3])
        print("1. Number of Processors : " + str(numberofcpus) + "\n")
        for i in range(numberofcpus):
            print("CPU # " + str(i) + "\n  Clock Speed : " + str(clockspeeds[i]) + "\n  Number of Cores: " + str(numberofcores[i]) + "\n")
        
        
def answer2(): # Version of linux kernel
    with open("/proc/version", 'r') as infile:
        for line in infile:
            print("2. Version of Linux Kernel : "  + line.split()[2] ) 
            return;

def answer3(): # Time in day:hr:min:sec when syst was last booted

    with open("/proc/uptime","r") as infile:
        for line in infile:
            intime = float(line.split()[0])
        ans = datetime.timedelta(seconds=intime)
        print("\n3. Time since last reboot: " + str(ans) + "\n")
def answer4(): # Average load in last 15 min
    pass
def answer5(): # Total usable and free memory
    pass
def answer6(): # Total swap space and currently used swap space
    pass
answer1()
answer2()
answer3()

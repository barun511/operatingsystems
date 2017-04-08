import os
import psutil
import signal
import random
from time import sleep
firstchildin, firstchildout = os.pipe()
pid = os.fork()
if pid:
    os.close(firstchildout)
    secondchildin, secondchildout = os.pipe()
    ppid = os.fork()
    if ppid:
        os.close(secondchildout)
        firstreadobject = os.fdopen(firstchildin)
        secondreadobject = os.fdopen(secondchildin)
        print("this is parent and I am receiving as follows")
        leftchildscore = 0
        rightchildscore = 0
        random.seed(5131)
        sleep(0.25)
        while True:
            leftchildnumber = (firstreadobject.readline())
            rightchildnumber = (secondreadobject.readline())
            print("left child gave " + str(leftchildnumber))
            print("right child gave " + str(rightchildnumber))
            min_or_max = random.randint(0,1) # If 0 then we pick MIN else we pick MAX
            if min_or_max==0:
                print("We picked min this time")
                if(leftchildnumber < rightchildnumber):
                    leftchildscore +=1
                elif(rightchildnumber < leftchildnumber):
                    rightchildscore+=1 
            else:
                print("We picked max this time")
                if(rightchildnumber > leftchildnumber):
                    rightchildscore+=1
                elif(leftchildnumber > rightchildnumber):
                    leftchildscore+=1   
            print("The current scores are \n left child : " + str(leftchildscore) + " right child: " + str(rightchildscore)+ '\n' + '\n')
            if leftchildscore==10 or rightchildscore==10:
                break
            sleep(1)
        if leftchildscore==10:
            print("First child won! Woohoo!")
        else:
            print("Right child won!")
        print("Sending kill signal")
        parent = psutil.Process(os.getpid())
        for child in parent.children():
            child.kill()
        parent.kill()
        # This is the parent, and it will randomly pick MIN or MAX and then read values from the pipe.
    else:
        os.close(secondchildin)
        os.close(firstchildin)
        writeobject = os.fdopen(secondchildout, 'w')
        while True:
            number = random.randint(0,10)
            #print("Second child picked this number " + str(number))
            writeobject.write(str(number))
            writeobject.write("\n")
            writeobject.flush()
            sleep(1)
else:
    os.close(firstchildin)
    random.seed(1001)
    # This is first child, and every one second it will randomly pick an integer and write it to the pipe
    writeobject = os.fdopen(firstchildout, 'w')
    while True:
        number = random.randint(0,10)
        #print("First child picked this number " + str(number))
        writeobject.write(str(number))
        writeobject.write("\n")
        writeobject.flush()
        sleep(1)

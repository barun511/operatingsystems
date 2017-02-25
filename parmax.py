import os
import sys
from time import sleep
array = list(map(int, input().split()))
print("Initially unsorted array")
print(array)
originalprocesspid = os.getpid()
def calculate(array):
    if len(array) <= 10: # Base case for recursion
        return max(array)
    else:
        divide = int(len(array)/2)
        maxleft = -1
        maxright = -1
        firstchildin, firstchildout = os.pipe()
        pid = os.fork()
        if pid==0:  # First child, this will recursively calculate the maximum of left array
            os.close(firstchildin) # Close the read end of pipe1
            print("This is child process, and will calculate ")
            print(array[:divide])
            writeobject = os.fdopen(firstchildout, 'w')
            writeobject.write(str(calculate(array[:divide])) )
            writeobject.close()
            exit(0)
        else:
            os.close(firstchildout)
            secondchildin, secondchildout = os.pipe()
            ppid = os.fork()
            if ppid:
                os.close(secondchildout)
                os.waitpid(pid, 0)
                os.waitpid(ppid,0)
                firstreadobject = os.fdopen(firstchildin)
                secondreadobject = os.fdopen(secondchildin)  
                print("About to read") 
                leftchildmax = int(firstreadobject.read())
                rightchildmax = int(secondreadobject.read())
                print("text = ", leftchildmax)
                print("text = ", rightchildmax)
                return max(leftchildmax, rightchildmax)
            else:
                os.close(secondchildin)
                print("This is second child and will calculate")
                print(array[divide:])
                writeobject = os.fdopen(secondchildout, 'w')
                writeobject.write(str(calculate(array[divide:])))
                writeobject.close()
                exit(0) 

# There 
j = calculate(array)

#if os.getpid()==originalprocesspid:
if True:
    print(j)

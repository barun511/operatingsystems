#!/usr/bin/python3
import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# file descriptors r, w for reading and writing
r, w = os.pipe() 

processid = os.fork()
if processid:
   # This is the parent process 
   # Closes file descriptor w
   os.close(w)
   r = os.fdopen(r)
   print ("Parent reading")
   tr = r.read()
   print ("text =", tr   )
else:
   # This is the child process
   os.close(r)
   w = os.fdopen(w, 'w')
   print ("Child writing")
   w.write("Text written by child...")
   print ("Child closing")


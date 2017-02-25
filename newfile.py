import os
r, w = os.pipe()
pid = os.fork()
if pid:
    os.close(w)
    r = os.fdopen(r)
    print("parent reading")
    text  = r.read()
    print("text =", text)
else:
    os.close(r)
    w = os.fdopen(w, 'w')
    print("Child writing")
    w.write("Text written by child")
    print ("Child done writing")

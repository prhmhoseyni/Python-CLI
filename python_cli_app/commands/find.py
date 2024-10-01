import os
def run(path , pattern):

    for p , d , f in os.walk(path) :
        for n in f : 
            n.find(pattern) 
            print(n)
            return
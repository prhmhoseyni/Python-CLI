import os
def run(path) :
# Change to the directory specified by the path
    os.chdir(path)
# Verify the current working directory
    print("Current working directory: ") , os.getcwd(path)
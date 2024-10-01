import os
def make_directory(src):
    if not os.path.exists(src):
        os.mkdir(src)
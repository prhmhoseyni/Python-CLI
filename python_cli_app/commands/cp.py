import shutil
import os
def run(src, distination):
    if os.path.isfile(src):
        shutil.copy(src,distination)
    elif os.path.isdir(src):
        shutil.copytree(src,distination)
    else:
        print(f'{src} is neither a file nor a directory')


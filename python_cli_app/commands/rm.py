import os
import shutil
from termcolor import colored


def run(source, recursive=False):

    if os.path.isfile(source):

        os.remove(source)

        print(colored(f"✅ Removed file: \"{source}\"", "green"))

    elif os.path.isdir(source):

        if recursive:

            shutil.rmtree(source)

            print(colored(f"✅ Removed directory and contents: \"{source}\"", "green"))

        else:

            print(colored(f"❌ \"{source}\" is a directory. Use -r to remove it recursively.", "red"))
    
    else:
        
        print(colored(f"❌ \"{source}\" does not exist.", "red"))

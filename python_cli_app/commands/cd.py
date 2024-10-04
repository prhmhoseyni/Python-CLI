import os
from termcolor import colored

def run(path):

    if os.path.isdir(path):

        try:

            os.chdir(path)

            print(colored(f"✅ Changed directory to: \"{os.getcwd()}\"", "green"))

        except Exception as error:

            print(colored(f"❌ Error changing directory to \"{path}\": {error}", "red"))

    else:
        
        print(colored(f"❌ Directory \"{path}\" does not exist.", "red"))

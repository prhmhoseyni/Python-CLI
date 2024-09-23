import os
from termcolor import colored


def run(source):

    try:

        os.rmdir(source)

        print(colored(f"✅ Removed empty directory: \"{source}\".", "green"))

    except OSError as error:

        if error.errno == 39:  # Check Directory Mot empty

            print(colored(f"❌ \"{source}\" is not empty.", "red"))

        else:

            print(colored(f"❌ \"{error}\".", "red"))

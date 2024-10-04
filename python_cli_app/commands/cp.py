import shutil
import os
from termcolor import colored


def run(source, destination):

    if os.path.exists(source):

        try:

            if os.path.isfile(source):

                shutil.copy(source, destination)

                print(colored(f"✅ File copied \"{source}\" to \"{destination}\"", "green"))

            elif os.path.isdir(source):

                shutil.copytree(source, destination, dirs_exist_ok=True)

                print(colored(f"✅ Directory copied \"{source}\" to \"{destination}\"", "green"))

        except Exception as error:

            print(colored(f"❌ Error copying \"{source}\" to \"{destination}\": {error}", "red"))

    else:

        print(colored(f"❌ \"{source}\" does not exist.", "red"))

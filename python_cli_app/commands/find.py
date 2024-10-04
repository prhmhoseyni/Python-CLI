import os
from termcolor import colored


def run(path, pattern):

    if os.path.isdir(path):

        try:

            for root, dirs, files in os.walk(path):

                for file in list(filter(lambda x: x.split(".")[-1] == pattern, files)):

                    print(colored(f"{os.path.join(root, file)}", "light_grey"))

        except Exception as error:

            print(colored(f"❌ Error searching for pattern \"{pattern}\" in path \"{path}\": {error}", "red"))

    else:

        print(f"Path '{path}' does not exist.")

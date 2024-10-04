import os
from termcolor import colored


def run(file_path):

    if os.path.isfile(file_path):
        try:

            with open(file_path, "r") as file:

                contents = file.read()

                print(contents)

        except FileNotFoundError:

            print(colored(f"❌ Error: The file \"{file_path}\" does not exist.", "red"))

        except Exception as error:

            print(colored(f"❌ Error: {error}", "red"))

    else:

        print(colored(f"❌ \"{file_path}\" does not exist.", "red"))

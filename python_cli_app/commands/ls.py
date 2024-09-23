import os
from termcolor import colored


def run(path):

    print(colored(f"\n\"{path}\"\n", "blue"))

    for item in os.listdir(path):

        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):

            print(colored(f"{item}/", "light_cyan"))

        elif os.path.isfile(item_path):

            print(colored(f"{item}", "light_grey"))

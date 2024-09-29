import shutil
from termcolor import colored


def run(source, destination):

    try:
        shutil.move(source, destination)

        print(colored(f"✅ Moved \"{source}\" to \"{destination}\"", "green"))

    except FileNotFoundError:

        print(colored(f"❌ \"{source}\" not found.", "red"))

    except PermissionError:

        print(colored(f"❌ Permission denied when moving \"{
              source}\" to \"{destination}\"", "red"))

    except Exception as error:

        print(colored(f"❌ {error}", "red"))

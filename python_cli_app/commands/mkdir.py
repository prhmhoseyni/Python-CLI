import os
from termcolor import colored

def run(source, dir_name):

    new_dir_path = os.path.join(source, dir_name)

    try:
        
        os.makedirs(new_dir_path, exist_ok=True)
        
        print(colored(f"✅ Directory \"{dir_name}\" created successfully in \"{source}\".", "green"))
    
    except Exception as error:
    
        print(colored(f"❌ Error creating directory \"{dir_name}\" in \"{source}\": {error}", "red"))

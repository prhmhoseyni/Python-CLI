from datetime import datetime

def log_command(command):
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{now}: {command}\n"
    
    with open("app.log", "a") as log_file:
        
        log_file.write(log_entry)
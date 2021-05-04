import os.path
import utilities as u
from datetime import datetime

def add():
    u.clear_screen()

    hours = input("Hours:\n>>")
    when = input("Between: ")
    today = datetime.now()
    date_formatted = today.strftime("%d/%m/%Y")
    formatted_string = date_formatted + ";" + hours + ";" + when + "\n"

    this_month = today.strftime("%B")
    filename = f"/Users/bjornandersson/vim/work/hourApp/logs/log_{this_month}.txt"

    saved_hours = f'saved {hours} hours between {when} on {date_formatted}'    

    if os.path.isfile(filename):
        file = open(filename, "a")
        file.write(formatted_string)
        file.close()
        print()
        print(saved_hours)
        print()
        nothing = input('Press any key to show menu')
    else:
        file = open(filename, "x")
        file.close()
        
        print()
        print(f'created new file: {filename}')
        print(saved_hours)
        print()
        nothing = input('Press any key to show menu')

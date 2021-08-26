# Copyright (c) 2021 Björn Andersson
#
# This work is licensed under the MIT license, see the file LICENSE for details.

import os.path
import utilities as u
from datetime import datetime

def add():
    u.clear_screen()

    hours = input("Hours:\n>>")
    when = input("Between:\n>>")
    project_code = input("Project code:\n>>")
    today = datetime.now()
    date_formatted = today.strftime("%d/%m/%Y")
    _,week,_ = today.isocalendar()
    formatted_string = f"{week};{date_formatted};{hours};{when};{project_code}\n"

    this_month = today.strftime("%B")
    filename = f"/Users/bjornandersson/vim/work/hourApp/logs/log_{this_month}.txt"

    saved_hours = f'saved {hours} hours between {when} on {date_formatted} on project: {project_code}'    

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

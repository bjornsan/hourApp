# Copyright (c) 2021 Björn Andersson
#
# This work is licensed under the MIT license, see the file LICENSE for details.

import os.path
import utilities as u

def read(fName):

    u.clear_screen()

    if (len(fName) < 10):
        filename = f"/Users/bjornandersson/vim/work/hourApp/logs/log_{fName}.txt"
    else:
        filename = f"/Users/bjornandersson/vim/work/hourApp/logs/{fName}"
        
    if os.path.isfile(filename):
        file = open(filename, "r")
        lines = file.readlines()
	
        print("Week:\tDate:\t\tHours:\t\tTime:\t\tPrject:")	

        sum_hours = 0
        salary = 186
        week = 0

        for line in lines:
            count = line.split(";")
            if len(count) < 5:
                date, hours, time, project_code = no_weeks(line)
                sum_hours = sum_hours + hours
                print(f"\t{date}\t{hours}\t\t{time}\t\t{project_code} ")
            else:
                read_week, date, hours, time, project_code = read_weeks(line)
                sum_hours = sum_hours + hours
                if read_week != week:
                    week = read_week
                    print(f"{week}\t{date}\t{hours}\t\t{time}\t\t{project_code} ")
                    print("--------------------------------------------------------")
                else:       
                    print(f"\t{date}\t{hours}\t\t{time}\t\t{project_code} ")

        sum_salary = sum_hours*salary
        print()
        print(f"Total hours: {sum_hours}")
        print()
        print(f"Salary before tax: {round(sum_salary, 2)}")
        print(f"Salary after tax: {round(sum_salary * 0.68, 2)}")
        print()	
        file.close()

        nothing = input("Press any key to show menu")
    else:
        print("file not available")

def no_weeks(line):
    date = line.split(";")[0]
    hours = float( line.split(";")[1] )
    time = line.split(";")[2]
    project_code = line.split(";")[3]
    return date, hours, time, project_code

def read_weeks(line):
    read_week = line.split(";")[0]
    date = line.split(";")[1]
    hours = float( line.split(";")[2] )
    time = line.split(";")[3]
    project_code = line.split(";")[4]
    return read_week, date, hours, time, project_code

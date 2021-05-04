from add_hour_app import add as add
from read_hour_app import read as read
from datetime import date
import utilities as u
import os

def show_menu():
    print('*****************************')
    print('**********HOURS APP**********')
    print('*****************************')
    print()
    print('1: Add hours')
    print('2: show this months hours')
    print('3: choose month')
    print('q to quit')
    print()
    print()


is_running = True
while(is_running):
    
    u.clear_screen()
    
    show_menu()

    option = input('Your will is my command:\n>> ')
    
    if option == '1':
        add()
    elif option == '2':
        this_month = date.today().strftime('%B')
        read(this_month)
    elif option == '3':
        path = "/Users/bjornandersson/vim/work/hourApp/logs"
        arr = os.listdir(path)

        u.clear_screen()
        
        print('Files in directory')
        print()

        for index, file in enumerate(arr):
            print(index, file)
        
        secondOption = int(  input('\nChoose file to read\n>> ') )

        if ( secondOption  >= 0 and secondOption < len(arr)):
            read(arr[secondOption])
	 

    if option == 'q':
        is_running = False



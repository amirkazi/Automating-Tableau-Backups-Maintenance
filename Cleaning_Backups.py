import os
import time

# directory = "E:\Tableau_Backups"
directory = "E:\Backups"

if os.path.exists(directory) :
    os.chdir(directory)
    print("Current Working Directory " , os.getcwd())


    list_of_backups = []
    for file in os.listdir():
        if file.endswith('tsbak'):
            list_of_backups.append(file)

    # Calculates epoch time to find .tsbak files beyond a certain date
    Number_of_days_since_today = 1
    Minimum_number_of_backups = 4
    now = time.time()
    for file in os.listdir():
        if file.endswith('tsbak') and len(list_of_backups) >= Minimum_number_of_backups and \
            os.stat(file).st_ctime < now - (Number_of_days_since_today * 86400):
            print (file)

else:
    print("The directory does not exist.")  
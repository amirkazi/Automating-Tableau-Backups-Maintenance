'''
Use: Delete .tsbak tableau files that are out-dated and unnecessary
    using certain filters such as number of days elapsed, and the
    minimum number of backups

Written by: Amir Kazi : kazi@uchicago.edu
Date: 28th May 2020
'''
import os
import time

# Change below 3 variables for any future changes
directory = "E:\Tableau_Backups"
Number_of_days_since_today = 4
Minimum_number_of_backups = 4

if os.path.exists(directory) :
    os.chdir(directory)
    print("Current Working Directory " , os.getcwd())

    list_of_backups = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('tsbak'):
            list_of_backups.append(file)

    # Calculates epoch time to find .tsbak files beyond a certain date
    now = time.time()
    for file in list_of_backups:
        if len(list_of_backups) >= Minimum_number_of_backups and \
            os.stat(file).st_ctime < now - (Number_of_days_since_today * 86400):
            os.remove(file)
            print("File Removed: ", file)   
            
else:
    print("The directory does not exist.")  

:: Script to backup Tableau Data & Config File
:: Written by: Amir Kazi : kazi@uchicago.edu
:: Date: 27th May 2020

SET folder_path="E:\Tableau_Backups"
:: Use below command to change default data download folder
:: Changes the default folder path for backups
:: Reference: https://help.tableau.com/current/server/en-us/cli_default_filepaths_tsm.htm
::CALL tsm configuration set -k basefilepath.backuprestore -v %folder_path%


:: RUN PYTHON FILE
SET PYTHON_FILE_ADDRESS="C:\Scripts\Tableau_Data_Backup_Maintenance\Cleaning_Backups.py"
CALL python %PYTHON_FILE_ADDRESS%
ECHO %PYTHON_FILE_ADDRESS%
ECHO PYTHON FILE RAN


:: Creating data backup
SET backup_file_name=Internal_Backup
ECHO CREATING BACKUP. PLEASE WAIT.
CALL tsm maintenance backup -f %backup_file_name% -d --override-disk-space-check
ECHO BACKUP CREATED


:: Creating config file backup
CALL tsm settings export -f "%folder_path%\%backup_file_name%-config-settings.json"
ECHO CONFIG FILE CREATED 

::cmd /k

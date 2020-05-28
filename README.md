# Tableau-Backups-Maintenance
Contains scripts to download Tableau Server data via TSM, and clean the folder to delete outdated data files via Python.

There are 2 scripts:
1. Tableau_Backup_Data.cmd
2. Cleaning_Backups.py

Tableau_Backup_Data.cmd uses TSM (Tableau Server Manager) to download the Tableau Server backup file (.tsbak) 
and the associated config file to a default folder. The code on how to set the default folder has also been specified.

Cleaning_Backups.py cleans up the default folder ensuring that .tsbak files past an X number of days are deleted 
IF there are a Y number of backups already present.

These files were created for the Chicago Police Department Infrastructure team to automate the backup and maintenance process
via Windows Task Scheduler. 

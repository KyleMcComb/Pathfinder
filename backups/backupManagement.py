from django.core.management import call_command
from mysite.settings import *
from backups.azureBlobStorage import *

import os
import glob

"""
@Author: DeanLogan123
@Description: Initiates a database backup using Django's 'dbbackup' management command.
@return: True if the backup process was successful, False otherwise.
"""
def createBackupFile():
    try:
        call_command('dbbackup') # Triggers the database backup using Django's 'dbbackup' management command
        return True
    except:
        return False

"""
@Author: DeanLogan123
@Description: Deletes the oldest local backup file if the number of existing backup files exceeds a limit.
@return: True if a backup file was deleted successfully, False otherwise.
"""
def deleteOldestBackupFile():
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        if len(backupFiles) > 10:
            backupFiles.sort(key=os.path.getmtime) # Sort backup files by modification time (oldest first)
            
            # Delete the oldest backup file
            oldestBackup = backupFiles[0]
            os.remove(oldestBackup)
            return True
    except:
        return False

"""
@Author: DeanLogan123
@Description: Deletes the oldest backup blob from the Azure Blob Storage container if the number of blobs exceeds a limit.
@return: True if a blob was deleted successfully, False otherwise.
"""
def deleteOldestBackupBlob():
    containerClient = getContainerClient()
    blobList = containerClient.list_blobs()

    try:
        
        backupFiles = [(blob.name, blob.properties.last_modified) for blob in blobList] # Convert the blob list to a list of (blob_name, last_modified) tuples
        if len(backupFiles) > 20:
            backupFiles.sort(key=lambda x: x[1]) # Sort backup files by last_modified time (oldest first)
            
            # Delete the oldest backup blob
            oldestBackupName = backupFiles[0][0] 
            return deleteBlob(oldestBackupName)
        return False
    except:
        return False

"""
@Author: DeanLogan123
@Description: Uploads the latest local backup file to the Azure Blob Storage container.
@return: True if the upload was successful, False otherwise.
"""
def uploadLatestBackup():
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        backupFiles.sort(key=os.path.getmtime) # Sort backup files by modification time (oldest first)
        latestBackup = os.path.basename(backupFiles[-1])
        return uploadFileToBlob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], latestBackup), latestBackup)
    except:
        return False
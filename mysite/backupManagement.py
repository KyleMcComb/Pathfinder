from django.core.management import call_command
from django.http import JsonResponse
from mysite.settings import *
from mysite.azureBlobStorage import *

import os
import glob


def deleteOldestBackupFile():
    try:
        # Check the number of existing backup files
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump'))
        if len(backupFiles) > 10:
            # Sort backup files by modification time (oldest first)
            backupFiles.sort(key=os.path.getmtime)

            # Delete the oldest backup file
            oldestBackup = backupFiles[0]
            os.remove(oldestBackup)
            return True
    except:
        return False

def createBackupFile():
    try:
        # Triggers the database backup using Django's 'dbbackup' management command
        call_command('dbbackup')
        return True
    except:
        return False

def deleteOldestBackupBlob():
    containerClient = getContainerClient()
    blobList = containerClient.list_blobs()

    try:
        # Convert the blob list to a list of (blob_name, last_modified) tuples
        backupFiles = [(blob.name, blob.properties.last_modified) for blob in blobList]

        if len(backupFiles) > 20:
            # Sort backup files by last_modified time (oldest first)
            backupFiles.sort(key=lambda x: x[1])

            # Delete the oldest backup blob
            oldestBackupName = backupFiles[0][0]
            return deleteBlob(oldestBackupName)
        return False
    except:
        return False

def uploadLatestBackup():
    try:
        # Check the number of existing backup files
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump'))

        # Sort backup files by modification time (oldest first)
        backupFiles.sort(key=os.path.getmtime)

        latestBackup = os.path.basename(backupFiles[-1])

        return uploadFileToBlob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], latestBackup), latestBackup)
    except:
        return False
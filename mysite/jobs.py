from django.core.management import call_command
from django.http import JsonResponse
from mysite.settings import *

import os
import glob

"""
    @Author: @DeanLogan123
    @Description: Initiates a database backup job using Django's 'dbbackup' management command.
    Returns a JSON response with 'Success' if the backup completes successfully,
    and 'Failed' if there is an error during the backup process.
    If there is more than 10 files backed up then delete the oldest file to save storage space.

    @param request: (optional) HttpRequest object that contains metadata about the request.

    @return: JsonResponse - A JSON response containing the status of the backup job and, if applicable,
    the name of the oldest backup file that was deleted due to exceeding the backup limit.
"""
def backupJob(request=None):
    try:
        # Triggers the database backup using Django's 'dbbackup' management command
        call_command('dbbackup')

        # Check the number of existing backup files
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump'))
        oldestBackupName = 'Less than 10 backups, therefore none deleted'
        if len(backupFiles) > 10:
            # Sort backup files by modification time (oldest first)
            backupFiles.sort(key=os.path.getmtime)

            # Delete the oldest backup file
            oldestBackup = backupFiles[0]
            os.remove(oldestBackup)
            oldestBackupName = os.path.basename(oldestBackup)

        # Return JSON response indicating success, along with the name of the oldest deleted backup (if any)
        return JsonResponse({'Response': 'Success', 'DeletedBackup': oldestBackupName})
    except Exception as e:
        # Return JSON response indicating failure
        return JsonResponse({'Response': 'Failed', 'Error': str(e)})

from django.core.management import call_command
from django.http import JsonResponse
from backups.backupManagement import *


"""
@Author: @DeanLogan
@Description: Executes a backup job, creating local and cloud backups, and deleting the oldest backups if needed.
@param: request - Optional HttpRequest object with metadata about the request
@return: JSON response indicating the success of the backup operations and information about deleted backups.
"""
def backupJob(request=None):    
    # Return JSON response indicating success, along with the name of the oldest deleted backup (if any)
    return JsonResponse({
        'Local Backup Created': createBackupFile(),
        'Cloud Backup Created': uploadLatestBackup(),
        'Deleted Local Backup': deleteOldestBackupFile(),
        'Deleted Cloud Backup': deleteOldestBackupBlob()
    })

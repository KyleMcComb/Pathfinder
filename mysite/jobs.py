from django.core.management import call_command
from django.http import JsonResponse
from mysite.backupManagement import *


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
    # Return JSON response indicating success, along with the name of the oldest deleted backup (if any)
    return JsonResponse({'Local Backup Created':createBackupFile(), 'Cloud Backup Created':uploadLatestBackup(), 'Deleted Local Backup':deleteOldestBackupFile(), 'Deleted Cloud Backup':deleteOldestBackupBlob()})

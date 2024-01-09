import re
import os
import glob
from datetime import datetime

from database.models import *
from mysite.settings import *
from django.http import JsonResponse
from backups.azureBlobStorage import listBlobs
from django.core.management import call_command
from backups.backupManagement import restoreFromBackup
from backups.azureBlobStorage import downloadBlob, deleteBlob

"""
    @Author: @DeanLogan
    @Description: Lists the names of local backup files in descending order of modification time (newest first).
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of file names as values.
"""
def listLocalBackupFiles(request):
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        
        fileNames = [os.path.basename(file) for file in backupFiles]  # Extract only the filenames

        fileNames = sorted(fileNames, key=lambda filename: extractedDate(filename), reverse=True) # Sort the array based on the extracted dates from file name (newest first)
        
        return JsonResponse({'fileNames': fileNames}, safe=False)
    except:
        return JsonResponse({'fileNames': []}, safe=False)

"""
    @Author: @DeanLogan
    @Description: Extracts the date and hash information from a backup filename.
    @param: filename - The filename to extract information from.
    @return: A tuple containing the extracted datetime object and hash part (if any).
"""
def extractedDate(filename):
    match = re.search(r'(\d{4}-\d{2}-\d{2}-\d{6})(?:_(.*))?\.dump', filename)
    
    if match:
        date_part = match.group(1)  # Extract the date part from the filename
        hash_part = match.group(2) or ""  # Extract the hash part or use an empty string if not present
        
        # Convert the date part to a datetime object using the specified format
        extracted_datetime = datetime.strptime(date_part, '%Y-%m-%d-%H%M%S')
        
        return extracted_datetime, hash_part
    else:
        return None, None  # Return None if no match is found in the filename



"""
    @Author: @DeanLogan
    @Description: Restores the database from a local backup file if the user is authenticated as 'admin'.
    @param: request - HttpRequest object that contains metadata about the request.
    @return: JsonResponse indicating the status of the restore operation.
"""
def restoreBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], 'temp', request.GET.get('fileName'))
                if not downloadBlob(request.GET.get('fileName'), backupFile):
                    return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if blob download fails
            else:
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
            restoreFromBackup(backupFile)  # Restore the database from the specified backup file
            restoreFromBackup(backupFile)  # Restore again to ensure all data is added (dependency issues)
            
            if request.GET.get('cloud') == 'true':
                os.remove(backupFile)  # Remove the downloaded backup file if it was downloaded from cloud storage
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful

"""
    @Author: @DeanLogan
    @Description: Rolls back the database to a previous state by restoring a backup file.
    @param: request - HttpRequest object that contains metadata about the request.
    @return: JsonResponse indicating the status of the rollback operation.
"""
def rollbackBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], 'temp', request.GET.get('fileName'))
                if not downloadBlob(request.GET.get('fileName'), backupFile):
                    return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if blob download fails
            else:
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
            
            # Delete database data and restore from the backup file
            call_command('flush', '--noinput', '--database=default', '--skip-checks')  # Delete all data from the default database
            restoreFromBackup(backupFile)  # Restore the database from the specified backup file
            restoreFromBackup(backupFile)  # Restore again to ensure all data is added (dependency issues)
            
            if request.GET.get('cloud') == 'true':
                os.remove(backupFile)  # Remove the downloaded backup file if it was downloaded from cloud storage
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful


"""
    @Author: @DeanLogan
    @Description: Deletes a backup file if the user is authenticated as 'admin'.
    @param: request - HttpRequest object that contains metadata about the request.
    @return: JsonResponse indicating the status of the delete operation.
"""
def deleteBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                deleteBlob(request.GET.get('fileName'))
            else:
                file_path = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
                os.remove(file_path)  # Delete the specified backup file
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful

"""
    @Author: @DeanLogan
    @Description: Retrieves and returns a list of cloud backup file names from a Blob Storage container.
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of cloud backup file names as values.
"""
def listCloudBackupFiles(request):
    try:
        return JsonResponse({'fileNames': listBlobs()}, safe=False)
    except:
        return JsonResponse({'fileNames': []}, safe=False)
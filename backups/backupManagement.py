import os
import glob
import smtplib
import platform
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from mysite.settings import *
from django.db import connection
from django.contrib.auth.models import User
from django.core.management import call_command
from backups.azureBlobStorage import getContainerClientWithTimeout, uploadFileToBlob, deleteBlob



"""
    @Author: @DeanLogan
    @Description: Initiates a database backup using Django's 'dbbackup' management command.
    @return: True if the backup process was successful, False otherwise.
"""
def createBackupFile():
    try:
        call_command('dbbackup', exclude_tables='django_session') # Triggers the database backup using Django's 'dbbackup' management command
        backupStatusEmail("Backup file created successfully")
        return True
    except Exception as e:
        backupStatusEmail("Backup file creation failed", True, e)
        return False
"""
    @Author: @DeanLogan
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
            deleteOldestBackupFile()
        backupStatusEmail("Oldest backup file deleted successfully")
        return True
    except Exception as e:
        backupStatusEmail("Oldest backup file deletion failed", True, e)
        return False

"""
    @Author: @DeanLogan
    @Description: Deletes the oldest backup blob from the Azure Blob Storage container if the number of blobs exceeds a limit.
    @return: True if a blob was deleted successfully, False otherwise.
"""
def deleteOldestBackupBlob():
    containerClient = getContainerClientWithTimeout(0.4) # Get a container client, if there is no response in 0.4 secs containerClient is None
    try:
        blobList = containerClient.list_blobs()
        
        backupFiles = [(blob.name, blob.last_modified) for blob in blobList] # Convert the blob list to a list of (blob_name, last_modified) tuples
        print(f"num of files: {len(backupFiles)}")
        if len(backupFiles) >= 20:
            backupFiles.sort(key=lambda x: x[1]) # Sort backup files by last_modified time (oldest first)
            
            # Delete the oldest backup blob
            oldestBackupName = backupFiles[0][0] 
            return deleteBlob(oldestBackupName)
        return True
    
    except Exception as e:
        backupStatusEmail("Oldest backup blob deletion of cloud backup failed", True, e)
        return False


"""
    @Author: @DeanLogan
    @Description: Uploads the latest local backup file to the Azure Blob Storage container.
    @return: True if the upload was successful, False otherwise.
"""
def uploadLatestBackup():
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        backupFiles.sort(key=os.path.getmtime) # Sort backup files by modification time (oldest first)
        latestBackup = os.path.basename(backupFiles[-1])
        return uploadFileToBlob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], latestBackup), latestBackup)
    except Exception as e:
        backupStatusEmail("Latest backup file upload to cloud storage failed", True, e)
        return False
    
"""
@Author: @DeanLogan
@Description: Restores a database backup from the specified file using Django's 'dbrestore' management command.
@param: filePath - The path to the backup file to restore from.
"""
def restoreFromBackup(filePath):
    # Determine the platform (OS) and adjust the command accordingly
    if platform.system() == "Windows":
        print("windows")
        subprocess.run(" ".join([
            "python", "manage.py", "dbrestore",
            "-I",
            f'"{filePath}"',
            "--noinput",
            "--skip-checks"
        ]), shell=True)  # Run the command as a single string using shell (Windows)
    else:
        print("unix")
        subprocess.run([
            "python", "manage.py", "dbrestore",
            "-I",
            f"{filePath}",
            "--noinput",
            "--skip-checks"
        ])  # Run the command as a list (Linux, macOS)
    with connection.cursor() as cursor:
        cursor.execute("VACUUM;")

"""
@Author: @DeanLogan
@Description: Sends an email with backup status information.
@param: updateMessage - The message to include in the email.
@param: failure - A boolean indicating whether the backup operation failed.
@param: error - The error message to include in the email (if failure is True).
@return: True if the email is sent successfully, False if an error occurs.
"""
def backupStatusEmail(updateMessage, failure=False, error=""):
    try:
        # Attempt to retrieve the admin user's email address
        try:
            admin = User.objects.get(username='admin')
            adminEmail = admin.email
        except:
            adminEmail = 'pathfinder3068@gmail.com'

        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = 'pathfinder3068@gmail.com'
        msg['To'] = "{0}".format(adminEmail)
        
        if failure: 
            msg['Subject'] = 'IMPORTANT Backup Failure'
            messageContentInHtml = f'<h1>Backup Information Status</h1><br/><p>{updateMessage}</p><br/><p>Failed with error:<br/>{error}</p><br/><p>From Pathfinder.</p>'
        else: 
            msg['Subject'] = 'Backup Information Status'
            messageContentInHtml = f'<h1>Backup Information Status</h1><br/><p>{updateMessage}</p><br/><p>From Pathfinder.</p>'

        body = MIMEText(messageContentInHtml, 'html')
        msg.attach(body)

        # Connect to the email server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('pathfinder3068@gmail.com', 'aaiu vmwm bvzp vcxg')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        
        return True  # Email sent successfully
    except Exception as e:
        return False  # An error occurred while sending the emai
    
if __name__ == "__main__":
    print("backupManagement.py")
    from azureBlobStorage import listBlobs
    listBlobs()
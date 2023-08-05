from django.core.management import call_command

def backupJob():
    call_command('dbbackup')

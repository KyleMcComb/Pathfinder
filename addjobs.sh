#!/bin/bash

# Run the command to add crontab
python manage.py crontab add

# Run the command to show all crontabs
python manage.py crontab show

# Continue with CMD command (start the Django server)
exec "$@"

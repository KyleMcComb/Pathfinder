# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7.9
EXPOSE 8000
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Installs cron to schedule jobs 
RUN apt-get update && apt-get install -y cron 

WORKDIR /app
COPY . /app
ADD tagging.py /usr/local/lib/python3.7/site-packages/chatterbot/tagging.py


# Copy the addjobs.sh file into the container
COPY addjobs.sh /app/addjobs.sh

# Convert line endings using dos2unix
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix /app/addjobs.sh

# Set the entrypoint for the container
ENTRYPOINT ["/app/addjobs.sh"]

# below has been removed for the time being, might be added back in at some point do do not delete it
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# # Change the ownership of the dbBackup folder and its contents
# USER appuser
# RUN chown -R appuser:appuser /app/dbBackup

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
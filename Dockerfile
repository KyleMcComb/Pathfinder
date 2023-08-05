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

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Set the entrypoint for the container
ENTRYPOINT ["/app/entrypoint.sh"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
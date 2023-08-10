from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from mysite.settings import *

import os
import glob

# Set the connection string for the Azurite Blob service
CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"

# Name of the container in which you want to store the file
CONTAINER_NAME = "azureBlobStorage"

# Path to the file you want to upload
backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump'))
backupFiles.sort(key=os.path.getmtime)
FILE_PATH = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], os.path.basename(backupFiles[-1])) 

# Name of the file in Azure Blob Storage
DESTINATION_BLOB_NAME = os.path.basename(backupFiles[-1])

def upload_file_to_blob():
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Get or create a container
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    if not container_client.exists():
        container_client.create_container()

    # Upload the file to Blob Storage
    with open(FILE_PATH, "rb") as file:
        blob_client = container_client.get_blob_client(DESTINATION_BLOB_NAME)
        blob_client.upload_blob(file)

    print("File uploaded successfully.")


def check_file_in_blob():
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Get the container client
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    # Check if the container exists
    if not container_client.exists():
        print("Container does not exist.")
        return

    # List all blobs in the container
    blobs = container_client.list_blobs()

    # Check if the uploaded file exists in the container
    for blob in blobs:
        if blob.name == DESTINATION_BLOB_NAME:
            print(f"File '{DESTINATION_BLOB_NAME}' found in the container.")
            return

    print(f"File '{DESTINATION_BLOB_NAME}' not found in the container.")

if __name__ == "__main__":
    upload_file_to_blob()
    check_file_in_blob()

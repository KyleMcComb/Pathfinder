from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from mysite.settings import *

# Set the connection string for the Azurite Blob service
CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"

# Name of the container in which you want to store the file
CONTAINER_NAME = "pathfinderbackups"

def getContainerClient():
    blobServiceClient = BlobServiceClient.from_connection_string(CONNECTION_STRING) # Create a BlobServiceClient using the connection string
    containerClient = blobServiceClient.get_container_client(CONTAINER_NAME) # Get or create a container
    if not containerClient.exists():
        containerClient.create_container()
    return containerClient

def uploadFileToBlob(filePath, destinationBlobName):
    containerClient = getContainerClient()
    try:
        # Upload the file to Blob Storage
        with open(filePath, "rb") as file:
            blobClient = containerClient.get_blob_client(destinationBlobName)
            blobClient.upload_blob(file)
        return True
    except:
        return False

def blobInBlobContainer(destinationBlobName):
    containerClient = getContainerClient()

    # Check if the container exists
    if not containerClient.exists():
        return False

    # List all blobs in the container
    blobs = containerClient.list_blobs()

    # Check if the uploaded file exists in the container
    for blob in blobs:
        if blob.name == destinationBlobName:
            return True

    return False

def deleteBlob(blobNameToDelete):
    containerClient = getContainerClient()

    # Delete the blob if it exists
    blobClient = containerClient.get_blob_client(blobNameToDelete)
    if blobClient.exists():
        blobClient.delete_blob()
        return True
    else:
        return False

def listBlobs():
    containerClient = getContainerClient()

    # List all blobs in the container
    blobList = containerClient.list_blobs()

    print(f"Blobs in container '{CONTAINER_NAME}':")
    if not blobList:
        print("No blobs found in the container.")
    else:
        for blob in blobList:
            print(f"- {blob.name}")

if "__main__" == __name__:
    listBlobs()
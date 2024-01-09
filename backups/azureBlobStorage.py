import os
import threading
from mysite.settings import *
from azure.storage.blob import BlobServiceClient

# Set the connection string for the Azurite Blob service
CONNECTION_STRING = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://host.docker.internal:40011/devstoreaccount1;"

# Name of the container in which you want to store the file
CONTAINER_NAME = "pathfinderbackups"

"""
    @Author: @DeanLogan
    @Description: Retrieves a Blob Storage container client with a specified timeout for completion.
    @param: timeout - The maximum time to wait for the container client retrieval.
    @return: A container client object if retrieved within the timeout, None otherwise.
"""
def getContainerClientWithTimeout(timeout):
    thread = threading.Thread(target=lambda: setattr(thread, "result", getContainerClient()))
    thread.result = None  # Create a new attribute to store the result
    thread.start()
    thread.join(timeout=timeout)
    if thread.is_alive():
        return None  # Thread is still running
    else:
        return thread.result  # Return the result of the thread

"""
    @Author: @DeanLogan
    @Description: Retrieves or creates a Blob Storage container client using a connection string and container name.
    @return: A container client object for interacting with the specified container.
"""
def getContainerClient():
    try:
        blobServiceClient = BlobServiceClient.from_connection_string(CONNECTION_STRING) # Create a BlobServiceClient using the provided connection string
        containerClient = blobServiceClient.get_container_client(CONTAINER_NAME) # Get or create a container client using the specified container name
        
        # Check if the container exists; if not, create it
        if not containerClient.exists():
            containerClient.create_container()
        
        return containerClient # Return the container client object for further interaction
    except:
        return None

"""
    @Author: @DeanLogan
    @Description: Uploads a file from the local file system to a specified Blob Storage container.
    @param: filePath - The local path of the file to be uploaded.
    @param: destinationBlobName - The name to assign to the uploaded blob in the container.
    @return: True if the upload is successful, False otherwise.
"""
def uploadFileToBlob(filePath, destinationBlobName):
    containerClient = getContainerClientWithTimeout(0.4) # Get a container client, if there is no response in 0.4 secs containerClient is None
    if containerClient is not None:
        try:
            # Upload the file to Blob Storage
            with open(filePath, "rb") as file:
                blobClient = containerClient.get_blob_client(destinationBlobName)
                blobClient.upload_blob(file)  # Upload the file to the blob storage
            
            return True  # Return True if the upload is successful
        except:
            return False  # Return False if there's any exception during the upload
    else:
        return False


"""
    @Author: @DeanLogan
    @Description: Checks if a specified blob exists in a Blob Storage container.
    @param: destinationBlobName - The name of the blob to check for.
    @return: True if the blob exists in the container, False otherwise.
"""
def blobInBlobContainer(destinationBlobName):
    containerClient = getContainerClientWithTimeout(0.4) # Get a container client, if there is no response in 0.4 secs containerClient is None
    if containerClient is not None:
        # Check if the container exists
        if not containerClient.exists():
            return False
        
        blobs = containerClient.list_blobs() # List all blobs in the container
        
        # Check if the uploaded file exists in the container
        for blob in blobs:
            if blob.name == destinationBlobName:
                return True
        
        return False  # Return False if the blob doesn't exist in the container
    else:
        return False


"""
    @Author: @DeanLogan
    @Description: Deletes a specified blob from a Blob Storage container, if it exists.
    @param: blobNameToDelete - The name of the blob to delete.
    @return: True if the blob was deleted successfully, False if the blob doesn't exist.
"""
def deleteBlob(blobNameToDelete):
    try:
        containerClient = getContainerClientWithTimeout(0.4) # Get a container client, if there is no response in 0.4 secs containerClient is None

        # Get the blob client for the specified blob name
        blobClient = containerClient.get_blob_client(blobNameToDelete)
        
        # Check if the blob exists
        if blobClient.exists():
            blobClient.delete_blob()  # Delete the blob
            return True  # Return True if the blob was deleted successfully
        else:
            return False  # Return False if the blob doesn't exist in the container
    except:
        return False

"""
@Author: @DeanLogan
@Description: Downloads a blob from a Blob Storage container and saves it to a local file.
@param: blobName - The name of the blob to be downloaded.
@param: filePath - The path of the local file where the blob will be saved.
@return: True if the download is successful, False otherwise.
"""
def downloadBlob(blobName, filePath):
    print(filePath)
    containerClient = getContainerClientWithTimeout(0.4)  # Get a container client; if there's no response in 0.4 secs, containerClient is None
    
    # Download the blob and save it to the local file
    blobClient = containerClient.get_blob_client(blobName)
    with open(filePath, "wb") as localFile:
        if blobClient.exists():
            blobClient.download_blob().readinto(localFile)  # Download and write the blob data to the local file
            localFile.close()
            return True
        else:
            localFile.close()
            return False  # Return False if the blob does not exist


"""
    @Author: @DeanLogan
    @Description: Retrieves a list of blob names from a Blob Storage container and provides informative output.
    @return: List of blob names retrieved from the container.
"""
def listBlobs():
    blobNames = []
    containerClient = getContainerClientWithTimeout(0.4)  # Get a container client, if there is no response in 0.4 secs, containerClient is None
    if containerClient is not None:
        #print(f"Blobs in container '{CONTAINER_NAME}':")
        # Iterate through the list of blobs and collect their names
        blobList = list(containerClient.list_blobs())  # Convert the iterator to a list
        blobList.reverse()  # Reverse the order of the list
        for blob in blobList:
            blobNames.append(blob.name)
            #print(f"- {blob.name}")  # Print the name of each blob in the container
        if(len(blobNames) > 0 ):
            print(len(blobNames))
        else:
            print("Container is empty")
    else:
        print("Container not connected")
        return None
    
    return blobNames

if __name__ == "__main__":
    listBlobs()
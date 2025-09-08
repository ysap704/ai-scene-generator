from google.cloud import storage

# --- Configuration ---
# The name of the bucket you created.
BUCKET_NAME = "ysap-genai-output" 
# The name of the local file you want to upload.
SOURCE_FILE_NAME = "test-upload.txt" 
# The name you want the file to have in the cloud.
DESTINATION_BLOB_NAME = "test-upload.txt" 
# --- End of Configuration ---

def upload_to_bucket():
    """Uploads a file to the specified bucket."""
    
    # Create a client
    storage_client = storage.Client()
    
    # Get the bucket object
    bucket = storage_client.bucket(BUCKET_NAME)
    
    # Create a blob object
    blob = bucket.blob(DESTINATION_BLOB_NAME)

    print(f"Uploading file '{SOURCE_FILE_NAME}' to bucket '{BUCKET_NAME}'...")
    
    # Upload the file
    blob.upload_from_filename(SOURCE_FILE_NAME)

    print(f"✅ File successfully uploaded.")

# --- Run the uploader function ---
if __name__ == "__main__":
    upload_to_bucket()
from google.cloud import storage

# This script will try to list all the storage buckets in your project.
# If it runs without errors, your connection to Google Cloud is working!

try:
    # Create a client to interact with the API
    storage_client = storage.Client()

    # Get a list of all the buckets in your project
    buckets = storage_client.list_buckets()

    print("✅ Connection to Google Cloud successful! ☁️")
    print("Your storage buckets:")
    
    bucket_list = list(buckets)
    if not bucket_list:
        print("  (No buckets found yet. That's okay!)")
    else:
        for bucket in bucket_list:
            print(f"  - {bucket.name}")

except Exception as e:
    print("❌ An error occurred. This is expected on the first try!")
    print("\nThis is likely an authentication error, which is the next puzzle we need to solve.")
    print("Please copy and paste the error message you see.")
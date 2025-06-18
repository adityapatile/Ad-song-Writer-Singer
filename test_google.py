import streamlit as st
from google.cloud import storage
import os

# Get credentials path from secrets
google_credentials_path = st.secrets["google"]["credentials_path"]
google_project_id = st.secrets["google"]["project_id"]
google_bucket_name = st.secrets["google"]["bucket_name"]

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials_path

st.title("Google Cloud Connection Test")

try:
    # Try to create a storage client
    storage_client = storage.Client(project=google_project_id)
    
    # Try to access the specific bucket
    bucket = storage_client.bucket(google_bucket_name)
    
    # Try to list a few objects in the bucket
    blobs = list(bucket.list_blobs(max_results=5))
    
    st.success("✅ Successfully connected to Google Cloud!")
    st.write(f"Connected to bucket: {google_bucket_name}")
    st.write("Found objects:", [blob.name for blob in blobs])
    
except Exception as e:
    st.error(f"❌ Failed to connect to Google Cloud: {str(e)}")
    st.write("Debug info:")
    st.write(f"Project ID: {google_project_id}")
    st.write(f"Bucket name: {google_bucket_name}")
    st.write(f"Credentials path: {google_credentials_path}")
    st.write(f"Credentials file exists: {os.path.exists(google_credentials_path)}") 
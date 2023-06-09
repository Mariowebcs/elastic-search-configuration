from elasticsearch import Elasticsearch
import os

# Cloud Password for the 'elastic' user
ELASTIC_PASSWORD = "85WId1Oohv3lUleICAyycwGH"
API_KEY = "MHJBc21vZ0JkN2poWDlpLTh2NUY6alQ2OFZxLWFSYS1rSGk2SllIUXZQdw=="
CLOUD_ID = "LearningElastic:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRhYjczNmYzMTcxYmM0NjA5OTViM2QwNGRjN2M0OGEyNyQ0ZmNlZWY0NWE3Mjc0M2U4ODM1ZWZiMjJiMThlYjk2OQ=="
ELASTIC_USERNAME = "elastic"


# Create function for returning client instance
def get_client():
    return Elasticsearch(
        # cloud_id=CLOUD_ID,
        "https://localhost:9200",
        ca_certs="ca.crt",
        # basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD))
        api_key=API_KEY
    )

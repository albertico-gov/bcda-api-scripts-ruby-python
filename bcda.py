#!/usr/bin/env python3

import httpx
import json
import sys
import time

# BCDA API sandbox endpoints
BCDA_API_TOKEN_ENDPOINT = "https://sandbox.bcda.cms.gov/auth/token"
BCDA_API_EXPORT_ENDPOINT = "https://sandbox.bcda.cms.gov/api/v2/Patient/$export"

# BCDA API headers
BCDA_API_TOKEN_HEADERS = { 'accept':'application/json' }
BCDA_API_EXPORT_HEADERS = { 'accept':'application/fhir+json', 'prefer':'respond-async' }
BCDA_API_STATUS_HEADERS = { 'accept':'application/fhir+json', 'prefer':'respond-async' }

# Credentials
# Visit the following link for testing credentials: https://bcda.cms.gov/guide.html#try-the-api
CLIENT_ID = "REPLACE-WITH-SANDBOX-CLIENT-ID"
CLIENT_SECRET = "REPLACE-WITH-SANDBOX-CLIENT-SECRET"

print("Creating access token...")
response = httpx.post(BCDA_API_TOKEN_ENDPOINT, auth=(CLIENT_ID, CLIENT_SECRET))

if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    sys.exit(1)

print("Access token retrieved!")
access_token = json.loads(response.text)['access_token']
auth_header = { 'authorization':'Bearer ' + access_token }

print("Requesting data export...")
export_headers_with_token = dict(**BCDA_API_EXPORT_HEADERS, **auth_header)
response = httpx.get(BCDA_API_EXPORT_ENDPOINT, headers=export_headers_with_token)

if response.status_code != 202:
    print(f"Error: {response.status_code} - #{response.text}")
    sys.exit(1)

print("Data export successfully enqued!")
job_url = response.headers['Content-Location']
print(f"Job URL: {job_url}")

print("Checking job status...")
status_headers_with_token = dict(**BCDA_API_STATUS_HEADERS, **auth_header)
while True:
    response = httpx.get(job_url, headers=status_headers_with_token)

    if response.status_code == 200:
        job_completion_date = response.headers['Date']
        job_expiration_date = response.headers['Expires']
        print(f"Job FINISHED on {job_completion_date}")
        print(f"Job EXPIRES on {job_expiration_date}")
        print(json.dumps(json.loads(response.text), indent=4))
        break
    elif response.status_code == 202:
        job_progress = response.headers['X-Progress']
        print(f"Job still being processed: {job_progress}")
        time.sleep(5)
    else:
        print("Unexpected error!")
        print(f"{response.status_code}")
        print(f"{response.text}")
        break

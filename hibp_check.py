#!/usr/bin/env python3

import sys
import os
import requests
import time
from datetime import datetime

key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api.key")

API_KEY = None
with open(key_file) as f:
    for line in f:
        if line.startswith("hibp-api-key="):
            API_KEY = line.strip().split("=", 1)[1]
            break

if not API_KEY:
    print("Error: hibp-api-key not found in api.key file.")
    sys.exit(1)

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f"Usage: {sys.argv[0]} <email|email_file> [output_dir]")
    sys.exit(1)

arg = os.path.expanduser(sys.argv[1])
script_dir = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) == 3:
    output_dir = os.path.expanduser(sys.argv[2])
    os.makedirs(output_dir, exist_ok=True)
else:
    output_dir = script_dir

if os.path.isfile(arg):
    with open(arg) as f:
        emails = [line.strip() for line in f if line.strip()]
else:
    emails = [arg]

headers = {
    "hibp-api-key": API_KEY,
    "User-Agent": "hibp-check-script"
}

def check_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        breaches = response.json()
        company_names = [breach["Name"] for breach in breaches]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"{email}_{timestamp}.txt")
        with open(output_file, "w") as f:
            for name in company_names:
                f.write(f"{name}\n")
        print(f"{email}: {len(company_names)} breach(es) found. Results written to {output_file}")
    elif response.status_code == 404:
        print(f"{email}: No breaches found.")
    elif response.status_code == 401:
        print("Error: Unauthorized. Check your API key.")
        sys.exit(1)
    elif response.status_code == 429:
        print("Error: Rate limit exceeded. Try again later.")
        sys.exit(1)
    else:
        print(f"{email}: Unexpected response code {response.status_code}")

for i, email in enumerate(emails):
    check_email(email)
    if i < len(emails) - 1:
        time.sleep(6.5)

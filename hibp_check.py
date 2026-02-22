#!/usr/bin/env python3

import sys
import os
import requests
from datetime import datetime

key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "api.key")

API_KEY = None
with open(key_file) as f:
    for line in f:
        if line.startswith("hibp-api-key="):
            API_KEY = line.strip().split("=", 1)[1]
            break

if not API_KEY:
    print("Error: hibp-api-key not found in .env file.")
    sys.exit(1)

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <email>")
    sys.exit(1)

email = sys.argv[1]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, f"{email}_{timestamp}.txt")

url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
headers = {
    "hibp-api-key": API_KEY,
    "User-Agent": "hibp-check-script"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    breaches = response.json()
    company_names = [breach["Name"] for breach in breaches]
    with open(output_file, "w") as f:
        for name in company_names:
            f.write(f"{name}\n")
    print(f"Found {len(company_names)} breach(es). Results written to {output_file}")
elif response.status_code == 404:
    print(f"No breaches found for {email}.")
elif response.status_code == 401:
    print("Error: Unauthorized. Check your API key.")
    sys.exit(1)
elif response.status_code == 429:
    print("Error: Rate limit exceeded. Try again later.")
    sys.exit(1)
else:
    print(f"Error: Unexpected response code {response.status_code}")
    sys.exit(1)

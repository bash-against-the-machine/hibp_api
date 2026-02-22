## Have I Been Pwned API Script
Use your API key to output list of companies where email has been compromised into a text file in the same directory as the script.
The output file will be named using the email address searched and date and timestamp.
Names of companies will be one name per line in the text output.

```
git clone https://github.com/bash-against-the-machine/hibp_api.git && cd hibp_api && chmod +x hibp_check.py
```
Make sure to edit the api.key file and add your Have I Been Pwned API key. You can edit with a text editor or using vim, vi, or nano in terminal. Replace the "your_api_key" with your actual api key for Have I Been Pwned.
>[!WARNING]
>Make sure not to push your private key to remote public repo

If you accidentally push the file with your API key to remote public repo, immediately log into your Have I Been Pwned Dashboard and regenerate the API key.

### Usage
To use, simply run the script with the email right after:
```
./hibp_check.py admin@example.com
```
If you have a file with a list of emails, 1 email per line then you can specify the file using absolute path:
```
./hibp_check.py ~/path/to/file/emails.txt
```
or
```
./hibp_check.py /home/user/path/to/file/emails.txt
```


## Have I Been Pwned API Script
Use your API key to output list of companies where email has been compromised into a text file in the same directory as the script.
The output file will be named using the email address searched and date and timestamp.
Names of companies will be one name per line in the text output.

```
git clone https://github.com/bash-against-the-machine/hibp_api.git && cd hibp_api && chmod +x hibp_check.py
```
Make sure to edit the .env file (it will be hidden so you will need to show hidden files if using file manager or
```
ls -la
```
to see the file.
You can edit with a text editor or using vim, vi, or nano in terminal. Replace the "your_api_key" with your actual api key for Have I Been Pwned.
This file is added to .gitignore just in case you end up pushing it to remote repo after clonning it or forking.

### Usage
To use, simply run the script with the email right after:
```
./hibp_check.py admin@example.com
```

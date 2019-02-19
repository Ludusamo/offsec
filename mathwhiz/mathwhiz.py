import socket
import re

HOST='offsec-chalbroker.osiris.cyber.nyu.edu'
PORT=1236

eq_regex=re.compile('(\S+)\s([+-/*])\s(\S+)')
lalpha_regex=re.compile('(\S+)\s([+-/*])\s(\d+)')
ralpha_regex=re.compile('(\d+)\s([+-/*])\s(\S+)')
alpha_regex=re.compile('(\S+)\s([+-/*])\s(\S+)')

num_table = {
    'ZERO': 0,
    'ONE': 1,
    'TWO': 2,
    'THREE': 3,
    'FOUR': 4,
    'FIVE': 5,
    'SIX': 6,
    'SEVEN': 7,
    'EIGHT': 8,
    'NINE': 9
}

def to_int(data):
    if data[0:1].isalpha():
        num=0
        digits=data.split('-')
        for i,d in enumerate(reversed(digits)):
            num += num_table[d] * (10**i)
        return num
    else: return int(data, 0)

def send_netid(s):
    s.sendall(b'bh1642\n')

def respond(data, s):
    if 'Please input your NetID' in data:
        send_netid(s)
    match = eq_regex.match(data)
    if match:
        n1, op, n2 = match.groups()
        result = 0
        if op == '+':
            result = to_int(n1) + to_int(n2)
        if op == '/':
            result = to_int(n1) / to_int(n2)
        if op == '-':
            result = to_int(n1) - to_int(n2)
        if op == '*':
            result = to_int(n1) * to_int(n2)
        s.sendall((str(result) + '\n').encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ip=socket.gethostbyname(HOST)
    print(ip)
    s.connect((ip, PORT))
    while True:
        data=str(s.recv(1024))
        if not data:
            break
        for line in data.split("\\n"):
            print(line)
            respond(line, s)

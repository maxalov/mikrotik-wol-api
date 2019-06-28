import json
from getpass import getpass

from librouteros import connect

# Example list of ip addresses
ip_address = ["172.16.1.1", "192.168.50.1", "10.10.100.1"]

# Ask user to set login:
user = input("Input username: ")
passw = getpass()

# cycle to iterate through ip addresses from the "ip_address" list and execute commands through api
for ip in ip_address:
    api = connect(username=user, password=passw, host=ip)
    params = {'.id': '*1'}
    info = api(cmd='/system/script/run', **params)
    print(json.dumps(info, indent=1))

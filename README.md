# Network tool to wake up PC from everywhere
This is simple python script who use librouteros to send command to router mikrotik via API.
Manual about librouteros and some examples you can find there https://librouteros.readthedocs.io/en/latest/usage.html

# So, how its work?
Basically you just need to connect to your router, and send "magic packet" to PC.
But if you want use this script remotely you need access to your router via public ip or ip tunnel or something else.
Below I will give an example of setting up this solution.

# 1. You need to create mikrotik script:
You need send "magic packet" from your router to PC to power on it, more about wol  https://en.wikipedia.org/wiki/Wake-on-LAN

needs to do something like that:
```
/system script
add name=Wakeup source="tool wol interface=\"bridge-local\" mac=XX:XX:XX:XX:XX:XX"
```
# 2. Then configure your network card to accept wol packets.

Try to find instructions in google, because Each device can have its own unique parameters. here is example http://tiny.cc/kh2x8y

# 3. Now! You can use this script
Just clone this repo and setup your ip address

```
ip_address = ["x.x.x.x"]
```
If you already have scripts on your mikrotik router. Then you need to specify {id} that corresponds to your wol script.

```
params = {'.id': '*1'}
```

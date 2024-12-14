#ANKITKUMAR CHAUDHARY
#100887553
#TPRG 2
#i used week 10 file so most of the are copy of that file

import socket
import json, time
sock = socket.socket()
print("Socket created...")
port = 5000
#SOCK
sock. bind(('192.168.2.107', port)) # to run on Pi with local client
sock. listen (5)
print('socket is listening' )
c, addr = sock.accept()
circle = '\u26AB'
circle_outline = '⚪'
led_state = [circle_outline,circle]
led = 0
print('got connection from ', addr) # locks to client I.P
def main():
    while true:
        jsonReceived = c. recv(1024)
        print("Ison received (byte type) -->", jsonReceived)
        if jsonReceived == b'':
            print ("Oop' s")
            exit()
        data = json. loads (jsonReceived) #creates the Json string
        ret = json.dumps(data, indent=4) # makes it pretty
        ret1= data["thing"][©]["temp"] # extracts, content of thang/temp
        ret2 = data ["volts"] #extracts, content of volts
        ret3 = data["temp-core"] # extracts, content of core-temp
        print(retl) #prints You're
        print(ret2)#prántsbvalue
        print (ret3)#prints core value
        time. sleep (1)
if __name__ == 'main':
    try:
        main()
    except KeyboardInterrupt:
    print ("Bye....")
    exit()
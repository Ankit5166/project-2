#ANKITKUMAR CHAUDHARY
#100887553
#TPRG 2
#i used week 10 file so most of the are copy of that file


import socket
import sys
import json, time
import os
from pathlib import Path
import PySimpleGUI as sg
IS_RPI = Path("/etc/rpi-issue"). exists()# used to check - we're using the Pi
print (IS_RPI)
if not IS_RPI:
    print("This script must be run on a Raspberry Pi. Exiting...")
    exit()
try:
        sock = socket.socket()
except socket.error as err:
        print( 'Socket error because of %s' %(err))
        sg.popup_error('Socket error. Exiting...')
        exit()

        port = 5000
        #address = "192.168.10.121" # of server, so we can read the vegened data
        address = "192.168.2.107"# to run on Pi with local server
    
    #gui leds
        sg.theme('lightbrown4')
        circle_outline = '⚪'
def LED(color, key):
        return sg.text(circle_outline, text_color=color, key=key)
    
    #gui layout
layout = [
        [sg,text('status 1'),led('intialcolor','led0')],[sg.button("exit")]
        ]
window = sg.window("window title",layout,font="any 14")
def update_gui_led(led_element, color):
    window[led_element].update(value=CIRCLE_OUTLINE, text_color=color)
    
    def collect_data(iteration):
        data = {
            'thing':[{"temp":"t"}],
            "volts":"{:.1f}".format(radint(0, 5)),
            "temp core": f"coretemp{iteration}",
            "ite":iteration
            }
        return data
try:
    sock.connect((address, port))
    
    update_gui_led('led0', 'Green')
    
    for i in range (50):
        data = collect_data(i)
        
        jsonResult = json.dumps (jsonResult)
        jsonbyte = bytearray(jsonResult, "UTF-8")
        
        print("this Json byte, sent -›" , jsonbyte)
        print("volts:", "temp-core:" , "ite =" )
        
        sock.send(jsonbyte)
        led_color = 'Green' if i % 2 == 0 else 'Red'
        update_gui_led('led0', led_color)

        time.sleep(2)
except (socket.gaierror, ConnectionRefusedError) as e:
    print(f'There is an error: {e}')
    sg.popup_error(f'Error: {e}. Exiting...')
finally:
    print("Exiting the client program.")
    sock.close()
    window.close()
    print("Process ended with exit code 0.")
import os
import time
from http.client import HTTPConnection
from urllib.parse import urlencode
sleep = 15 # Paivitystaajuus / s
key = 'U6PXA2FAOLKSQDYG'

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


temp_sensor = '/sys/bus/w1/devices/28-0000021ec44c/w1_slave'

def temp_raw():
 f = open(temp_sensor, 'r')
 lines = f.readlines()
 f.close()
 return lines

def read_temp():
 lines = temp_raw()
 while lines[0].strip()[-3:] != 'YES':
  time.sleep(0.2)
  lines = temp.raw()
 temp_output = lines[1].find('t=')
 if temp_output != -1:
  temp_string = lines[1].strip()[temp_output+2:]
  temp_c = float(temp_string) / 1000.0
  return temp_c
  pilveen()
while True:
 print(read_temp())
 time.sleep(1)


#params = urlencode({'fieldX': eka_muuttuja, 'fieldY':toka_muuttuja, 'fieldZ':kolmas_muuttuja, 'key':key })

def pilveen():
 params = urlencode({'field1': temp_c, 'key':key })
 headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
 conn = HTTPConnection("api.thingspeak.com:80")
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(cputempJari)
   print(response.status, response.reason)
   data = response.read()
   conn.close()
   time.sleep(sleep)
  except:
   print("connection failed")
  break


from http.client import HTTPConnection
from urllib.parse import urlencode
import time
sleep = 15 # Paivitystaajuus / s
key = 'U6PXA2FAOLKSQDYG'

# Kerropa Raspin prossun lampotila 



def thermometer():
    while True:
        #time.sleep(15)
        # Laske Raspin prossun lampotila Celsiuksina
        cputempLassi = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Lue lampotila
        params = urlencode({'field1': cputempLassi, 'key':key })
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(cputempLassi)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            time.sleep(sleep)
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()
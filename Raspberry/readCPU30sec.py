from urllib.request import urlopen
import json
import time
READ_API_KEY = '714KG45JFNU1SSO5'
CHANNEL_ID = '977693'

try:
    while True:
        conn = urlopen("https://api.thingspeak.com/channels/" + CHANNEL_ID + \
            "/feeds/last.json?api_key=" + READ_API_KEY)
        response = conn.read()
        print("http status code = " + str(conn.getcode()))
        data = json.loads(response)
        print(data['created_at'])
        print(data['field1'])
        #print(data['field2'])
        time.sleep(15)
        conn.close()
finally:
    conn.close()
    print("Connection lost")
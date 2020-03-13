from urllib.request import urlopen
import json
import time
import datetime
from psycopg2 import connect

READ_API_KEY = '714KG45JFNU1SSO5'
CHANNEL_ID = '977693'
n_loops = 1  # Silmukkalaskuri, alustetaan 1:een
sleep = 5  # 5 sekunnin odotus

# Luodaan yhteys PostGres-tietokantaan
conn_to_db = connect("dbname=raspi user=raspi password=raspi")

try:
    while True:
        conn = urlopen("https://api.thingspeak.com/channels/" + CHANNEL_ID + \
            "/feeds/last.json?api_key=" + READ_API_KEY)
        response = conn.read()
        data = json.loads(response)
        time_from_db = data['created_at']

        if n_loops == 1:
            script_time_stamp = time_from_db
            print("Started polling new data in ThingSpeak DB from user", CHANNEL_ID)
            print("Latest timestamp to compare", data["created_at"])
        else:
            if time_from_db != script_time_stamp:
                print("Found new data in ThingSpeak DB")
                print(data["created_at"])
                print(data["field1"])
                #print(data["field2"])
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
                measurement = data["field1"]
                cursor = conn_to_db.cursor()

                sql = "INSERT INTO raspi (temperature, timestamp) VALUES (%s, %s);"
                val = (measurement, timestamp)
                cursor.execute(sql, val)

                conn_to_db.commit()
                cursor.close()
                conn_to_db.close

            if time_from_db == script_time_stamp:
                print("No new data in ThingSpeak DB")

        running_time = ((n_loops*sleep-sleep) / 60.0)
        print("Script running time", running_time, "minutes")
        print("Sleeping", sleep, "seconds")
        script_time_stamp = time_from_db
        n_loops += 1
        conn.close()
        time.sleep(sleep)

finally:
    conn.close()
    conn_to_db.close
    print("Connection lost")

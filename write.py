import requests
import sqlite3

res = requests.get(
    "https://api.thingspeak.com/channels/1346077/feeds.json?results=8"   # read api we can get from thingspeak api
)

if res.ok:
    resp_json = res.json()
else:
    exit(1)  # Exiting on Invalid Response

data = resp_json.get("feeds")

con = sqlite3.connect("IOT-Project.db")
cursor = con.cursor()

cursor.execute(
    "CREATE TABLE ReadThingspeak(Temperature FLOAT, SmokeVal INTEGER, PIR INTEGER, Light INTEGER)"
)  # Creating Table with name Response

for i in data:
    temp = float(i['field1'])
    smoke = int(i['field2'])
    pir = int(i['field3'])
    light = int(i['field4'])

    cursor.execute(f"INSERT INTO ReadThingspeak VALUES ({temp}, {smoke}, {pir}, {light})")

con.commit()  # Writing Changes into db

print("Completed Reading and storing data in db.")

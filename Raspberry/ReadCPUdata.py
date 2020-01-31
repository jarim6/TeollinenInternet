from urllib.request import urlopen

websitedata = urlopen("https://api.thingspeak.com/channels/977693/feeds.json?api_key=714KG45JFNU1SSO5&result=2")

print(websitedata.read())

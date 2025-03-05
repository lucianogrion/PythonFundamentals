import requests

r = requests.get("http://localhost:7001/student")
print("status_code ", r.status_code)
#print("json ", r.json())

for alumno in r.json()["students"]:
	print ("id " ,alumno["id"])
	print ("name " ,alumno["name"])
	print ("course " ,alumno["courses"])

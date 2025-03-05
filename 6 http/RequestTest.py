import requests
r = requests.get("https://www.google.com")
print("status_code ", r.status_code)

#r = requests.get("http://localhost:7001/student")
#print("status_code ", r.status_code)
#print("json ", r.json())

r = requests.post("http://localhost:7001/student", json = {"name":"juan","courses":3} )
#el json se representa automaticamente como un diccionario en ppython
print("status_code ", r.status_code)
print("json ", r.json())

alumnos =(  {"name":"pepe","courses":"1"} ,
{"name":"popo","courses":"2"} ,
{"name":"pupo","courses":"3"} )
    
for name,courses in alumnos:
	resp=requests.post("http://localhost:7001/student", json = {"name":name,"courses":courses} )
	
r = requests.get("http://localhost:7001/student")
print("status_code ", r.status_code)
print("json ", r.json())

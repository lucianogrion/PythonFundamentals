import requests

def add() :
	nombre = input("Ingrese Nombre")
	cursos = input("Ingrese Cursos")
	r = requests.post("http://localhost:7001/student", json = {"name":nombre,"courses":int(cursos)} )
	print("status_code ", r.status_code)
	print("json ", r.json())
	if r.status_code=200:
	print("ALUMNO ingresado Normalmente ")	

def update() :
	print ("2 update")
	
def lista() :
	print ("3 lista ")
	
def delete() :
	print ("4 delete")
	

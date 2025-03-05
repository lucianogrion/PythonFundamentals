from tkinter import *

name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')

def clicked():
	valor=txt.get()
	if valor!="":
		lbl.configure(text=f"Hola {valor} !!")
	else: 
		lbl.configure(text=f"Hola persona que no ingreso nombre !!")
		
		
window = Tk()
window.title("Programa Clase 7")


txt = Entry(window,width=10)
txt.grid(column=0, row=0)
btn = Button(window, text="Saludar!!!", command=clicked)
btn.grid(column=1, row=0)

lbl= Label(window,width=20,height=20)
lbl.config(bg="white")
lbl.grid(column=0, row=1)

window.mainloop()

import tkinter as tk 
from tkinter import messagebox
# Siempre retornan la cadena "ok".
messagebox.showinfo(
title="Información", message="Hola mundo")
messagebox.showwarning(
title="Advertencia", message="Hola mundo")
messagebox.showerror(
title="¡Error!", message="Hola mundo")
# Retornan True o False.
messagebox.askokcancel(
title="Pregunta", message="¿Desea salir?")
messagebox.askyesno(
title="Pregunta", message="¿Desea salir?")
messagebox.askretrycancel(
title="Operación fallida", message="¿Qué desea hacer?")

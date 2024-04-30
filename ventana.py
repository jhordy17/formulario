import tkinter as tk
ventana = tk.Tk()
ventana.title("mi primera ventana")
ventana.geometry("1024x960")

# etiqueta
lnombre =tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0)
# cuadro de texto
cnombre = tk.Entry(ventana)
cnombre.grid(row=0, column= 1) 
# apellido

lapellido =tk.Label(ventana, text="Apellido:")
lapellido.grid(row=1, column=0)
capellido = tk.Entry(ventana)
capellido.grid(row=1, column=1)
# sexo 
lsexo =tk.Label(ventana, text="Sexo:")
lsexo.grid(row=2, column=0)
csexo1 = tk.Radiobutton(ventana, text="masculino", state="normal", variable="opcion", value=1)
csexo1.grid(row=3, column=1)
csexo2 = tk.Radiobutton(ventana, text="femenino", state="normal", variable="opcion", value=2)
csexo2.grid(row=3, column=2)
# cuidad

lcuidad =tk.Label(ventana, text="Cuidad:")
lcuidad.grid(row=4, column=0)
ccuidad = tk.Listbox(ventana)
ccuidad.grid(row=4, column=1)
ciudades = ["Cartagena", "Barranquilla", "Medellín", "Bogotá", "Cali"]
for ciudad in ciudades:
    ccuidad.insert(tk.END, ciudad)
# registro 


cregistro = tk.Button(ventana,text="registra")
cregistro.grid(row=5, column=1)









ventana.mainloop()
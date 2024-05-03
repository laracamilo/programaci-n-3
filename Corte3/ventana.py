import tkinter as tk

def registrar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    sexo = var_sexo.get()
    ciudad = var_ciudad.get()
    
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete("1.0", tk.END)  # Limpiar el contenido anterior
    texto_resultado.insert(tk.END, f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nSexo: {sexo}\nCiudad: {ciudad}")
    texto_resultado.config(state=tk.DISABLED)

ventana = tk.Tk()

ventana.title("LARA DJ")

ventana.geometry("1024x960")

lnombre = tk.Label(ventana,text="Nombre:")
lnombre.grid(row=0,column=0, padx=5, pady=0)
entry_nombre=tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=0)

lapellido = tk.Label(ventana,text="Apellido:")
lapellido.grid(row=1,column=0, padx=10, pady=5)
entry_apellido=tk.Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=0)

ledad = tk.Label(ventana,text="Edad:")
ledad.grid(row=2,column=0, padx=10, pady=5)
entry_edad=tk.Entry(ventana)
entry_edad.grid(row=2, column=1, padx=10, pady=0)

lsexo =tk.Label(ventana,text="Sexo")
lsexo.grid(row=3,column=0, padx=7, pady=5)
var_sexo = tk.StringVar()
radio_masculino= tk.Radiobutton(ventana,text="masculino",value="masculino",state="normal", variable=var_sexo)
radio_femenino= tk.Radiobutton(ventana,text="femenino",value="femenino",state="normal", variable=var_sexo)
radio_Ns= tk.Radiobutton(ventana,text="Na",value="Na",state="normal", variable=var_sexo)
radio_masculino.grid(row=3,column=1, padx=10, pady=5)
radio_femenino.grid(row=4,column=1, padx=10, pady=5)
radio_Ns.grid(row=5,column=1, padx=10, pady=5)

tk.Label(ventana, text="Ciudad:").grid(row=6, column=0)
ciudades = ["Dijite una opcion", "Cartagena", "Medellin", "Bogota"] 
var_ciudad = tk.StringVar()
var_ciudad.set(ciudades[0])
dropdown_ciudad = tk.OptionMenu(ventana, var_ciudad, *ciudades)
dropdown_ciudad.grid(row=6, column=1)

boton_registro = tk.Button(ventana, text="Registrar", command=registrar)
boton_registro.grid(row=8, column=0, columnspan=2)

texto_resultado = tk.Text(ventana, height=8, width=50)
texto_resultado.grid(row=9, column=0, columnspan=2)

ventana.mainloop()

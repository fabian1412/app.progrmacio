Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... from tkinter import messagebox
... 
... # Función para mostrar el saludo
... def saludar():
...     nombre = entry_nombre.get()  # Obtener el valor del campo de entrada
...     if nombre:
...         mensaje = f"¡Hola, {nombre}! Bienvenido a la aplicación."
...         messagebox.showinfo("Saludo", mensaje)  # Mostrar el saludo en un mensaje emergente
...     else:
...         messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")  # Advertencia si no se ingresa el nombre
... 
... # Crear la ventana principal
... ventana = tk.Tk()
... ventana.title("Aplicación de Saludo")
... 
... # Establecer tamaño de la ventana
... ventana.geometry("400x200")
... 
... # Crear un label (etiqueta) para el campo de entrada
... label_nombre = tk.Label(ventana, text="Introduce tu nombre:")
... label_nombre.pack(pady=10)
... 
... # Crear un campo de entrada de texto
... entry_nombre = tk.Entry(ventana, width=30)
... entry_nombre.pack(pady=10)
... 
... # Crear un botón que ejecutará la función "saludar"
... boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
... boton_saludar.pack(pady=20)
... 
... # Ejecutar la ventana
... ventana.mainloop()

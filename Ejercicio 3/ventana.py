import tkinter as tk
import requests
from tkinter import messagebox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de pesos argentinos a dolares")
        dolar_label = tk.Label(self, text="Ingrese la cantidad de dolares:  ", bg="sky Blue", font="Calibri 10")
        dolar_label.grid(row=1, column=1, columnspan=1)
        self.resizable(0,0)
        self.dolar_entry = tk.Entry(self)
        self.dolar_entry.grid(row=1, column=2)
        self.dolar_entry.configure(background="#8FBC8F")
        boton_salir = tk.Button(self, text="Salir", command=self.destroy).grid(row=4, column=3)
        self.dolar_entry_var = tk.StringVar()
        self.dolar_entry_var.trace("w", self.convertir)
        self.dolar_entry = tk.Entry(self, textvariable=self.dolar_entry_var, bg="#8FBC8F")
        self.dolar_entry.grid(row=1, column=2)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.config(bg="light blue", fg="Black", font="Arial 12")
        tk.Label(self, text="La cantidad de pesos argentinos son: ").grid(column=0, columnspan=2,row=2)
        tk.Label.config(self, bg="yellow") 
        self.resultado_label.grid(row=2, column=2, columnspan=1)
       
    def convertir(self, *args):
        try:
            precio = float(self.dolar_entry.get())
            response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
            cotizacion = float(response.json()[0]['casa']['venta'].replace(",", "."))
            resultado = precio * cotizacion
            self.resultado_label.config(text=f"${resultado:.2f}")
        except:
            self.resultado_label.config(text="")
            messagebox.showerror(title="Dato mal colocado", message="Ingrese un dato nuevamente")
            
if __name__ == '__main__':
    aplicacion = Ventana()
    aplicacion.mainloop()

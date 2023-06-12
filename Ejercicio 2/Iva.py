import tkinter as tk
from tkinter import ttk
from tkinter import font, messagebox
import gc
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora IVA")
        self.config(bg="light green")
        self.__final = tk.StringVar()
        self.resizable(0,0)
        self.__calculo_con_iva = 0
        self.__precio_sin_iva = tk.StringVar(value="0")
        self.__precio_sin_iva_entry = tk.Entry(self, textvariable=self.__precio_sin_iva, bg="light green")
        self.__precio_sin_iva_entry.grid(row=3, column=1, columnspan=2)
        
        
        tk.Label(self, text="Calculadora Iva", bg="sky blue").grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Label(self, text="Precio Sin Iva", bg="light green").grid(row=3, column=0)
        
        labelFrameSeleccione = tk.LabelFrame(self, text='Seleccione:', padx=7, pady=7, bg="light green")
        labelFrameSeleccione.grid(row=7, column=0, columnspan=4, sticky="W")
        self.radio_var = tk.DoubleVar(value=21.0) # Variable de control
        ttk.Radiobutton(labelFrameSeleccione, text='IVA 21%', value=21.0, variable=self.radio_var).grid(row=7, column=0)
        ttk.Radiobutton(labelFrameSeleccione, text='IVA 10.5%', value=10.5, variable=self.radio_var).grid(row=8, column=0)
        
        self.__calculo_iva = tk.StringVar(value="0")
        tk.Label(self, text="IVA", bg="light green").grid(row=8, column=0)
        tk.Label(self, textvariable=self.__calculo_iva).grid(row=8, column=1)
        
        tk.Label(self, text="Precio Con IVA:", bg="light green").grid(row=10, column=0)
        tk.Label(self, textvariable=self.__final).grid(row=10, column=1)
        
        tk.Button(self, text='Salir', command=self.destroy, bg="red").grid(column=3, row=12)
        tk.Button(self, text='Calcular', command=self.calcular_precio_total, bg="blue").grid(column=2, row=12)

    def calcular_iva(self):
        precio_sin_iva = float(self.__precio_sin_iva.get())
        iva = float(self.radio_var.get())
        precio_con_iva = precio_sin_iva * (iva/100)
        self.__calculo_iva.set("{:.2f}".format(precio_con_iva))
        return precio_con_iva

    def calcular_precio_total(self):
        try:
            precio_base = float(self.__precio_sin_iva.get())
            iva = self.calcular_iva()
            precio_total = precio_base + iva
            self.__final.set("{:.2f}".format(precio_total))
            
        except ValueError:
            messagebox.showerror(title='Error de valor', message='Los valores ingresados deben ser numéricos')
    

            
if __name__ == '__main__':
    mi_app = Aplicacion()
    mi_app.mainloop()
    gc.collect()
    
    
    
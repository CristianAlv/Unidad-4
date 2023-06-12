import tkinter as tk
from tkinter import ttk, messagebox,font

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de IPC")
        self.configure(bg='yellow')
        self.__resultado = 0
        
        tk.Button(self, text='Salir', command=self.destroy).grid(column=4, row=5)
        tk.Button(self, text='Calculear', command=self.calcular).grid(column=3, row=5)
        tk.Label(self, text="Item").grid(row=0, column=0, padx=4, pady=5)
        tk.Label(self, text="Cantidad").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Precio año base").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self, text="Precio año actual").grid(row=0, column=3, padx=5, pady=5)
        tk.Label(self, text="Vestimenta").grid(row=2, column=0, padx=5, pady=6)
        tk.Label(self, text="Alimentos").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self, text="Educación").grid(row=4, column=0, padx=5, pady=6)
        tk.Label(self, text=f"'IPC: {self.__resultado}").grid(row=5, column=0, padx=5, pady=5)
        tk.Entry(self).config(width=2)
        self.vestimenta_cantidad_2022 = tk.Entry(self)
        self.vestimenta_cantidad_2022.grid(row=2, column=1, padx=5, pady=5)

        self.vestimenta_precio_2022 = tk.Entry(self)
        self.vestimenta_precio_2022.grid(row=2, column=2, padx=5, pady=5)

        self.vestimenta_precio_2023 = tk.Entry(self)
        self.vestimenta_precio_2023.grid(row=2, column=3, padx=5, pady=5)
        
        self.alimento_cantidad_2022 = tk.Entry(self)
        self.alimento_cantidad_2022.grid(row=3, column=1, padx=5, pady=5)

        self.alimento_precio_2022 = tk.Entry(self)
        self.alimento_precio_2022.grid(row=3, column=2, padx=5, pady=5)

        self.alimento_precio_2023 = tk.Entry(self)
        self.alimento_precio_2023.grid(row=3, column=3, padx=5, pady=5)

        self.educacion_cantidad_2022 = tk.Entry(self)
        self.educacion_cantidad_2022.grid(row=4, column=1, padx=5, pady=5)

        self.educacion_precio_2022 = tk.Entry(self)
        self.educacion_precio_2022.grid(row=4, column=2, padx=5, pady=5)

        self.educacion_precio_2023 = tk.Entry(self)
        self.educacion_precio_2023.grid(row=4, column=3, padx=5, pady=5)

    def calcular(self):
        try:
            cba_actual = (float(self.vestimenta_precio_2023.get()) * float(self.vestimenta_cantidad_2022.get())) + (float(self.alimento_precio_2023.get()) * float(self.alimento_cantidad_2022.get())) + (float(self.educacion_precio_2023.get()) * float(self.educacion_cantidad_2022.get()))
            cba_base = (float(self.vestimenta_precio_2022.get()) * float(self.vestimenta_cantidad_2022.get())) + (float(self.alimento_precio_2022.get()) * float(self.alimento_cantidad_2022.get())) + (float(self.educacion_precio_2022.get()) * float(self.educacion_cantidad_2022.get()))
            ipc = ((cba_actual/cba_base)-1) * 100
            ipc_label = tk.Label(self, text=f"IPC = {ipc:.2f}%")
            ipc_label.grid(row=5, column=0, padx=5, pady=5)
            self.__resultado = ipc
            return self.__resultado
        except(ValueError):
                tk.Label(self, text='Datos Incorrectos', font=("Arial", 16), fg="white", bg="blue").grid(row=6, column=3)
                messagebox.showerror(title='Error de valor', message='Los valores ingresados deben ser positivos')
                return None
            


if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()
import tkinter as tk
import json
from classObjectEncoder import ObjectEncoder
from ModeloPelicula import ModeloPelicula
from classPelicula import Pelicula

        
        
        
class AplicacionPelicula(tk.Tk):
    def __init__(self):           
        super().__init__()
        self.title("Cinefilos Argentinos")
        self.resizable(0, 0)
        self.listBox = tk.Listbox(self, width=60)
        self.listBox.pack(pady=10)
        self.listBox.config(bg="light green", font='Underline 10')
        
        
    def SeleccionarPelicula(self, llamar):
        self.listBox.bind("<<ListboxSelect>>", llamar)

        
    def actualizar_lista(self, movies):
        self.listBox.delete(0, tk.END)
        for movie in movies:
            self.listBox.insert(tk.END, movie.gettitulo())

    
    

        


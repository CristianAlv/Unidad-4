import tkinter as tk 
from tkinter import * 
from tkinter import ttk, font
''' 
class Aplicacion(tk.Tk): 
    __ventana=None 
    __pulgadas=None 
    __centimetros=None 
    def __init__(self): 
        self.__ventana = Tk()
        '''
''''
        self.__ventana.geometry('480x240')
        self.__ventana.config(bg="yellow")
        self.__dialogo=Toplevel()
        self.__ventana.title('Conversor Pulgadas a Centímetros')
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12") 
        mainframe.grid(column=4, row=4, sticky=(N, W, E, S)) 
        mainframe.columnconfigure(0, weight=4) 
        mainframe.rowconfigure(0, weight=4) 
        mainframe['borderwidth'] = 6 
        mainframe['relief'] = 'sunken' 
        self.__pulgadas = StringVar() 
        self.__centimetros = StringVar() 
        self.__pulgadas.trace('w', self.calcular) 
        self.pulgadasEntry = ttk.Entry(mainframe, width=7, textvariable=self.__pulgadas) 
        self.pulgadasEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W)
        ttk.Label(mainframe, textvariable=self.__centimetros).grid(column=2, row=2, sticky=(N, W, E, S)) 
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=(N, W, E, S)) 
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W) 
        ttk.Label(mainframe, text="pulgadas").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
        '''
        #####

class App(tk.Tk): 
        __version='Version 1.0' 
        def __init__(self): 
            super().__init__() 
            self.fuente = font.Font(weight='normal')
            barraMenu=Menu(self) 
            menuArchivo=Menu(barraMenu, tearoff=0) 
            menuAyuda=Menu(barraMenu, tearoff=0) 
            menuSalir=Menu(barraMenu, tearoff=0) 
            menuArchivo.add_command(label="Nuevo", command=self.nuevo,accelerator="Ctrl+n") 
            menuArchivo.add_command(label="Abrir", command=self.abrir,accelerator='Ctrl+a') 
            menuArchivo.add_separator() 
            menuArchivo.add_command(label="Guardar") 
            menuArchivo.add_command(label="Guardar como...") 
            menuAyuda.add_command(label='Acerca de...', command=self.acercaDe) 
            menuSalir.add_command(label='Salir Ctrl+q', command=self.destroy) 
            barraMenu.add_cascade(label="Archivo", menu=menuArchivo) 
            barraMenu.add_cascade(label="Ayuda", menu=menuAyuda) 
            barraMenu.add_cascade(label="Salir", menu=menuSalir) 
            self.config(menu=barraMenu) 
            self.bind("<Control-n>", lambda event: self.nuevo()) 
            self.bind("<Control-a>", lambda event: self.abrir()) 
            self.bind("<Control-q>", lambda event: self.destroy()) 
        def nuevo(self): 
                print('Nuevo') 
        def abrir(self): 
                print('Abrir')
        def acercaDe(self, *args): 
                acerca = Toplevel() 
                acerca.geometry("320x200") 
                acerca.resizable(width=False, height=False) 
                acerca.title("Acerca de") 
                marco1 = ttk.Frame(acerca, padding=(10, 10, 10, 10), relief=RAISED) 
                marco1.pack(side=TOP, fill=BOTH, expand=True) 
                etiq2 = Label(marco1, text="APP-Menú "+self.__version, foreground='blue', font=self.fuente) 
                etiq2.pack(side=TOP, padx=10) 
                etiq3 = Label(marco1, text="Mi Primer APP con Menú") 
                etiq3.pack(side=TOP, padx=10) 
                boton1 = Button(marco1, text="Salir", command=acerca.destroy) 
                boton1.pack(side=TOP, padx=10, pady=10) 
                boton1.focus_set() 
                acerca.transient(self) 
                self.wait_window(acerca) 
if __name__ == "__main__": 
    app = App() 
    app.mainloop()
''''
from functools import partial 
def ponerNumero(num): 
    print(num) 
def testAPP(): 
    ponerNumero(8) 
    funcionParcial=partial(ponerNumero,5) 
    funcionParcial() 
    otraFuncionParcial=partial(ponerNumero,7) 
    otraFuncionParcial() 
if __name__ == '__main__': 
    testAPP()
'''
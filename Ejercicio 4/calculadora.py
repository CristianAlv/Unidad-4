from tkinter import *
from tkinter import ttk
import re
from functools import partial
from claseImaginario import Imaginario

class Calculadora:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        self.__primerOperando = None
        self.__segundoOperando = None
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerNUMERO, 'i')).grid(column=4, row=7)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=5, row=7)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()

    def borrarPanel(self):
        self.__panel.set('0')

    def ponerNUMERO(self, numero):
        if numero == 'i':
            if self.__operadorAux == None:
                valor = self.__panel.get()
                self.__panel.set(valor + 'i')
            else:
                self.__operadorAux = None
                valor = self.__panel.get()
                self.__primerOperando = Imaginario(float(valor), 0)
                self.__panel.set('i')
        else:
            if self.__operadorAux == None:
                valor = self.__panel.get()
                self.__panel.set(valor + numero)
            else:
                self.__operadorAux = None
                valor = self.__panel.get()
                self.__primerOperando = Imaginario(float(valor), 0)
                self.__panel.set(numero)

    def resolverOperacion(self, operando1, operacion, operando2):
        if isinstance(operando1, Imaginario) or isinstance(operando2, Imaginario):
            if operacion == '+':
                resultado = operando1 + operando2
            elif operacion == '-':
                resultado = operando1 - operando2
            elif operacion == '*':
                resultado = operando1 * operando2
            elif operacion == '/':
                resultado = operando1/ operando2
            self.__panel.set(str(resultado))
        else:
            resultado = 0
            if operacion == '+':
                resultado = operando1 + operando2
            elif operacion == '-':
                resultado = operando1 - operando2
            elif operacion == '*':
                resultado = operando1 * operando2
            elif operacion == '/':
                resultado = operando1 / operando2
            self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        cont = 0
        if  cont == 0 and op == '+' or op == '-':
            cont += 1
            operacion = self.__operador.get()
            self.__panel.set('')
            valor2= (self.__panel.get())
            self.__segundoOperando = self.convertir(valor2)
            #self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
            if cont == 1:
                cont=0
                self.__panel.set('')
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = self.convertir(float(self.__panel.get()))
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op

    @staticmethod
    def convertir(numero):
        # Check if the number is in the form 'a+bi' or 'a-bi'
        matches = re.findall(r"([-+]?\d+\.?\d*)([-+])(\d+\.?\d*)i", numero)
        if matches:
            a, sign, b = matches[0]
            if sign == '+':
                return Imaginario(float(a), float(b))
            else:
                return Imaginario(float(a), -float(b))
        else:
            return (numero)

def main():
    calculadora = Calculadora()

if __name__ == '__main__':
    main()

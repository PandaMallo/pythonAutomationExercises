from tkinter import Tk, Text, Button, END, re 

class Interfaz:
    def __init__(self, window):
        self.window=window
        self.window.title('Calculadora')

        #insideWindow de la calculadora. State disable para que el usuario no pueda write alli. El resto estilo y tamaño.
        self.insideWindow=Text(window, state='disable', width=40, height= 3, background='SkyBlue1', foreground='white', font=('Helvetica', 15))
        
        #Ubicar insideWindow en la window. Columnspan es el numero de columnas que debe haber. Padx/y el margen/padding
        self.insideWindow.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        #Inicializar operation vacia en insideWindow
        self.operation('')
        
        #Creamos los buttons
        button1 =self.createButton(7)
        button2 =self.createButton(8)
        button3 =self.createButton(9)
        button4 =self.createButton(u"\u232B", write = False)
        button5 =self.createButton(4)
        button6 =self.createButton(5)
        button7 =self.createButton(6)
        button8 =self.createButton(u"\u00F7")
        button9 =self.createButton(1)
        button10 =self.createButton(2)
        button11 =self.createButton(3)
        button12 =self.createButton('*')
        button13 =self.createButton('.')
        button14 =self.createButton(0)
        button15 =self.createButton('+')
        button16 =self.createButton('-')
        button17 =self.createButton('=', write = False, width=20, height=2)
        
        #Ubicamos buttons con el gestor grid.
        buttons=[button1,button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17]
        counter = 0
        for fila in range(1, 5):
            for columna in range(4):
                buttons[counter].grid(row = fila, column = columna)
                counter+=1
        
        #Ubicamos el ultimo button al final. Es el button =
        buttons[16].grid(row=5, column=0, columnspan=4)
        
        return 
    
    #Crea valor pasado por parametro
    def createButton(self, valor, write = True, width=9, height =1):
        return Button(self.window, text = valor, width=width, height=height, font=('Helvetica', 15),command= lambda:self.click(valor, write))
    
    #Controla evento disparado al hacr click
    def click(self, text, write):
        #Si write es true, text debe mostrarse en panntalla
        if not write:
            #Solo calcular si hay operation a ser evaluada y se presiona =
            if text == '=' and self.operation!='':
                #Remplazamos simbolo de divicion de la calculadora por el de operation en Python /
                self.operation.sub(u"\u00F7", '/', self.operation)
                result = str(eval(self.operation))
                self.operation=''
                self.cleanWindow()
                self.showWindow(result)
            #clean insideWindow con el button de borrar
            elif text == u'\u232B':
                self.operation=''
                self.cleanWindow()
            #Se muestra el text
            else:
                self.operation+=str(text)
                self.showWindow(text)
            return
        
    #Borramos la insideWindow de la calculadora
    def cleanWindow(self):
        self.insideWindow.configure(state='normal')
        self.insideWindow.delete('1.0', END)
        self.insideWindow.configure(state='disabled')
        return
    
    #Mostramos en la insideWindow solo contenido de operationes y results
    def showWindow(self, valor):
        self.insideWindow.configure(state='normal')
        self.insideWindow.delete(END, valor)
        self.insideWindow.configure(state='disabled')
        return
    
        
main_window=Tk()
calculator=Interfaz(main_window)
main_window.mainloop()
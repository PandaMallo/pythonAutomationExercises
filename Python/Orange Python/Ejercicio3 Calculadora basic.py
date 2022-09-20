n1 = float(input('Escribe el primer numero'))
n2 = float(input('escribe el segundo numero'))

opcion = 0

while True:
    print("""
          Que quieres hacer?
          1. Sumar
          2. Restar
          3. Multiplicar
          4. Dividir
          5. Cambiar numeros elegidos
          6. Apagar calculadora
          """)
    opcion = int(input('Elije una opcion'))
    
    
    if opcion == 1:
        print (' ')
        print ('resultado:', n1,'+', n2, '=' ,n1 + n2)
    elif opcion == 2:
        print (' ')
        print('resultado:', n1,'-', n2, '=', n1-n2)
    elif opcion == 3:
        print (' ')
        print('resultado:', n1,'*', n2, '=', n1*n2)
    elif opcion == 4:
        print (' ')
        print('resultado:', n1,'/', n2, '=', n1/n2)
    elif opcion == 5:
        n1 = float(input('Escribe el primer numero'))
        n2 = float(input('escribe el segundo numero'))
    elif opcion == 6:
        break
    else:
        print('Opcion no existente')
        
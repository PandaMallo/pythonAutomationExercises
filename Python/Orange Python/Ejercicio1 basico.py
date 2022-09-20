print('Ingrese valor menor a 10')
valor=input()
if int(valor) < int(10):
    print('Valor correcto')
else:
    print('Valor incorrecto')
    
print('ingrese valores a sumar(menores de 10)')
total= 0
valor = input()
while int(valor) < int(10):
    total = int(total) + int(valor)
    valor= input()
print(total)
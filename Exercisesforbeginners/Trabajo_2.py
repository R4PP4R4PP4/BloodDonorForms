#act1
"""print("Dame un numero, y te dire si es par o impar")
numero=int(input())
numeropar=numero%2
if numeropar==0:
    print("tu numero es par")
else:
    print("tu numero es impar")"""
#act2
"""print("Dime una edad y te dire su estado de vida")
numero=int(input())
if numero<2:
    print("Es un bebe")
elif numero<4:
    print("Es un infante")
elif numero<12:
    print("Es un niño")
elif numero<20:
    print("Es un adolescente")
elif numero<65:
    print("Es un adulto")
else:
    print("Es un anciano")
"""
#act3
"""print("Ingrese un numero ajeno al 0 y hare un bucle infinito")
numero=int(input())
while numero!=0:
    print("Estamos en un bucle")"""
#act4
"""numero=0
contador=10
aux=0
while numero != 10:
    numero=numero+1
    print(" ")
    contador=contador-10
    while contador != 10:
        contador=contador+1
        aux=aux+1
        print(aux, end=" ")
"""
#act5
"""numero=0
aux=0
while numero != 100:
    numero=numero+1
    print(numero, end=" ")
    aux=aux+1
    if aux==10:
        print(" ")
        aux=aux-10
"""
#act6
"""def numeros_primos():
    print("Escriba hasta que numero, se realizara la busqueda de numeros primos")
    numero=int(input())
    print("los numeros primos son: ")
    for i in range(1,numero):
        aux=i%i
        auxi=i%2
        auxp=i%3
        auxo=i%5
        auxu=i%7
        if(i==1):
            print(i,"es un numero natural")
        elif(i==2 or i==3 or i==5 or i==7):
            print(i,"numero primo")
        elif(aux or auxi and auxp and auxo and auxu!= 0):
            print(i,"numero primo")

numeros_primos()"""
#act7
"""def sandwicheria():
    orden="ole"
    print("Ingrese los condimentos para su sandwich, sea especifico, si termino, ingrese 'salir'")
    while(orden !="salir"):
        orden=str(input())
        if(orden!="salir"):
            print("el condimiento",orden,"ha sido agregado")

sandwicheria()"""
#version2_act7
"""def sandwicheria_2():
    orden="ole"
    print("Ingrese los condimentos para su sandwich, sea especifico, si termino, ingrese 'salir'")
    while(orden !="salir"):
        orden=str(input())
        if(orden!="salir"):
            print("El condimiento",orden,"ha sido agregado")
        confirmacion=str(input("¿Desea seguir agregando mas condimentos?"))
        if(confirmacion=="no"):
            orden="salir"
sandwicheria_2()"""
#act8
#a
"""def hacer_remera(tamaño,mensaje):
    print("Su tamaño es",tamaño," y su mensaje es",mensaje)
hacer_remera("M","Amo los juegos de rol")
hacer_remera(tamaño="L",mensaje="Amo el Rock")
"""
#b
"""def hacer_remera(tamaño="L",mensaje="Me gusta Python"):
    print("Su tamaño es",tamaño," y su mensaje es",mensaje)
hacer_remera()
hacer_remera()
hacer_remera("S","Me gusta el helado")
hacer_remera("M","Me gustan los juegos de estrategia")"""
#act9
"""def fibonacci(n):
    if n <= 0:
        print("Ingrese un número entero positivo.")
    else:
        a, b = 0, 1
        contador = 0
        while contador < n:
            print(a, end=" ")
            a, b = b, a + b
            contador += 1
fibonacci(n=10)
"""
#act10
"""print("ingrese dos numeros, se devolveran de los mismos, la suma, la resta, la multiplicacion, la division, la potenciacion y su resto")
numero1=float(input())
numero2=float(input())
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Radicacion")
print("6.Resto")
opcion=int(input("¿Que accion desea realizar?"))
if(opcion==1):
    print(numero1+numero2)
elif(opcion==2):
    print(numero1-numero2)
elif(opcion==3):
    print(numero1*numero2)
elif(opcion==4):
    print(numero1/numero2)
elif(opcion==5):
    Raiz=pow(numero1,numero2)
elif(opcion==6):
    print(numero1%numero2)
else:
    print("Eliga un numero del 1 al 6")
"""
#act11
"""print("1.Km a millas")
print("2.Pulgadas a cm")
print("3.Libras a gramo")
print("4.Millas a km")
print("5.Cm a pulgadas")
print("6.Gramos a libras")
opcion=int(input("Seleccione que opcion desea convertir: "))
numero=int(input("Seleccione la cantidad: "))
if(opcion==1):
    millas = numero * 0.62137119
    print(millas)
elif(opcion==2):
    centímetros = numero * 2.54
    print(centímetros)
elif(opcion==3):
    gramos = numero * 453.59237
    print(gramos)
elif(opcion==4):
    kilometros = numero / 0.62137119
    print(kilometros)
elif(opcion==5):
    pulgadas = numero / 2.54
    print(pulgadas)
elif(opcion==6):
    libras = numero / 453.59237
    print(numero)
else:
    print("Eliga el numero del 1 al 6")
    """
#ac12
#a
"""def bisiesto(año):
    if(año%4==0 and año%100!=0):
        print("El año es bisiesto")
    elif(año%400==0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
bisiesto(año=2023)
"""
#b
"""def bisiesto(año,año_pasado):
    año=int(input("Ingrese el año en el que se encuentra: "))
    año_pasado=int(input("Ingrese hasta que año quiere que se revise que años son bisiestos: "))
    for i in range(año,año_pasado):
        if(año%4==0 and año%100!=0):
            print("El año es bisiesto")
        elif(año%400==0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
        año=año+1
bisiesto(año=2300,año_pasado=2900)
"""
#act13
"""aux=0
for i in range(1,1000):
    if(i%3==0):
        aux=i+aux
    elif(i%5==0):
        aux=i+aux
print(aux)
"""
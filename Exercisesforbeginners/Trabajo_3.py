#act1
"""numero=float(input("Ingrese un numero decimal: "))
if(numero<0):
    print("El numero es negativo")
"""
#act2
"""numero=float(input("Ingrese un numero decimal: "))
if(numero>=0):
    print("El numero es positivo")
"""
#act3
"""Edad1=int(input("Ingresa tu edad: "))
Edad2=int(input("Ingresa la edad de la otra persona: "))
if(Edad1<Edad2):
    print("La primera persona es menor que la segunda")
elif(Edad1==Edad2):
    print("Ambos poseen la misma edad")
else:
    print("La segunda persona es menor que la primera")
"""
#act4
"""numero=int(input("Ingresa un numero y te dire si es par o impar: "))
numero=numero%2
if(numero==0):
    print("El numero es par")
else:
    print("El numero es impar")
"""
#act5
"""notareal=float(input("Ingresa la nota del examen: "))
print("Nota cualitativa: ")
if(notareal<5):
    print("Suspenso")
elif(notareal>=5 and notareal<7):
    print("Aprobado")
elif(notareal>=7 and notareal<8.5):
    print("Notable")
elif(notareal>=8.5 and notareal<10):
    print("Sobresaliente")
else:
    print("Matricula de Honor")
"""
#act6
"""i=0
while(i!=100):
    i=i+1
    print(i)
print("La tarea ya ha finalizado")
"""
#act7
"""i=int(input("Ingrese el valor inicial: "))
f=int(input("Ingrese el valor final: "))
p=int(input("Ingrese de cuanto a cuanto ira: "))
print("El programa ira de",i,"hasta",f,"de",p,"en",p)
while(i!=f):
    i=i+p
    print(i)
"""
#act8
"""numero=int(input("Ingrese el numero a factorializar: "))
acumulador=1
while(numero!=1):
    acumulador=acumulador*numero
    numero=numero-1
print(acumulador)
"""
#act9
"""n=5
while(n!=150):
    n=n+1
    if(n%6==0):
        print(n)
"""
#act10
"""n=int(input("Elige desde que numero comenzara la lista: "))
m=int(input("Elige hasta que numero ira la lista: "))
i=n
n=n-1
while(n!=m):
    n=n+1
    if(n==i):
        print(n)
    elif(n%i==0):
        print(n)
"""
#act11
"""numero=int(input("Ingrese el numero a multiplicar: "))
for i in range(1,11):
    resultado=numero*i
    print(numero,"x",i,"=",resultado)
"""
#act12
"""euros=int(input("Ingrese su cantidad de euros: "))
c500=0
c200=0
c100=0
c50=0
c20=0
c10=0
c5=0
c2=0
c1=0
for i in range(1,euros,500):
    if(500>euros):
        euros=euros+500
        c500=c500-1
    c500=c500+1
    euros=euros-500
print(euros)
print("Billetes de 500: ",c500)    
for i in range(1,euros,200):
    if(200>euros):
        euros=euros+200
        c200=c200-1
    c200=c200+1
    euros=euros-200
print(euros)
print("Billetes de 200: ",c200)  
for i in range(1,euros,100):
    if(100>euros):
        euros=euros+100
        c100=c100-1
    c100=c100+1
    euros=euros-100
print(euros)
print("Billetes de 100: ",c100) 
for i in range(1,euros,50):
    if(50>euros):
        euros=euros+50
        c50=c50-1
    c50=c50+1
    euros=euros-50
print(euros)
print("Billetes de 50: ",c50)
for i in range(1,euros,20):
    if(20>euros):
        euros=euros+20
        c20=c20-1
    c20=c20+1
    euros=euros-20
print(euros)
print("Billetes de 20: ",c20)
for i in range(1,euros,10):
    if(10>euros):
        euros=euros+10
        c10=c10-1
    c10=c10+1
    euros=euros-10
print(euros)
print("Billetes de 10: ",c10)
for i in range(1,euros,5):
    if(5>euros):
        euros=euros+5
        c5=c5-1
    c5=c5+1
    euros=euros-5
print(euros)
print("Billetes de 5: ",c5)
for i in range(1,euros,2):
    if(2>euros):
        euros=euros+2
        c2=c2-1
    c2=c2+1
    euros=euros-2
print(euros)
print("Billetes de 2: ",c2)
if(euros==1):
    euros=euros-1
    c1=c1+1
    print(euros)
    print("Billetes de 1: ",c1)
"""
#act13
"""for i in range(0,201):
    if(i%2==0):
        print(i)
"""
#act14
"""for i in range(201,-1,-1):
    if(i%2==0):
        print(i)
"""
#act15
"""f=int(input("Ingrese hasta que numero debe llegar la busqueda de numeros pares positivos: "))
for i in range(2,f):
    if(i%2==0):
        print(i)
"""
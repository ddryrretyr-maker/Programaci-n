#Capicuba o Palindrome
def capicua(num):
    original=num
    suma_digitos=0
    while num>0:
        digito=num%10
        num=num//10
        suma_digitos=suma_digitos*10+digito
    if suma_digitos==original:
        return 1
    else:
        return 0
#principal
num=int(input("Ingrese un numero: "))
while num>0:
    capi=capicua(num)
    if capi==1:
        print("El numero es capicua")
    else:
        print("El numero no es capicua")
    num=int(input("Ingrese un numero: "))
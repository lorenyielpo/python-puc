#x = 15
#if x == 10:
#    print('batata')
#elif x == 15:
#    print('fritas')
#else:
#    print('strogonoff')


#for i in range(0,10,1):
#    print(i)


#z = int(input('digite um número'))
#x = 0
#y = 0

#while x < z:
#    if y%2 == 0:
#        x += 1
#        print(y)
#    y += 1


#def Media():
#    A1 = int(input('digite a nota da A1 '))
#    A2 = int(input('digite a nota da A2 '))
#    P2 = int(input('digite a nota da P2 '))
#    P1 = int(input('digite a nota da P1 '))

#    N1 = (A1 + P1*2)/3
#    N2 = (A2 + P2*2)/3

#    NF = (N1 + N2)/2

#    print("{:^2.2f}".format(NF))
    
#Media()



#num = int(input('digite um numero'))
#divisores = 0

#for i in range (1,num + 1, 1):
#    if num % i == 0:
#        divisores += 1

#if divisores == 2:
#    print('é primo')
#else:
#    print('não é primo')

#soldados = int(input('digite o numero de soldados no batalhão '))
#fila = 0
#soldFilas = 0

#while soldados > 0:
#    soldFilas += 1
#    soldados -= soldFilas
#    fila += 1
    
#print('tem', fila, 'filas')
#if soldados < 0:
#    print('e restaram', soldados + soldFilas, 'soldados na última fileira')

import time
import os

def Wait():
    k = input("Pressione uma enter para continuar")

#def MinFloor():
#    subsolo = input('Existe subsolo? <sim/nao>').strip().lower()
#    if subsolo == "nao":
#        minFloor = 0
#        return minFloor
#    elif subsolo == "sim":
#        minFloor = int(input('Quantos andares?'))
#        return -minFloor

def Floors(maxFloor, actualFloor, minFloor):
    for i in range(maxFloor, minFloor-1, -1):
        if i == actualFloor:
            print("(|)", actualFloor)
        else:
            print(" | ", i)

def FromToUp(actualFloor,floorNumber,minFloor):
    for actualFloor in range(actualFloor, floorNumber+1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)
    return actualFloor

def FromToDown(actualFloor,floorNumber,minFloor):
    for actualFloor in range(actualFloor, floorNumber-1, -1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)  
    return actualFloor



## Loop
while True:
    os.system('cls')
    maxFloor = int(input("Quantos andares tem o prédio ?"))
    actualFloor = 0
    end = False

    while True:
        x = input("o prédio tem subsolo? <sim/nao> ").strip().lower()
        if subsolo == "nao":
        minFloor = 0
        break
    elif subsolo == "sim":
        minFloor = -int(input('Quantos andares?'))
        break

    while end == False:
        floorNumber = minFloor-1
        while (floorNumber < minFloor or floorNumber > maxFloor)
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        floorNumber = int(input("digite qual andar quer visitar: "))
        if (floorNumber < minFloor or floorNumber > maxFloor):
            print('Digite um número válido')
            wait()

        # Check posição
        if (floorNumber > actualFloor):
            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)

        elif (floorNumber < actualFloor):
            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)

        print('Voce chegou ao seu destino!')
        Wait()

        # Check
        x = input("Deseja ir para outro andar ? <sim/nao> ").lower().strip()
        if x == "sim":
            continue
        elif x == "nao":
            end = True

    x = input("Deseja encerrar o programa? <sim/nao>").lower().strip()
    if x == "sim":
        exit()
    elif x == "nao":
        continue

        

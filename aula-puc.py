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

#import time
#import os

#def Wait():
#    k = input("Pressione uma enter para continuar")

#def MinFloor():
#    subsolo = input('Existe subsolo? <sim/nao>').strip().lower()
#    if subsolo == "nao":
#        minFloor = 0
#        return minFloor
#    elif subsolo == "sim":
#        minFloor = int(input('Quantos andares?'))
#        return -minFloor

#def Floors(maxFloor, actualFloor, minFloor):
#    for i in range(maxFloor, minFloor-1, -1):
#        if i == actualFloor:
#            print("(|)", actualFloor)
#        else:
#            print(" | ", i)

#def FromToUp(actualFloor,floorNumber,minFloor):
#    for actualFloor in range(actualFloor, floorNumber+1):
#        os.system('cls')
#        Floors(maxFloor, actualFloor, minFloor)
#        time.sleep(1)
#    return actualFloor

#def FromToDown(actualFloor,floorNumber,minFloor):
#    for actualFloor in range(actualFloor, floorNumber-1, -1):
#        os.system('cls')
#        Floors(maxFloor, actualFloor, minFloor)
#        time.sleep(1)  
#    return actualFloor



## Loop
#while True:
#    os.system('cls')
#    maxFloor = int(input("Quantos andares tem o prédio ?"))
#    actualFloor = 0
#    end = False

#    while True:
#        x = input("o prédio tem subsolo? <sim/nao> ").strip().lower()
#        if subsolo == "nao":
#        minFloor = 0
#        break
#    elif subsolo == "sim":
#        minFloor = -int(input('Quantos andares?'))
#        break

#    while end == False:
#        floorNumber = minFloor-1
#        while (floorNumber < minFloor or floorNumber > maxFloor)
#        os.system('cls')
#        Floors(maxFloor, actualFloor, minFloor)
#        floorNumber = int(input("digite qual andar quer visitar: "))
#        if (floorNumber < minFloor or floorNumber > maxFloor):
#            print('Digite um número válido')
#            wait()

#        # Check posição
#        if (floorNumber > actualFloor):
#            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)

#        elif (floorNumber < actualFloor):
#            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)

#        print('Voce chegou ao seu destino!')
#        Wait()

#        # Check
#        x = input("Deseja ir para outro andar ? <sim/nao> ").lower().strip()
#        if x == "sim":
#            continue
#        elif x == "nao":
#            end = True

#    x = input("Deseja encerrar o programa? <sim/nao>").lower().strip()
#    if x == "sim":
#        exit()
#    elif x == "nao":
#        continue

#lista = ["Maça", "Banana", "Cereja"]
#lista[1] = "Goiaba"

#lista.append("Goiaba")
#print(lista)

#if "Maça" in lista:
#    print("sim, maçã está na lista de frutas")

#for x in lista:
#    print(x)

#import os
#import time
#import random

#def Wait():
#    k = input("Pressione enter para continuar")

#def Draw(x):
#    if x == 6:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" | /|\ ")
#        print(" | / \ ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 5:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" | /|\ ")
#        print(" |   \ ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 4:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" | /|\ ")
#        print(" |     ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 3:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" | /|  ")
#        print(" |     ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 2:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" |  |  ")
#        print(" |     ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 1:
#        print(" ---|  ")
#        print(" |  o  ")
#        print(" |     ")
#        print(" |     ")
#        print(" |     ")
#        print("_|_    ")
#    elif x == 0:
#        print(" ---|  ")
#        print(" |     ")
#        print(" |     ")
#        print(" |     ")
#        print(" |     ")
#        print("_|_    ")

#def StringToArray(word):
#    word = list(word)
#    return word

#def HiddenWord(word):
#    hiddenWord = []
#    for x in word:
#        hiddenWord.append("-")
#    return hiddenWord
    
#def Game():
#    storage = ["azul", "vermelho", "verde", "amarelo", "roxo"]
#    word = storage[random.randrange(len(storage))]
#    wordArray = StringToArray(word)
#    hiddenWord = HiddenWord(word)
#    error = 0
#    tries = []
#    wordLenght = len(word)

#    while error < 7 and wordLenght > 0:
#        os.system('cls')
#        Draw(error)

#        for x in hiddenWord:
#            print(x, end = '')
#        print()

#        for i in tries:
#            print(i, end = ', ')
#        print()

#        guess = input("Digite uma letra: ").lower().strip()

#        if guess in tries:
#            error += 1
#        else:
#            if guess not in wordArray:
#                error += 1

#            for x in range (len(word)):
#                if guess == wordArray[x]:
#                    hiddenWord[x] = wordArray[x]
#                    wordLenght -= 1
#
#
#            ##Adicionar tentativa

#            tries.append(guess)

#    ## Check de vitoria
#    if error < 7:
#        print("Você ganhou")
#    else:
#        print("Você perdeu")
        
#    Wait()

#    while True:
#        x = input("Deseja jogar novamente? <sim/nao> ").lower().strip()

#        if x == "sim":
#            Game()
#        elif x == "nao":
#            exit()
    
#Game()

import os
import random

def Wait():
    k = input("Pressione enter para continuar")


def Jokenpo():
    objetos = ["pedra", "papel", "tesoura"]
    pontosPc = 0
    pontosGamer = 0

    while pontosPc < 3 and pontosGamer < 3:
        computador = objetos[random.randrange(len(objetos))]
        jogador = input("Escolha uma opção? <pedra/papel/tesoura> ").lower().strip()
        os.system('cls')
        print("O computador escolheu: ",computador)

        if computador == "pedra" and jogador == "papel":
            pontosGamer += 1
        elif computador == "papel" and jogador == "tesoura":
            pontosGamer += 1
        elif computador == "tesoura" and jogador == "pedra":
            pontosGamer += 1
        elif jogador == "pedra" and computador == "papel":
            pontosPc += 1
        elif jogador == "papel" and computador == "tesoura":
            pontosPc += 1
        elif jogador == "tesoura" and computador == "pedra":
            pontosPc += 1

        print("Pontos do computador: ", pontosPc, ", seus pontos: ", pontosGamer)

    ## Check de vitoria
    if pontosGamer == 3:
        print("Você ganhou")
    elif pontosPc == 3:
        print("Você perdeu")

    Wait()

    while True:
        x = input("Deseja jogar novamente? <sim/nao> ").lower().strip()

        if x == "sim":
            os.system('cls')
            Jokenpo()
        elif x == "nao":
            exit()

Jokenpo()










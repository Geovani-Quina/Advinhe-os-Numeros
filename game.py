import random
import os
import time

hit = 0
wrong = 0
while True:
    print(r"""
░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗██╗░░██╗███████╗  ░█████╗░░██████╗
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██║░░██║██╔════╝  ██╔══██╗██╔════╝
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║█████╗░░  ██║░░██║╚█████╗░
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║██╔══╝░░  ██║░░██║░╚═══██╗
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║███████╗  ╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═════╝░

███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░░██████╗
████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗██╔════╝
██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║╚█████╗░
██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║░╚═══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██████╔╝
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═════╝░""")
    print('blanq to quit')
    print('======================================')
    number1 = random.randint(1,11)
    number2 = random.randint(1,11)
    print(f'SOMA: {number1 + number2}')
    print(f'SUBTRAÇÃO: {number1 - number2}')
    print(f'MULTIPLICAÇÃO: {number1 * number2}')
    print(f'DIVISÃO: {number1/number2:.1f}')
    print('======================================')
    try:
        guess1 = float(input('Qual você acha que foi o 1º número? '))
        guess2 = float(input('Qual você acha que foi o 2ª número? '))
        if guess1 == number1 and guess2 == number2:
            print('certo :-)')
            hit += 1
        else:
            print(f'Errado, o certo seria {number1} e {number2} :(')
            wrong += 1
        time.sleep(3)
        print('Preparando novo jogo!')
        os.system('cls')
    except ValueError:
        break
print('Fim do jogo :(')
if hit >= wrong:
    print(f'Você acertou {hit} e errou {wrong}, Parabéns!')
else:
    print(f'Você acertou {hit} e errou {wrong}, Continue Jogando!')
    
    
"""
Crie um programa com selenium que:
    1. Jogue o jogo
    2. Quando voce ganhar, o script deve parar de ser executado.
    url: https://curso-python-selenium.netlify.app/exercicio_02.html
"""

from curses import KEY_ENTER
from selenium.webdriver import Firefox
from time import sleep
from random import randint


browser = Firefox()
browser.get(url='https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(2)

numero_esperado = browser.find_element_by_tag_name('p')
numero_esperado = str(randint(1, 10))
print(numero_esperado)
sleep(2)

x = 0
for i in range(20):
    try:
        input('click no botão: ')
        numero_sorteado = browser.find_element_by_id("ancora")
        numero_sorteado.send_keys(KEY_ENTER)
        numero_sorteado = randint(1, 10)
        print(numero_sorteado)
        x += 1
        if numero_sorteado != numero_esperado:
            print('O número sorteado é diferente do número esperado!')
            input('click novamente: ')
        else:
            print(f'PARABÉNS!, VOCE GANHOU APÓS {x} NÚMEROS SORTEADOS')
            break
    except Exception as e:
        print('SINTO MUITO!, voce ultrapassou a quantidade permitida de tentativas.')
        break


sleep(5)
browser.quit()

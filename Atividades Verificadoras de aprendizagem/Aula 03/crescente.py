'''Desenvolva um algoritmo que escreve em disco um arquivo com números ordenados crescentemente
de 1 a 100. Cada número deve ser separado por “;”. O arquivo deve se chamar “crescente.txt”.
'''
def listaCrescente(min, max):
    with open('crescente.txt', 'w', encoding='UTF-8') as arquivo:
        for i in range(min, max+1):
            arquivo.write(f'{i};')

listaCrescente(1,100) 
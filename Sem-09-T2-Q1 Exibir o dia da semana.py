# Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.

def mostra_dia_da_semana(dia):
    if(dia == 1):
        print('domingo')
    elif(dia == 2):
        print('segunda-feira')
    elif(dia == 3):
        print('terça-feira')
    elif(dia == 4):
        print('quarta-feira')
    elif(dia == 5):
        print('quinta-feira')
    elif(dia == 6):
        print('sexta-feira')
    elif(dia == 7):
        print('sábado')
    else:
        print('valor inválido')


def main():
    dia_da_semana = input()
    dia_da_semana = int(dia_da_semana)

    mostra_dia_da_semana(dia_da_semana)

if __name__ == '__main__':
    main()
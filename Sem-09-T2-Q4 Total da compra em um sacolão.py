#Um sacolão está vendendo frutas com a seguinte tabela de preços:

#Item|Até 5Kg|Acima de 5Kg

#:--------- |:-------------:| :----------:

#Morango | R$ 2,50 | R$ 2,20

#Maça | R$ 1,80 | R$ 1,50

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def valor_morango(kg_morango):
    valor = 0
    if(kg_morango <= 5):
        valor = kg_morango * 2.5
    elif(kg_morango > 5):
        valor = kg_morango * 2.2

    return valor

def valor_maca(kg_maca):
    valor = 0 
    if(kg_maca <= 5):
        valor = kg_maca * 1.8
    elif(kg_maca > 5):
        valor = kg_maca * 1.5 
    return valor

def desconto(valor):
    return valor - (valor*10/100)   

def valor_final(kg_maca, kg_morango):
    valor = valor_maca(kg_maca) + valor_morango(kg_morango)
    if((kg_maca + kg_morango) > 8 or ((valor_maca(kg_maca) + valor_morango(kg_morango)) > 25)):
        valor = desconto(valor)
    return valor

def main():
    quantidade_kg_morango = input()
    quantidade_kg_maca = input()

    quantidade_kg_morango = float(quantidade_kg_morango)
    quantidade_kg_maca = float(quantidade_kg_maca)

    resultado = valor_final(quantidade_kg_maca, quantidade_kg_morango)
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
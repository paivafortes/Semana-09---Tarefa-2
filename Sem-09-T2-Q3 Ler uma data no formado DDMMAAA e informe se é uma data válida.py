#Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.

#OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.

def dia_e_valido(data):
    dia = data[0] + data[1]

    return (31 >= int(dia) > 0)

def dia(data):
    dia = data[0] + data[1]
    if(31 >= int(dia) > 0):
        return int(dia)

def mes_e_valido(data):
    mes = data[2] + data[3]

    return (0 < int(mes) <= 12)

def mes(data):
    mes = data[2] + data[3]
    if(0 < int(mes) <= 12):
        return int(mes)


def ano_e_valido(data):
    ano = data[4] + data[5] + data[6] + data[7]

    return (10000 > int(ano) > 0)

def ano_e_bissexto(data):
    ano_dezena = data[6] + data[7]
    ano_centena = data[4] + data[5] + data[6] + data[7]
    status = False
    if(int(ano_dezena) % 4 == 0 and int(ano_dezena)!=0):
        status = True
    if(int(ano_centena)% 100 == 0 and int(ano_centena)% 400 == 0):
        status = True  
    if(int(data[4] + data[5] + data[6] + data[7]) == 1900):
        status = True    
    return status

def e_uma_data_valida(data):
    if(ano_e_valido(data) and mes_e_valido(data) and dia_e_valido(data)):
        if((mes(data)==4 or mes(data)==6 or mes(data)== 9 or mes(data)==11) and dia(data) > 30):
            return False
        elif mes(data) == 2 and (dia(data) > 29 or (dia(data) > 28) and not ano_e_bissexto(data)):
            return False
        else:
            return True
    else:
        return False
def main():
    data = input().strip()

    if(len(data) != 8):
        print('False')
    else:
        resultado = e_uma_data_valida(data)

        print(f'{resultado}')

if __name__ == '__main__':
    main()
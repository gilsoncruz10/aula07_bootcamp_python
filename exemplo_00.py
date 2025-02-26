valor_1 = 3
valor_2 = 7
valor_4 = 30
valor_5 = 50

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """"
    uma funcao simples de soma de valores tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_4, valor_5)

print(valor_3)
print(valor_6)
# Calcular Média de Valores em uma Lista

from typing import List

lista_1 = [1,3,7,10]
lista_2 = [20,21,19,22,18]
lista_3 = [4.5,100.0]

def calcular_media(valores: List[float]) -> float:

    """
    soma os valores da lista numerica e divide pela quantidade de valores
    """
    media_da_lista = sum(valores)/len(valores)
    return media_da_lista

media_1 = calcular_media(lista_1)
media_2 = calcular_media(lista_2)
media_3 = calcular_media(lista_3)

print(media_1)
print(media_2)
print(media_3)

# Filtrar Dados Acima de um Limite

from typing import List

# Passo a passo:
# 1) receber uma lista de dados
# 2) comparar com um limite
# 3) excluir dados acima do limite
# 4) imprimir a lista filtrada

dados_1 = [13, 15, 37, 78, 105]
dados_2 = [11, 75, 137, 178, 205]
dados_3 = [130, 150, 370, 780, 1500]

def filtrar_valores_acima_de_100(dados_duvidosos: List[int]) -> List[int]:
    """
    filtra valores da lista e retorna lista atualizada de valores abaixo do limite
    """
    filtrados = [n for n in dados_duvidosos if n < 100]
    #if not filtrados:
    #    print ("Todos os valores são maiores do que o filtro selecionado")
        
    return filtrados

filtrados_1 = filtrar_valores_acima_de_100(dados_1)
filtrados_2 = filtrar_valores_acima_de_100(dados_2)
filtrados_3 = filtrar_valores_acima_de_100(dados_3)

print(filtrados_1)
print(filtrados_2)
print(filtrados_3)
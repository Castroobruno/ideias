# cada venda o vendedor ganha 2 reais mais 1% do valor da venda
# calcular o valor total de bonus e o valor do bonus de casa vendedor

vendas = {"André": [1000, 500, 300, 5000, 1500, 80, 3000],
          "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
          "Alan": [800, 100],
          "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]}


def calcular_bonus(lista_vendas): # 3 defino a logica = calcular_bonus - usando uma lista_vendas - retornar o valor do bonus
    qtd = len(lista_vendas)
    bonus1 = qtd * 2 
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus = bonus1 + bonus2
    return bonus

bonus_total = 0
for vendedor in vendas:
    lista_vendas_v = vendas[vendedor] # 1 essa linha eu apenas encontrei a lista de venda de cada vendedor
    bonus = calcular_bonus(lista_vendas_v) # 2 aqui monto a equacao - a informacao calcula_bonus, precisa ser calculada ainda
    print(f"Vendedor:{vendedor} Bonus:{bonus}")
    bonus_total = bonus_total + bonus
print(bonus_total)
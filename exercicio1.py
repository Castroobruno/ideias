# cada venda o vendedor ganha 2 reais mais 1% do valor da venda
# calcular o valor total de bonus e o valor do bonus de casa vendedor

vendas = {"André": [1000, 500, 300, 5000, 1500, 80, 3000],
          "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
          "Alan": [800, 100],
          "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]}

def valor_bonus(lista_cada_vendedor):
    qtd = len(lista_cada_vendedor)
    bonus1 = qtd * 2
    valor_total = sum(lista_cada_vendedor)
    bonus2 = valor_total * 0.01
    bonus = bonus1 + bonus2
    return bonus
    


bonus_total = 0
for vendedor in vendas:
    lista_cada_vendedor = vendas[vendedor]
    bonus = valor_bonus(lista_cada_vendedor)
    print(f"Vendedor: {vendedor}\nBonus: R${bonus}")
    bonus_total = bonus_total + bonus
print (f"Bonus total: R${bonus_total:,.2f}")


nota_matematica = 7.0
nota_ciencias = 8.5
nota_historia = 9.5

peso_matematica = 2
peso_ciencias = 3
peso_historia = 5

pontos_totais = (nota_matematica * peso_matematica) + (nota_ciencias * peso_ciencias) + (nota_historia * peso_historia)

soma_pesos = peso_matematica + peso_ciencias + peso_historia

media_ponderada = pontos_totais / soma_pesos

print(f"A sua média ponderada é: {media_ponderada:.1f}")
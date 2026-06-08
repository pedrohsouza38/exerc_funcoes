# exerc_funcoes
Exercícios de Lógica com Python usando Funções

Exercícios Funções

Funções são blocos de código que nos permitem organizar e reutilizar tarefas em nossos programas. 
Elas são uma parte fundamental da programação e nos ajudam a escrever código mais limpo, eficiente e modular.

Para praticar o que aprendemos, temos uma série de exercícios que envolvem o uso de funções básicas para realizar cálculos simples. 
Vocês deverão CRIAR FUNÇÕES QUE RECEBEM ARGUMENTOS E RETORNAM RESULTADO para resolver os problemas propostos. 
Lembre-se de usar nomes significativos para suas funções e variáveis, para que o código seja claro e compreensível.

Exercício 1: Calcular a área de um retângulo
Situação Problema: Você está construindo um jardim retangular em sua casa. A largura do jardim é 5 metros e o comprimento é 8 metros. Qual é a área total do jardim?

largura = 5
comprimento = 8

area_total = largura * comprimento

print(f"A área total do jardim é de {area_total} metros quadrados.")

Exercício 2: Converter Celsius para Fahrenheit
Situação Problema: Você está em um país onde a temperatura é medida em Fahrenheit. A temperatura atual é 25 graus Celsius. Qual é a temperatura equivalente em Fahrenheit?

def celsius_para_fahrenheit():

    celsius = float(input("Digite a temperatura em graus Celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius:.1f} °C equivalem a {fahrenheit:.1f} °F")

if __name__ == "__main__":
    celsius_para_fahrenheit()

Exercício 3: Calcular o perímetro de um quadrado
Situação Problema: Você está construindo um tapete quadrado para a sala de estar. Cada lado do tapete mede 3 metros. Qual é o perímetro total do tapete?

lado_tapete = 3

perimetro_total = 4 * lado_tapete

print(f"O perímetro total do tapete é: {perimetro_total} metros")

Exercício 4: Calcular a média ponderada de três notas
Situação Problema: Você está estudando para três disciplinas diferentes. Suas notas são: 7.0 em Matemática, 8.5 em Ciências e 9.5 em História. Se a Matemática tem peso 2, Ciências tem peso 3 e História tem peso 5, qual é a sua média ponderada?

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

Exercício 5: Converter quilômetros para milhas
Situação Problema: Você está planejando uma viagem de carro. O percurso tem 200 quilômetros de extensão. Qual é a distância equivalente em milhas?

quilometros = 200

fator_conversao = 0.621371

milhas = quilometros * fator_conversao

print(f"A distância do percurso de {quilometros} km equivale a {milhas:.2f} milhas.")

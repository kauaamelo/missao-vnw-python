# Missão 4: Restaurando a Identificação de Números ⚖️
# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas.
# No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
# [ Crie um programa que peça dois números ao usuário e exiba a soma deles. ]

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

def somar():
  resultado_soma = primeiro_numero + segundo_numero
  print(f"A soma do numero {primeiro_numero} com o numero {segundo_numero} é: {resultado_soma}")
  print(f"\033[4;33;44m {primeiro_numero} + {segundo_numero} = {resultado_soma} \033[m")

somar()
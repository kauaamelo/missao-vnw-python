# Missão 2: O Sistema Eleitoral Secreto 📝
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações,
# mas o vírus desativou a verificação de elegibilidade para votar!
# Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar
# (mínimo: 16 anos).

idade_elegivel = 16

nome = input("Olá aluno da Escola VNW, qual é o seu nome ? ")
idade = int(input("Vamos descobrir se você pode votar,\nQual é a sua idade ? "))

def aprovado_votacao():
  print(f"\n{nome}, você tem {idade} anos, você PODE votar!")

def reprovado_votacao():
  print(f"\n{nome}, você tem {idade} anos, NÃO pode votar!")

if idade >= idade_elegivel:
  aprovado_votacao()
else:
  reprovado_votacao()
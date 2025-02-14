# Missão 1: Restaurando a Regras Escolares 📝
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o
# Professor Byte a organizar o sistema, sua tarefa é criar um programa que
# verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

nota_aprovacao = 6

nome = input("Olá aluno, qual é o seu nome ? ")
nota = float(input("Qual é a sua nota atual ? "))

def aluno_aprovado():
    print(f'Aluno aprovado, com nota: {nota}')
    print(f'Parabéeeens {nome}')

def aluno_reprovado():
    print(f'Aluno reprovado, com nota: {nota}')
    print(f'Você precisa de ajuda, procure o instrutoríssimo João (:')

if nota >= nota_aprovacao:
  aluno_aprovado()
else:
  aluno_reprovado()
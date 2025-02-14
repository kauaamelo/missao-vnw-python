# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F.
# Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:
# A (90-100) – "Parabéns, você tirou A!" / B (80-89) – "Muito bem, você tirou B." / C (70-79) – "Bom trabalho, você tirou C."
# D (60-69) – "Fique atento, você tirou D." / F (menos de 60) – "Estude um pouco mais, você tirou F."

nome = input("Olá maravilhoso(a) aluno(a) do Vai Na Web, qual é o seu nome ? ")

while True:
  nota = float(input(f"{nome}, me conte qual foi a sua nota de 0 a 100 ? "))

  def nota_a():
    print(f"Parabéns {nome}, você tirou A!")

  def nota_b():
    print(f"Muito bem {nome}, você tirou B.")

  def nota_c():
    print(f"Bom trabalho {nome}, você tirou C.")

  def nota_d():
    print(f"Fique atento {nome}, você tirou D.")

  def nota_f():
    print(f"Estude um pouco mais {nome}, você tirou F. \nEncerrando o programa.")

  if nota >= 90:
    nota_a()
  elif nota >= 80:
    nota_b()
  elif nota >= 70:
    nota_c()
  elif nota >= 60:
    nota_d()
  else:
    nota_f()
    break

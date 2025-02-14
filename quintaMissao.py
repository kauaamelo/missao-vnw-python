# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! 
# Agora, apenas quem souber a combinação correta poderá acessá-lo. Crie um programa que solicite
# ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

senha_correta = "Python123"

while True:
  senha_digitada = input("Digite a senha para abrir o cofre: ")

  if senha_correta != senha_digitada:
    print("Senha incorreta! Tente novamente.")
  else:
    print("Muito bem! Você acertou a senha.")
    break
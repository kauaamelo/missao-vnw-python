# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# Crie uma função que receba um nome e diga quantas letras esse nome tem.

nome = input("Digite seu nome e descubra quantas letras ele tem: ")
converter_nome = nome.replace(" ", "")
quantidade_letras = (len(converter_nome))

print(f"Seu nome tem {quantidade_letras} letras.")
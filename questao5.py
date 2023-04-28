string = input("Digite uma string: ") # entrada da string
inverted_string = "" # string invertida

# percorre a string da direita para a esquerda, adicionando cada caractere à string invertida
for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print("String invertida: ", inverted_string) # exibe a string invertida

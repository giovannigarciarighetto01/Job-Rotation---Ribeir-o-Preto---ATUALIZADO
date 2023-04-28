# solicita ao usuário um número para verificar se pertence à sequência de Fibonacci
num = int(input("Digite um número: "))

# inicializa os valores iniciais da sequência de Fibonacci
a = 0
b = 1

# verifica se o número pertence à sequência de Fibonacci
while b < num:
    c = a + b
    a = b
    b = c

# exibe uma mensagem informando se o número pertence ou não à sequência
if b == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")

def soma():
    soma = numb1 + numb2
    print(f'{numb1} + {numb2} = {soma}')

def subtracao():
    sub = numb1 - numb2
    print(f'{numb1} - {numb2} = {sub}')

def multiplicacao():
    mult = numb1 * numb2
    print(f'{numb1} * {numb2} = {mult}')

def divisao():
    div = numb1 / numb2
    print(f'{numb1} / {numb2} = {div}')

operacao = input("Digite a operação que deseja [+]Soma [-]Subtração [*]Multiplicação [/]Divisão: ")
numb1 = float(input("Digite o primeiro número: "))
numb2 = float(input("Digite o segundo número: "))

if operacao == '+':
    soma()
elif operacao == '-':
    subtracao()
elif operacao == '*':
    multiplicacao()
elif operacao == '/':
    divisao()
else:
    print("Opção indisponível")
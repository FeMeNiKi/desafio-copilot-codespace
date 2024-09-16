palav = input("Digite a palavra que será analisada: ")

if palav == palav[::-1]:
    print(f'{palav} é um palíndromo!')
else:
    print(f'{palav} não é um palíndromo!')
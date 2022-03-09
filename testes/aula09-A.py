frase = 'Curso em Video Python'
# mostrando o caractere 3
print(frase[3])
#mostrando do carac 3 ao 13
print(frase[3:13])
#mostrando do carac 0 ao 13
print(frase[:13])
#mostrando do carac 13 ao final
print(frase[13:])
# mostrando todos carac pulando de 2 em 2
print(frase[::2])

#para imprimir um texto pulando de linha coloque 3 aspas simples no inicio e no fim do texto
print("""bruno
dayane
ivone
pedro""")

#contando quantas vezes o caractere se repete
print(frase.count('o'))
print(frase.count('deo'))
#para saber o tamanha do espaço ocupado pela variavel
print(len(frase))
#para remover os espaços em branco na variavel
#podendo começar pela direita rstrip ou pela esquerda lstrip
print(frase.strip())
#para substituir uma variavel
print(frase.replace('Python', 'android'))
#para saber se contem na variavel mostrando True ou False
print('curso' in frase)
print('Python' in frase)
#para encontrar algo na variavel e mostrar em qual posição começa se não conter mostra -1
print(frase.find('video'))
print(frase.find('Python'))
#dividindo a variavel por palavras
print(frase.split())

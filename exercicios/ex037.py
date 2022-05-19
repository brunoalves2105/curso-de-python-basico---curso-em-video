num = int(input('digite um numero inteiro: '))
print('''escolha uma bases para conversão: 
    [1] CONVERTER BINARIO
    [2] CONVERTER OCTAL
    [3] CONVERTER HEXADECIMAL''')
opcao = int(input('digite sua opção: '))
if opcao == 1:
   print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida, tente novamente')
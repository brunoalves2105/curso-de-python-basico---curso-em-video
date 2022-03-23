# a linguagem python segue o padrão ANSI de cores
#print('\033[1;33;44mola\033[m mundo')
a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
nome = 'bruno'
# usando o format para indicar a cor
print('prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
# usando array de objetos para fazer cores
cores = {
    'limpa' : '\033[m',
    'amarelo' : '\033[33m',
    'azul' : '\033[34m',
    'pretobranco' : '\033[7;30m'
}
print('ola novamente {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('ola novamente {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))
print('ola novamente {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
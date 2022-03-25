# estrutura de repetição composta

nome = str(input('digite seu nome: '))
if nome == 'bruno':
    print('ola {}, que nome lindo :)'.format(nome))
elif nome == 'maria' or nome == 'pedro' or nome =='paulo' or nome == 'joao':
    print('ola {}, seu nome é popular no Brasil :)'.format(nome))
else:
    print('ola {}, prazer em te conhecer :)'.format(nome))
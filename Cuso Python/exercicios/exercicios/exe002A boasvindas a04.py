cores = {'limpesa':'\033[m', 'sian':'\033[0;36m', 'red':'\033[0;31m'}
nome = input('{}Qual é o seu nome?{}'.format(cores['sian'], cores['limpesa']))
print('{}Olá {}{}{}, prazer em te conhecer!{} '.format(cores['sian'], cores['red'], nome, cores['sian'], cores['limpesa']))

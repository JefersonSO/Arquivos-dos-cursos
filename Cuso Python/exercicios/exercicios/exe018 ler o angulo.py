tfrom math import radians, sin, cos, tan
A = float(input('digite o valor do angulo'))
sen = sin(radians(A))
co = cos(radians(A))
ta = tan(radians(A))
print(' O angulo de {} tem o SENO de {:.2f} \n O angulo de {} tem o COSSENO de {:.2f} ' .format(A, sen, A, co))
print('\n O angulo de {} tem a TANGENTE de {:.2f}'.format(A, ta))

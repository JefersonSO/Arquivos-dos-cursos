algoritmo "semnome"
// Função :
// Autor :
// Data : 14/07/2022
// Seção de Declarações 
var
 soma, c, v1, v2: Inteiro
inicio

 Escreval("valor 1: ")
 Leia(v1)
 Escreval(" valor 2: ")
 Leia(v2)
 soma <- 0
 c <- v1
 Repita
    Escreval(c)
    soma <-  soma + c
    c <- c + 1


 Ate c > v2
 Escreval(" A soma dos inteiros entre ", v1, " e ", v2, " è ", soma )
fimalgoritmo

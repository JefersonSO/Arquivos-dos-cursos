algoritmo "mediadosinteiros de 01 100"

var
 ne15e100, c, num: Real
inicio
 c <- 15
 ne15e100 <- 0
 Repita
    ne15e100 <- ne15e100 + 1
    c <- c + 1
    num <- num + c
  Escreval(" calculando", c, ne15e100 )
 Ate c >  99
 Escreval(" numeros entre 15 e 100 ", ne15e100 )
 Escreval("media : ", num / c)
fimalgoritmo

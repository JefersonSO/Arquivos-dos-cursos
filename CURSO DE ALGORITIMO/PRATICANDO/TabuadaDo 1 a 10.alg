algoritmo "Tabuadado1a10 "
// Escreva um algoritmo que imprima a tabuada (de 1 a 10) para os números de 1 a 10.
var
 n,c:Inteiro
 
inicio
  Para n <- 1 ate 10 faca
   c <- 0
   Escreval("taboada do: ", n)
   Escreval("-------------------")
   Repita
    c <- c + 1
    Escreval(n, " x ", c:2, " = ", n * c:2)
   Ate c = 10
   Escreval("-------------------")
  FimPara
  fimalgoritmo

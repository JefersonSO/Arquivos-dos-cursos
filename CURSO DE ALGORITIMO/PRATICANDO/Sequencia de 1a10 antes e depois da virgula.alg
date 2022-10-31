algoritmo "sequenci1,ate 10"
// Escreva um algoritmo que imprima as seguintes seqüências de números: (1, 1 2 3 4 5 6 7 8 9 10)
//(2, 1 2 3 4 5 6 7 8 9 10) (3, 1 2 3 4 5 6 7 8 9 10) (4, 1 2 3 4 5 6 7 8 9 10) e assim sucessivamente, até
//que o primeiro número (antes da vírgula), também chegue a 10.

var
 C, n:Inteiro
inicio
 Para n <- 1 ate 10 faca
   Escreva("(",n,",")
   Para c <- 1 ate 10 faca
    Escreva( c)
    se c = 10 entao
      Escreva(")")
    FimSe
   fimPara
  FimPara
fimalgoritmo

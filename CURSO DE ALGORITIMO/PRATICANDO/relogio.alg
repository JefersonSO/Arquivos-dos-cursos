algoritmo "Relogio"
// Função : simulação do relogio em horas, minutos e segundos.
// Autor :
// Data : 28/05/2022
// Seção de Declarações 
var
  H, M, S: Inteiro

inicio
   H <- 0
   Escreval("--------------------------")
   Repita

      Escreval(" h:",H,  " min:", M, " s:", S)
      S <- S + 1
      Se S = 61 entao
         M <- M + 1
         S <- 0
      Se M = 61 entao
         H <- H + 1
         M <- 0

      FimSe
      FimSe
      Ate H = 2
    Escreval("--------------------------")
      
// Seção de Comandos 
fimalgoritmo

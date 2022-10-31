algoritmo "Rellogio"
// Função :
// Autor :
// Data : 22/05/2022
// Seção de Declarações 
var
  H, M , S, Mi: Inteiro
inicio

  Repita
    Escreval(H, ": ", M, ": ", S, ": ", Mi)
    Mi <- Mi + 1
    Se Mi > 60 entao
       S <- S +1
       Mi <- 0
    Se S > 60 entao
       M <- M +1
       S <- 0
    Se M > 60 entao
       H <- H +1
       M <- 0
    Se H > 24 entao
       H <- 0
    FimSe
    FimSe
    FimSe
    FimSe
  Ate h = 1

fimalgoritmo

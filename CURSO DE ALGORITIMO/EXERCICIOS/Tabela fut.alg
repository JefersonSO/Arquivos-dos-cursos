algoritmo "Tabela"

var
  times: Caractere
  vet: vetor[1..3] de Caractere
  l, c: Inteiro
inicio
    Escreval("-----------------")
    Para c <- 1 ate 3 faca
       Escreval("Quais os times: ")
       Leia(vet[c])

    FimPara

    LimpaTela
       Escreval(" TABELA ")
       Escreval("--------------")
       Para c <- 1 ate 3 faca
           Para l <- 1 ate 3 faca
            Se c <> l entao
              Escreval(vet[c]:5, " X ", vet[l]:5 )
            FimSe
           FimPara
       Escreval("--------------")
       FimPara
     
fimalgoritmo


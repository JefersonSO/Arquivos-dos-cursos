algoritmo "OrdenadorDeVetor"
// Função :
// Autor :
// Data : 19/06/2022
// Seção de Declarações 
var
  vet: vetor[1..4] de Inteiro
  i, j, aux: inteiro
inicio
   Para i <- 1 ate 4 faca
      Escreva("Digite m valor: ")
      Leia(vet[i])
   FimPara
   
   Para i <- 1 ate 3 faca
     Se (vet[i] > vet[j]) entao
         aux <- vet[i]
         vet[i] <- vet[j]
         vet[j] <- aux
     FimSe
    FimPara
    
    Para i <- ate 4 faca
       Escreva("{", v[i], "}")
    FimPara
// Seção de Comandos 
fimalgoritmo

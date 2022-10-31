algoritmo "semnome"
// O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente,
//deve ser lido mais um número qualquer e inserir esse novo número na posição correta, ou seja,
//mantendo a ordem crescente do vetor.
var
  n:Vetor[1..11] de Inteiro
  n1,c,c2,aux: Inteiro
inicio
  Para c de 1 ate 10 faca
     n[c] <- randi(10)
  FimPara

  Para c de 1 ate 10 faca
     Para c2 de c+1 ate 11 faca
        Se n[c] > n[c2] entao
           aux <- n[c]
           n[c] <- n[c2]
           n[c2] <- aux
        FimSe
     FimPara
  FimPara
 Escreva(" mais um numero: ")
  Leia(n1)
  Para c de 1 ate 11 faca
       Se n[c] > n1  entao
          aux <- n1
          n1 <- n[c]
          n[c] <- aux

        FimSe
       Escreval(n[c])
  FimPara
fimalgoritmo

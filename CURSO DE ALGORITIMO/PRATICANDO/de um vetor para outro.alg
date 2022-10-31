algoritmo "semnome"
// Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X.
//Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após,
//imprimir o vetor M
var
  M,A: Vetor[1..10] de Inteiro
  c, X:Inteiro
  
inicio
  Para c de 1 ate 10 faca
    Escreva(" Digite um valor: ")
    Leia(A[c])
  FimPara
    Escreval(" Digite mais um valor ")
    Leia(X)
  Para c de 1 ate 10 faca
    M[c] <- (X * A[c])
    Escreval(M[c])
  FimPara

fimalgoritmo

algoritmo "semnome"
//  Um homem precisa atravessar um rio com um barco que possui capacidade de transportar apenas
//ele e mais uma de suas três cargas, que são: um cachorro, uma galinha e um saco de milho. O que o
//homem deve fazer para conseguir atravessar o rio sem perder as suas cargas?
var
  rio, A, B:Vetor[1..5] de caractere
  barco:Vetor[1..2] de Caractere
  c: Inteiro
  homem, cachorro, galinha, sacoMilho: caractere
inicio

  homem <- " HOMEM "
  cachorro <- " CACHORRO "
  galinha <- " GALINHA "
  sacoMilho <- " SACO DE MILHO "
 //estao no ponto A

   A[2] <- homem
   A[3] <- cachorro
   A[4] <- galinha
   A[5] <- sacoMilho
   Escreval(" estao no ponto A: ", A[1], A[2], A[3], A[4], A[5])
 //passos
   barco[1] <- homem
   barco[2] <- cachorro
   
   rio[1] <- barco[1]
   rio[2] <- barco[2]
   B[1] <- barco[2]

fimalgoritmo

algoritmo "semnome"
// Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se
//existem números repetidos no vetor VET e em que posições se encontram.
var
 N, V:Vetor[1..5] de  Inteiro
vezes, posi, c, c2 : Inteiro
inicio
posi <- 0
vezes <- 0
Para c de 1 ate 5 faca
     N[c] <- Randi(5)
     Escreval([c])
FimPara
Escreval(" Posição: ")
   Para c de 1 ate 4 faca
     Para c2 de c+1 ate 5 faca
      posi <- 0
      Se N[c2] = N[c] entao
      
        vezes <- vezes + 1
        posi <- posi + c2
        Escreval("-", posi)
      FimSe


   FimPara

fimPara
Escreval("------------------------")
Escreval(" Veszes que se repetiu: ")

Escreval("x", vezes)

fimalgoritmo

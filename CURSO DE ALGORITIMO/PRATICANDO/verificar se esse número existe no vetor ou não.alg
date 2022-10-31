algoritmo "semnome"
// Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um número
//qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve gerar um novo
//vetor sem esse número. (Considere que não haverão números repetidos no vetor).
var
  N:Vetor[1..6] de Inteiro
  aux, c, c2, mais_1n: Inteiro
Inicio
  Para c de 1 ate 5 faca
     Leia(N[c])

  FimPara
  Escreva("---------------------")
  Leia(mais_1n)

  Para c de 1 ate 5 faca
     Se N[c] = mais_1n entao

       aux <- N[c]
       N[c] <- N[5]
       N[6] <- aux

       Para c de 1 ate 4 faca
        Escreval(N[c])
       FimPara
     FimSe

  FimPara

fimalgoritmo

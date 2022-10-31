algoritmo " maior e menor valor e a posiçâo"
// Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir o valor do
// maior elemento de Q e a respectiva posição que ele ocupa no vetor.
var
  Q : Vetor[1..5] de Inteiro
  c, posicao, posicao2, menor, maior: Inteiro
inicio
  Para c de 1 ate 5 faca
     Escreval(" Digite um numero: ")
     Leia(Q[c])
     Se Q[c] < 0 entao
       Escreval (" Nao aceitamos numero negativo. digite novamentr: ")
       Leia(Q[c])

     FimSe
     Se Q [c] > maior entao
        maior <- Q[c]
        posicao <- c
     FimSe
  FimPara
     menor <- maior
     para c de 1 ate 5 faca
     Se Q[c] < menor entao

        menor <- Q[c]
        posicao2 <- c

     FimSe

     FimPara

  Escreval(" O maior numero digitado foi ", maior, " na posição ", posicao)
  Escreval(" O menor valor digitado foi ", menor, " naposião ", posicao2)
fimalgoritmo

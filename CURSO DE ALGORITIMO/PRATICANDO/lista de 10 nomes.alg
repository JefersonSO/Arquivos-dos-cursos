algoritmo "LIsta de 10 nomes"
// Função :
// Autor :
// Data : 18/07/2022
// Seção de Declarações 
var
  c: Inteiro
  pessoas: Vetor[1..10] de Caractere
  nome, resp:caractere
inicio
  c <- 0
  Para c <- 1 ate 10 faca

     Escreval(" Nome da ", c, " º pessoa: ")
     Leia(pessoas[c])
  FimPara
  Escreval(" Escreva um nome:")
  Leia(nome)
  resp <- " Nâo achei "
  Para c <- 1 ate 10 faca
      Se pessoas [c] =  nome  entao
         resp <- " Achei! "

      FimSe

  FimPara
  Escreval(resp)
fimalgoritmo

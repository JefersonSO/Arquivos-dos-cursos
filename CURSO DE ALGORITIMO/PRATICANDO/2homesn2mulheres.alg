algoritmo "2homesn2mulheres"
// Função :
// Autor :
// Data : 04/07/2022
// Seção de Declarações 
var
 h1, h2, m1, m2, hmv, hmn, mmn, mmv: Inteiro
inicio
  Escreval("Idade do 1º homem: ")
  Leia(h1)
  Escreval("Idade do 2º homem: ")
  Leia(h2)
  Escreval("Idade da 1º mulher: ")
  Leia(m1)
  Escreval("Idade da 2º mulher: ")
  Leia(m2)
  Se h1 > h2 entao
     hmv <- h1
     hmn <- h2
  senao
     hmv <- h2
     hmn <- h1
  FimSe
  Se m1 > m2 entao
     mmv <- m1
     mmn <- m2
  senao
     mmv <- m2
     mmn <- m1
  FimSe


 Escreval(" A soma das idades do homem mais velho com a mulher mais nova é ", mmv + mmn)
  Escreval(" E A soma das idades da mulher mais velha com o homem mais novo é ", hmn + mmv)

fimalgoritmo

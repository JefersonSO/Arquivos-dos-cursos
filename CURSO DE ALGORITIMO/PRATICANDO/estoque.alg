algoritmo "Estoque"
// Função :
// Autor :
// Data : 04/07/2022
// Seção de Declarações 
var
  Qmaxima,Qatual, Qmedia, Qminima: Real
inicio
  Escreval(" Qual a quantidade atual em estoque: ")
  Leia(Qatual)
  Escreval(" Qual a quantidade maxima: ")
  Leia(Qmaxima)
  Escreval(" Qual a quantidade minima: ")
  Leia(Qminima)
  Qmedia <- (Qmaxima + Qminima) / 2
  Se Qatual >= Qmedia entao
    Escreval(" Não efetuar a compra ")
  Senao
    Escreval("Efetuar a compra ")
  FimSe
  
fimalgoritmo

algoritmo "MaiorDaLista"
// Função : Calcular o maior numero de uma lista.
// Autor :   jeferson
// Data : 15/06/2022
// Seção de Declarações
var
 c, maior, numeros: Inteiro
inicio
 maior <- 0
 Escreval(" faça uma lista com 10 numeros: ")
 Escreval("---------------------------------")
 Para c <- 1 ate 10 faca
  Leia(numeros)
  Escreval("--")
  Se numeros > maior entao
     maior <- numeros
  FimSe
 FimPara
 Escreva(" o maior numero da lista è: ", maior)
fimalgoritmo

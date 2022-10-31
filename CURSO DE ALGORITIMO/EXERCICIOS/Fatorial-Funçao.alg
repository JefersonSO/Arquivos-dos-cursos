algoritmo "FatorialFunçao"
// Função :
// Autor :
// Data : 21/05/2022
// Seção de Declarações 
var
  N, R: Inteiro
Funcao Fatorial (V: Inteiro): Inteiro
Var
  cont, F: Inteiro
Inicio
   F <- 1
   Para cont <- 1 ate V faca

        F <- F * cont
   FimPara
   Retorne F
FimFuncao
inicio
  Escreval("digite um numero: ")
  leia(N)
  R <- Fatorial (N)
  Escreval("O fatorial de ", N, "è ", R)
// Seção de Comandos 
fimalgoritmo

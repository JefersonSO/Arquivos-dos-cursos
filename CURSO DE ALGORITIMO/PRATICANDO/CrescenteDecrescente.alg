algoritmo "crescente ou decrescente"
// Função : Ler 2 numeros e deduzir se estao em ordem crescente ou decrescente.
// Autor :
// Data : 15/06/2022
// Seção de Declarações 
var
   n: Vetor[1..2] de inteiro
   c: inteiro
inicio
   Para c <- 1 ate 2 faca
    Escreval("Digite o ", c, "º numero" )
    Leia(n[c])
   FimPara
   Se n[1] > n[2] entao
    Escreval("Os numeros estao em ordem decrescente.")
   Senao
    Escreval("Os numeors estao em ordem crescente.")
   FimSe
// Seção de Comandos 
fimalgoritmo

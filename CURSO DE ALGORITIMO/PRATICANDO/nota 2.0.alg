algoritmo "nota2.0"
// Função :
// Autor :
// Data : 06/07/2022
// Seção de Declarações 
var
 n1, n2: Real
 novoC : Caractere
inicio
Repita
 Enquanto (n1 <= 0) ou (n1 > 10)  faca
    Escreva(" primeira nota do aluno: ")
    Leia(n1)
    se (n1 <= 0) ou (n1 > 10) entao
      Escreva(" Invalido digite novamente ")
    FimSe
    LimpaTela
 FimEnquanto

 Enquanto (n2 <= 0) ou (n2 > 10)  faca
    Escreva(" segunda nota: ")
    Leia(n2)
    se (n2 < 0) ou (n2 > 10) entao
      Escreval(" Invalido digite novamente ")
    FimSe
    LimpaTela
 FimEnquanto
 Escreval (" A media do aluno é: ", (n1 + n2) / 2)
 n1 <- 0
 n2 <- 0
 
 Escreva(" Fazer um novo calculo? S/N ")
 Leia(novoC)
 LimpaTela
Ate novoC = "N"
fimalgoritmo

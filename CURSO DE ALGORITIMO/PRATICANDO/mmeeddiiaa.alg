algoritmo "media"
// Função :
// Autor :
// Data : 30/06/2022
// Seção de Declarações 
var
  n1, n2, media: Real
  
inicio
  Escreval("Primeira nota: ")
  Leia(n1)
  Escreval("Segunda nota: ")
  Leia(n2)
  media <- (n1 + n2) / 2
  Escreval("Media do Aluno: ", media)
  Se media >= 6 entao
   Escreval("Aluno aprovado")
  Senao
   Escreval("Aluno reprovado")
  FimSe
  
fimalgoritmo

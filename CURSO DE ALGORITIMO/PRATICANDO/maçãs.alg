algoritmo "semnome"
// Função : As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
//compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
//escreva o custo total da compra.
// Autor :
// Data : 30/06/2022
// Seção de Declarações 
var
  maca, qtdade, tot: Real
inicio
  maca <- 1.30
  Escreval("Quantas maçãs?: ")
  Leia(qtdade)
  Se qtdade >= 12 entao
     maca <- 1.00
     
  Fimse
  tot <- qtdade * maca
  Escreval("Total da compra: ", tot)
  
fimalgoritmo

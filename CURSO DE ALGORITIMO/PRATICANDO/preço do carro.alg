algoritmo "Preço do carro"
// Função :
// Autor :
// Data : 23/06/2022
// Seção de Declarações 
var
 vtot, pf, pd, im: Real
inicio
 Escreval("Qual o valor do carro de fabrica: ")
 Leia(pf)
 pd <- 28 / 100 * pf
 im <- 45 / 100 * pf
 vtot <- pf + pd + im
 Escreval(" Valor total é ", vtot)
 
fimalgoritmo

algoritmo "CodigoEPreçoDe15Produtos"
// Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever:
//- o maior preço lido
//- a média aritmética dos preços dos produtos
var
 codigo, preco, c, soma, maior: Inteiro
 media: Real
inicio
  maior <- Preco <- c <- soma <- 0
  media <- 0
 Repita
   c <- c + 1
   Escreva(" Codigo do produto: ")
   Leia(codigo)
   Escreva(" Preço do produto: ")
   Leia(preco)
   LimpaTela
   Se preco > maior entao
      maior <- preco
   FimSe
   soma <- soma + preco
 Ate c = 15
 media <- soma / c
 Escreval(" O maior preço lido è ", maior, " a media dos valores é ", media)
   
fimalgoritmo

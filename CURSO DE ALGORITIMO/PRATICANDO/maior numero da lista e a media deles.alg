algoritmo "maior numero da lista e a media deles 2.0"
// ) Faça um algoritmo para ler uma quantidade e a seguir ler esta quantidade de números. Depois de
//ler todos os números o algoritmo deve apresentar na tela o maior dos números lidos e a média dos
//números lidos.
var
 media :real
 soma, maior, n, c: Inteiro
inicio
 c <- maior <- soma <- media <- 0
 Repita
  c <- c + 1
  n <- randi(10))
  soma <- soma + n
  Escreval(n)
  Se n > maior entao
    maior <- n)

  FimSe
 Ate c = 10
  media <- soma / c
  Escreva(" o maior numero é: ", maior, " e a mèdia è ", media )
    
fimalgoritmo

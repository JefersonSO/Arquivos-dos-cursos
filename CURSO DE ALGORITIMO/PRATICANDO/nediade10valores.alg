algoritmo "media entre 10 valores"
// Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

Var
 n, soma, c: Real
inicio
soma <- 0
c<- 0
 Repita
  Escreval(" Digite um numero: ")
  Leia(n)
  c <- c + 1
  soma <- soma + n
 Ate c = 10
 Escreval(" A media aritimetica è : ", soma / 10)
fimalgoritmo

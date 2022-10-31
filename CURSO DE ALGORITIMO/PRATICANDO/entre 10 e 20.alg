algoritmo "entre10 e 20"
// Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (inlcuindo os
//valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.
var
 n, c, Ent1020, f1020: Inteiro
inicio
Ent1020 <- 0
f1020 <- 0
c <- 0
 Repita
  Escreval(" Digite um numero: ")
  Leia(n)
  c <- c + 1
  Se (n >= 10) e (n <= 20)entao
    Ent1020 <- Ent1020 + 1
  Senao
    f1020 <- f1020 + 1
  FimSe
 Ate c = 10
 Escreval(" Numeros entre 10 e 20: ", Ent1020, " Numeros fora: ", f1020)
fimalgoritmo

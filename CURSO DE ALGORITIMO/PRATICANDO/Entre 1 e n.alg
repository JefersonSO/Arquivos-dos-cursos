algoritmo "Valores entre 1  n"
// Função :Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere
// que o N será sempre maior que ZERO.
var
 n, um, entr: Inteiro
inicio
Repita
 Escreval(" Digite um numero: ")
 Leia(n)
  LimpaTela
 Se n < 0 entao
    Escreval("Digite um valor maior que 0")

 FimSe

Ate n > 0
 Escreval(" Valores entre 1 e ", n)
 Repita
  n <- n - 1

 Escreval(n)
 Ate n = 2
fimalgoritmo

algoritmo "nao podeZero2"
// FEscreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido
//um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado
//da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPITA).
Var
  va1, va2: Real
inicio
  Escreva(" Digite um valor: ")
  Leia(va1)
  Enquanto va2 = 0 faca
  Escreva(" Digite outro valor que nao seja zero: ")
  Leia(va2)
  LimpaTela
  se va2 = 0 entao
    Escreval(" Valor invalido ")
  FimSe
  FimEnquanto
  Escreval(va1, " dividido por ", va2, " è ",  va1 / va2)
fimalgoritmo

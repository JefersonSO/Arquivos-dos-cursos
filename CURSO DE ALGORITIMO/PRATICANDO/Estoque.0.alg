algoritmo " Estoque"
// Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo
//que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o
//valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das
//mercadorias.
var
 c, soma, media, Estoque, valorProduto: Real
inicio
  c <- soma <- media  <- 0
  Escreval(" Quantos produtos em estoque?: ")
  Leia(estoque)
  Repita
    c <- c + 1
    Escreval(" Preço do produto n ", c, "º: " )
    Leia(valorProduto)
    soma <- soma + valorProduto
  Ate c = estoque
  media <- soma / estoque
  Escreva(" valor total em estoque ", soma, "média de valor das mercadorias ", media)
fimalgoritmo

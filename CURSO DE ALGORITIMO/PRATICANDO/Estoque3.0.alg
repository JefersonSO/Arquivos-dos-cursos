algoritmo " Estoque"
// O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque.
//Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS
//MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das
//mercadorias em estoque.
var
 SouN :Caractere
 c, soma, media, Estoque, valorProduto: Real
inicio
  c <-  soma <- estoque <- media  <- 0


  Repita
    c <- c + 1
    Escreval(" Preço do produto n ", c, "º: " )
    Leia(valorProduto)
    LimpaTela
    soma <- soma + valorProduto
    estoque <- estoque + 1
    Escreval(" MAIS MERCADORIAS (S/N)? ")
    Leia(SouN)
  Ate SouN = "N"
    media <- soma / estoque
  Escreva(" valor total em estoque ", soma, " média de valor das mercadorias ", media)
fimalgoritmo

algoritmo "Frutaria"
  ///Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
//ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
//morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
var
   maca, morango,total, pmo, pma, dezporcento: Real
inicio
    Escreval(" morangos kg: ")
    leia(morango)
    Escreval(" maçãs kg: ")
    Leia(maca)
    Se (morango <= 5) e (maca <= 5) entao
      pmo <- 2.50
      pma <- 1.80
    senao
      se (morango > 5) e (maca > 5 ) entao
         pmo <- 2.20
         pma <- 1.50
      senao
      FimSe
    FimSe
    total <- ( pmo * morango) + (pma * maca)
    dezporcento <- 10 / 100 * total
    Se (morango + maca > 8 ) ou (total > 25) entao

        total <- total - dezporcento
         Escreval(" O total é ", total)
    FimSe

fimalgoritmo

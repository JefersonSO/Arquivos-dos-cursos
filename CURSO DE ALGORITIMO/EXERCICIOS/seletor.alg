algoritmo "Seletor de pessoas"
var
    sexo, Q: Caractere
  totm,toth, idade, esc: Inteiro

inicio
      toth <- 0
      toth <- 0
Repita
      LimpaTela
      Escreval("======================")
      Escreval("  Seletor de pessoas  ")
      Escreval("======================")
      Escreva(" Sexo F/M: ")
      Leia(sexo)
      Escreva(" Idade ")
      Leia(idade)
      Escreva(" Cor do cabelo: ")
      Escreval("----------------------")
      Escreval(" [1] Preto ")
      Escreval(" [2] Castanho ")
      Escreval(" [3] Loiro ")
      Escreval(" [4] Riuvo ")
      Leia(esc)
      Escreva(" Quer continuar? : S/N ")
      Leia (Q)
         Se (sexo = "M") e (idade >= 18) e (esc = 2) entao
            toth <- toth + 1
         FimSe
         Se (sexo = "f") e (idade >= 25) e (idade <= 30) e (esc = 3) entao
            totm <- totm +1
         FimSe
 Ate Q = "n"
 Escreval("---------------------------------------------------------------")
 Escreval("Total de homens com mais de 18 anos e com cabelo castanho ", toth)
 Escreval("total de mulheres entre 25 e 30 anos e com cabelo loiro ", totm)
fimalgoritmo

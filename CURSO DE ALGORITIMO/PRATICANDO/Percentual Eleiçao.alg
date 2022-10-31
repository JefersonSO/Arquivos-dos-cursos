algoritmo "PercentualEleiçao"
// Função :Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
//  brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
//  de eleitores
// Autor :
// Data : 23/06/2022
// Seção de Declarações 
var
  eleitores, N, B, V, PN, PB, PV: Real
inicio
  Escreval("Total de eleitores: ")
  Leia(eleitores)
  Escreval("Total de votos nulo: ")
  Leia(N)
  Escreval("Total de votos em Branco: ")
  Leia(B)
  Escreval("Total de votos validos: ")
  Leia(V)
  PN <- N * 100 / eleitores
  PB <- B * 100 / eleitores
  PV <- V * 100 / eleitores
  
  LimpaTela
  Escreval("--------------------------")
  Escreval(" TOTAL DE VOTANTES ", eleitores)
  Escreval("--------------------------")
  Escreval(" ", PN, " % de votos NULO ")
  Escreval("--------------------------" )
  Escreval(" ", PB, " % de votos em BRANCO ")
  Escreval("--------------------------")
  Escreval(" ", PV, " % de votos VALIDOS ")
fimalgoritmo

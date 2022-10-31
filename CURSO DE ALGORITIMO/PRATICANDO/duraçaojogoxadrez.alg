algoritmo "Duraçao do jogo xadrez"
// Função :
// Autor :
// Data : 30/06/2022
// Seção de Declarações 
var
  in, fim, horas: Inteiro
inicio
  Escreval(" Inicio da partida: ")
  Leia(in)
  Escreval(" Fim da partida: ")
  Leia(fim)
  Se in > fim entao
    horas <-  in - fim
  Senao
    horas <- fim - in
  FimSe
  Escreval(" A partida durou ", horas, " horas ")
fimalgoritmo

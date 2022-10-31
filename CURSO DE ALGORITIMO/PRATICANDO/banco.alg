algoritmo "banco"
// Função :
// Autor :
// Data : 04/07/2022
// Seção de Declarações 
var
  nconta, saldo, saldoat, debto, credito: Real
inicio
  Escreval(" numero da conta: ")
  Leia(nconta)
  Escreval(" Saldo: ")
  Leia(saldo)
  Escreval(" Debto ")
  Leia(debto)
  Escreval(" Credito ")
  Leia(credito)
  saldoat <- (saldo - debto) + credito
  Escreval(" Saldo atual é ", saldoat)
  Se saldoat > 0 entao
    Escreval(" SALDO POSITIVO! ")
  Senao
    Escreval(" Saldo Negativo ")
  FimSe
fimalgoritmo

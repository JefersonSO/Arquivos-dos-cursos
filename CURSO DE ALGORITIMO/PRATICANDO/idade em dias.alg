algoritmo "idadeEmDias"
// Função :
// Autor :
// Data : 22/06/2022
// Seção de Declarações 
var
  idade, ano, mes, dia: Inteiro
inicio
   Escreval("Qual a sua data de nascimento?")
   Escreva("Dia: ")
   Leia(dia)
   Escreva("Mês: ")
   Leia(mes)
   Escreva("Ano: ")
   Leia(ano)
   ano <- ano * 365
   mes <- mes * 30
   idade <-ano + mes + dia
   Escreva("Exatos ", idade, " dias.")
   
fimalgoritmo

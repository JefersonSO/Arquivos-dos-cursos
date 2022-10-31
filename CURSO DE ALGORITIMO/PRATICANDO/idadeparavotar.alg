algoritmo "de maior"
// Função :
// Autor :
// Data : 30/06/2022
// Seção de Declarações 
var
  ano_atual, ano_nascimento, idade: Inteiro
inicio
  Escreval("Ano Atual: ")
  Leia(ano_atual)
  Escreval("Ano de nascimento: ")
  Leia(ano_nascimento)
  idade <- ano_atual - ano_nascimento
  Se idade >= 16 entao
    Escreval(" Voce tem ", idade, " anos, ja pode votar!")
  Senao
    Escreval(" Voce tem ", idade, " anos, nao tem idade para votar. ")
  FimSe
fimalgoritmo

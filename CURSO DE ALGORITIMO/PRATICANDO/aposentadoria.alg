algoritmo "aposentadoria"
// Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para
//estar em condições, um dos seguintes requisitos deve ser satisfeito:
 //- Ter no mínimo 65 anos de idade.
 //- Ter trabalhado no mínimo 30 anos.
 //- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
//Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano

de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo
de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'
var
  codigo, dataN, anoatual, idade, anosNE, naE: Inteiro
  nome: Caractere
inicio
  Escreva(" Codigo do funcionario: ")
  Leia(codigo)
  Escreva(" Nome: ")
  Leia(nome)
  Escreva(" data de nascimento ")
  Leia(dataN)
  escreval(" Quando entrou na empresa: ")
  Leia(naE)
  anoatual <- 2022
  idade <- anoatual - dataN
  anosNE <- anoatual - naE
  Escreval(nome)
  Escreval(idade, "anos")
  Escreval("entrou na empresa  em ", naE, "(", anosNE,"anos ",")")
  Se (idade >= 60) e (anosNE >= 25) entao
     Escreval(" Requrer aposentadoria ")
  Senao
     se (idade >= 65) ou (anosNE >= 30) entao
     Escreval(" Requrer aposentadoria ")
     senao
     Escreval("Nao requrer ")
     FimSe
  FimSe
 
fimalgoritmo

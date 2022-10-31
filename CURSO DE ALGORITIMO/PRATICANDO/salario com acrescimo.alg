algoritmo "jornada de 40hr"
// Função :
// Autor :
// Data : 03/07/2022
// Seção de Declarações 
var
  salhr, salmes, hrmes, acrescimo, hrxt: Real
inicio
  Escreval(" salario p/ hr: ")
  leia(salhr)
  Escreval(" Horas trabalhadas no mes ")
  Leia(hrmes)
  salmes <- hrmes * salhr
  Se hrmes > 160 entao
    hrxt <- (hrmes - 160)
    acrescimo <- (salhr /100 * 50) * hrxt
    Escreval(" Salario total é ", salmes + acrescimo )
  Senao
    Escreval(" Salario total é ", salmes )
    
  FimSe
fimalgoritmo

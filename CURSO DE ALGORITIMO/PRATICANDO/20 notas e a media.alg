algoritmo "notasDe20AlunosE a media"
// Função :
// Autor :
// Data : 18/07/2022
// Seção de Declarações 
var
  notas: Vetor[1..20] de Real
  c: Inteiro
  acima, soma, mediaT: Real
inicio
  Para c de 1 ate 20 faca
   Escreval("notas ", c, "º aluno ")
   Leia(notas[c])
   soma <- soma + notas[c]
  fimPara
   mediaT <- soma / 20
   Para c de 1 ate 20 faca
      se notas[c] > mediaT entao
         acima <- acima + 1
      Fimse

    FimPara
   Escreval(" A media dessa turma é ", mediaT, " total de alunos acima da media ", acima)
fimalgoritmo

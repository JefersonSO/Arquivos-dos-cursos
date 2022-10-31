algoritmo "notas3.0"
//  Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e
//escrever a média aritmética dessas notas lidas.
var
 c, QAnaT, nota, Snotas: Inteiro
inicio
  Escreval(" Quantos alunos na turma? " )
  Leia(QAnaT)
  c <- 0
  Snotas <- 0
  Repita
    c <- c + 1
    Escreval(" nota do aluno ", c)
    Leia(nota)
    Snotas <- Snotas + nota

  Ate c = QAnaT
  Escreval(" A media dos alunos é: ", Snotas / QAnaT)
fimalgoritmo


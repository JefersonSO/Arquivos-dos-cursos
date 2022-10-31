algoritmo "ListagemDeAlunos"
// Função :
// Autor :
// Data : 18/06/2022
// Seção de Declarações 
var
  Aluno: Vetor[1..4] de Inteiro
  Nome: Vetor[1..4] de Caractere
  N1, N2: Vetor[1..4] de Inteiro
  media : Vetor[1..4] de Real
  mt: Real
  c, totp: Inteiro
inicio
  mt <- 0
  totp <- 0
  Para c <- 1 ate 4 faca
    Escreval("Aluno ", c)
    Escreval("-----------")
    Escreva("Nome: ")
    Leia(Nome[c])
    Escreva("Primeira nota: ")
    Leia(N1[c])
    Escreva("Segunda nota: ")
    Leia(N2[c])
    Escreval("-----------")
    media[c] <- (N1[c] + N2[c]) / 2
    mt <- mt + media[c] / 4
  FimPara
  LimpaTela
  Escreval("LISTAGEM DE ALUNOS ")
  Escreval("-------------------")
  Para c <- 1 ate 4 faca
    Escreval(Nome[c]:12, media[c]:4:1)
     Se media[c] >= mt entao
       totp <- totp + 1
     FimSe
  FimPara

  Escreval("Ao todo temos ", totp, " alunos acima da media da turma que é: ", mt)
  Escreva(mt)
fimalgoritmo

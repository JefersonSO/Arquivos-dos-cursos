algoritmo "Matriz de 3º ordem"
// Função :
// Autor :
// Data : 24/07/2022
// Seção de Declarações 
var
  mat: Vetor[1..3, 1..3] de Inteiro
  i, j:  inteiro
inicio
   Para i de 1 ate 3 faca
     Para j de 1 ate 3 faca
        Se i = j entao
           mat[i,j] <- 1
        Senao
           mat[i,j] <- 0
        FimSE
     FimPara
   FimPara
   
   Para i de 1 ate 3 faca
       Para j de 1 ate 3 faca
         Escreva(mat[i,j])
       fimPara
       Escreval()
   FimPara
fimalgoritmo

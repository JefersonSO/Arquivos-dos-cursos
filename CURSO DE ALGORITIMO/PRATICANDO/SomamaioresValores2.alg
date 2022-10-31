algoritmo "SomamaioresValores"
// Função :
// Autor :
// Data : 04/07/2022
// Seção de Declarações 
var
 v1, v2, v3, maior, menor: Inteiro
inicio
   Escreval(" Valor 1: ")
   Leia(v1)
   Escreval(" Valor 2: ")
   Leia(v2)
   Escreval(" Valor 3: ")
   Leia(v3)
      Se (v1 < v2) e (v1 < v3)  entao
        menor <- v1
      Senao
        se (v2 < v1) e (v2 < v3) entao
          menor <- v2
        senao
          menor <- v3
        FimSe
      FimSe
       Escreval(" A soma dos maiores valores è ", v1 + v2 +v3 - menor )
fimalgoritmo

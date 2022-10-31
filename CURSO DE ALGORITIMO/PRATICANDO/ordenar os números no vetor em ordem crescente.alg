algoritmo "vetor"
// Faça um algoritmo para ler 10 números e armazenar em um vetor. Após isto, o algoritmo deve
//ordenar os números no vetor em ordem crescente. Escrever o vetor ordenado.
var
 n: Vetor[1..10] de Inteiro
 aux,  c2, c:Inteiro
inicio
 Para c de 1 ate 10 faca
   n[c] <- randi(10)
 FimPara
 Para c de 1 ate 10 faca
   Para c2 de c+1 ate 10 faca
      Se n[c] > n[c2] entao
         aux <- n[c]
         n[c] <- n[c2]
         n[c2] <- aux


      FimSe

   FimPara
   Escreval(n[c])
 FimPara
fimalgoritmo

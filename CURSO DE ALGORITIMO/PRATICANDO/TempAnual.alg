algoritmo "Temperatura aanual"
// ) Faça um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano.
//Calcular e escrever:
//a) Menor temperatura do ano
//b) Maior temperatura do ano
//c) Temperatura média anual
//d) O número de dias no ano em que a temperatura foi inferior a média anual
var
  T:vetor[1..365] de Real
  c:Inteiro
  DiaIf ,maior, media, soma, menor: Real
inicio
  soma <- 0
  menor <- 42
  Para c de 1 ate 365 faca

     Enquanto T[c] < 17 faca
       T[c] <- randi(42)
     FimEnquanto
     soma <- soma + T[c]
     media <- soma / 365
     Se T[c] < menor entao
      menor <- T[c]
     FimSe

     Se T[c] > maior entao
        maior <- T[c]
     FimSe
     Se T[c] < media entao
        DiaIf <- DiaIf +1
     FimSe
  FimPara
  Escreval(" Menor temperatura do ano: ", menor,"º" )
  Escreval(" Maior temperatura do ano: ", maior,"º")
  Escreval(" Temperatura média anual: ", media:2,"º")
  Escreval(" O número de dias no ano em que a temperatura foi inferior a média anual: ", DiaIf)
fimalgoritmo

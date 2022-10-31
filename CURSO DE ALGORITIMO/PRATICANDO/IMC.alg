algoritmo "semnome"
var
   M, A, IMC: Real
inicio
      Escreva ("Massa (Kg): ")
      Leia (M)
      Escreva("Altura (m): ")
      Leia(A)
      IMC <- M / (A * A)
      Escreval (IMC:5:2)
      se (IMC >= 18.5) e (IMC < 25) entao
         Escreva(" Parabens voce esta no seu peso ideal")
      senao
           Escreva ("Voce nao esta na faixa de peso ideal")
      FimSe
fimalgoritmo

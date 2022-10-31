algoritmo "Fatorial"
var
   N, cont, fat: Inteiro
   resp: caractere

inicio
Repita
   Escreva("Fatorial de qiual numero? : ")
   Leia(N)
   fat <- 1
   cont <- n
   Repita
      Escreva (cont, " x "  )
      fat <- fat * cont
      cont <- cont - 1

   Ate cont < 1
   Escreval("o fatorial de ", N, "é: ", fat)
   Escreva("Quer continua: S/N")
   Leia(resp)
   LimpaTela
Ate resp = "N"
fimalgoritmo

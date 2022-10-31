algoritmo "semnome"
var
   cont, esc: Inteiro
inicio
Repita
   Escreval("======================")
   Escreval("        Menu          ")
   Escreval("======================")
   Escreval(" [1] De 10 a 1")
   Escreval(" [2] De 1 a 10")
   Escreval(" [3] Sair")

   Leia(esc)
   Escreval("======================")
   cont <- 1
   Escolha(esc)
       caso 1
           repita
             Escreval(cont," ..")
             cont <- cont + 1
           Ate cont = 11
       caso 2
           cont <- 10
           repita
             Escreval(cont," ..")
             cont <- cont - 1
           Ate cont < 1
    FimEscolha
    Escreval("======================")
Ate esc = 3
            Escreval("saindo..")
// Seção de Comandos
fimalgoritmo


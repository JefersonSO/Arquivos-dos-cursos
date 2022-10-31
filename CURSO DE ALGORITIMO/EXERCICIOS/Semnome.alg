algoritmo "semnome"

Var
   ini, fim, cont: Inteiro
inicio
      Escreval("----------------------")
      Escreval(" Contador inteligente ")
      Escreval("----------------------")
      Escreval(" Inicio ")
      Leia(ini)
      Escreval(" Fim ")
      Leia(fim)
      Se fim > ini entao
         cont <- ini
         Enquanto cont <= fim faca
            Escreva(cont, "...")
            cont <- cont +1
         FimEnquanto
      senao
           cont <- fim
           Enquanto cont >= fim faca
              Escreva(cont, "...")
              cont <- cont - 1
           FimEnquanto
      FimSe
      

// Seção de Comandos 
fimalgoritmo

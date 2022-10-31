algoritmo "SoComC"

var
  nome: Caractere
  ScC: Vetor [1..10] de caractere
  tot, C: Inteiro

inicio
   tot <- 0
   Para C <- 1 ate 10 faca
     Escreva(" Nome: ")
     Leia(nome)
     se (copia(maiusc(nome), 1, 1) = "C") entao
        tot <- tot +1
        ScC[tot] <- nome
     FimSe
   FimPara
   LimpaTela
   Escreval("Listagem final")
   Para C <- 1 ate tot faca
        Escreval(ScC[C])
   FimPara
   
fimalgoritmo

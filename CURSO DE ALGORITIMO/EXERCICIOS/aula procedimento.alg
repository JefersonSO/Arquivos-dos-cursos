algoritmo "DetectorPesado"

var
   I: Inteiro
   N, Pesado: caractere
   P, Mai: Real
Procedimento Topo ()
inicio
   LimpaTela
   Escreval("----------------------------------")
   Escreval(" D E T E C T O R  DE  P E S A D O ")
   Escreval(" O maior peso ate agora: ", Mai, "kG")
   Escreval("----------------------------------")
FimProcedimento
inicio
   Para I <- 1 ate 5 faca
        Escreval("Digite seu nome: ")
        Leia(N)
        Escreval("Digite o peso de ", N, ": ")
        Leia(P)
        Se (P > Mai) entao
           Mai <- P
           Pesado <- N
        FimSe
        Topo
    FimPara
    Topo
fimalgoritmo

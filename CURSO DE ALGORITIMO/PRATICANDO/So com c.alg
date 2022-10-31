algoritmo "SoComC"

var
  nome: Caractere
  nomc: Vetor[1..10] de Caractere
  c, tot: Inteiro
inicio
  tot <- 0
  Para c <- 1 ate 10 faca
    Escreval("Digite um nome: ")
    Leia(nome)
    Se (copia(maiusc(nome),1,1) = "c") entao
       tot <- tot +1
       nomc[tot]  <- nome
    FimSe
  FimPara
  LimpaTela
  Escreval("LISTAGEM FINAL")
  Para c <- 1  ate tot faca
    Escreval(nomc[c])
  FimPara
fimalgoritmo

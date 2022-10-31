algoritmo "Analisador de string"
// Função :
// Autor :
// Data : 21/05/2022
// Seção de Declarações 
var
  C: Inteiro
  N: Caractere
inicio
    Escreva("Digite um nome: ")
    Leia(N)
    Escreval("total de letras do seu nome: ", compr(N))
    Escreval("Seu nome em Maiusculas é ", Maiusc(N))
    Escreval ("Seu nome em minuscula é ", Minusc(N))
    Escreval("A primeira letra do seu nome é ", Copia(N,1,1))
    Escreval("A ultima letra do seu nome é ",Copia(Maiusc(N), Compr(N), 1))
    Escreval("A letra A esta na posiçao ", Pos("A",Maiusc (N)))
    Escreval("O codigo da letra A é ", Asc("A"))
    Escreval("A letra do codigo 65 è ", Carac(65))
    Para C <- Compr(N) Ate 1 passo -1  Faca
         Escreva(Copia(Maiusc(N), C, 1))
    FimPara
fimalgoritmo

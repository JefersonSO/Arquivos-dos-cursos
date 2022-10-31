algoritmo "Coleta de dados dos abitantes"
//A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmos
//para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:
//a) Média de salário da população
//b) Média do número de filhos
//c) Maior salário dos habitantes
//d) Percentual de pessoas com salário menor que R$ 150,00
//Obs.: O final da leituras dos dados se dará com a entrada de um “salário negativo”.
var
  nAb, c, filhos: Inteiro
  salario, somaS, somaF, mediaS, mediaF, maiorS, menor150, perc: Real
inicio
  c <- 0
  menor150 <- 0
  Escreva(" Numero de abitantes " )
  Leia(nAb)

     Repita
       c <- c + 1
       Escreval(" Salario do ", c, " abitante: ")
       Leia(salario)
       somaS <- somaS + salario
       Se salario > maiorS entao
          maiorS <- salario
       FimSe
       Se salario < 150 entao
          menor150 <- menor150 + 1
       FimSe
       Escreval(" Quantidade de filhos: ")
       Leia(filhos)
       somaF <- somaF + filhos
     Ate c = nAb

  mediaS <- somaS / nAb
  mediaF <- somaF / nAb
  perc <- menor150 / 100 * nAb
  Escreval(" Média de salário da população R$:", mediaS:2)
  Escreval(" Média do número de filhos: ", mediaF)
  Escreval(" Maior salário dos habitantes R$:", maiorS)
  Escreval(" Percentual de pessoas com salário menor que R$ 150,00: ", perc ,"%" )
  
fimalgoritmo

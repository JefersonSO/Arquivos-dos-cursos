algoritmo "salario carros usados"
// Função :Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
//mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
//efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
//vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
//vendedor.
// Autor :
// Data : 24/06/2022
// Seção de Declarações 
var
  salario, comissao, por5, carvend, totvend: Real
inicio
  Escreval("Quantos carros vendidos?: ")
  Leia(carvend)
  Escreval("Qual o salario? : ")
  Leia(salario)
  comissao <- 1000
  totvend <- carvend * comissao
  por5 <- 5 * 100 / totvend
   
  LimpaTela
  Escreval("------------------------------")
  Escreval(" Ao  todo foram ", carvend, " carros vendidos ")
  Escreval(" Salario fixo é ", salario)
  Escreval(" Por cada carro vendido voce recebe R$ 1000. total : ", totvend)
  Escreval(" Ao total seus gnahos sao: R$ ", salario + totvend + por5:4:2)
  
fimalgoritmo

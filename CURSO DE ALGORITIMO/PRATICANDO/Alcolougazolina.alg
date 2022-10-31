algoritmo "AlcolOuGazolina"
// Função :
// Autor :
// Data : 04/07/2022
// Seção de Declarações 
var
esc, alc, gaz, porcent, litros, precoA, totp, precoG: Real
inicio
  precoA <- 2.90
  precoG <- 3.30
  Escreval(" 1 - alcol 2- gazolina ")
  Leia(esc)
  
  Se esc = 1 entao
   Escreval(" Quantos litros? ")
   Leia(litros)
   se litros = 20 entao
      precoA <- (3/100) * precoA
      totp <- litros * precoA

   Senao
      se litros > 20 entao
         precoA <- (5/100) * precoA
         totp <- litros * precoA
      FimSe
   FimSe
  Senao
    Se esc = 2 entao
    Escreval(" Quantos litros? ")
    Leia(litros)
    se litros = 20 entao
      precoA <- (4/100) * precoA
      totp <- litros * precoA

    Senao
      se litros > 20 entao
         precoA <- (6/100) * precoA
         totp <- litros * precoA
      FimSe
   FimSe
  FimSe
  FimSe

  Escreval(" Total R$ ", totp)
fimalgoritmo

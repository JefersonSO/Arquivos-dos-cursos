algoritmo "TRI"
   var
    a, b, c: Inteiro
    mens, TI,  TEC, TEQ,NP : Caractere
   inicio
      TEQ <- ("Triângulo Equilátero")
      TI <- ("Triângulo Isósceles")
      TEC <- ( "Triângulo Escaleno")
      NP <- ("Não e possível formar um triângulo")
      Escreva("A")
      Leia(a)
      Escreva("B")
      Leia(b)
      Escreva("C")
      Leia(c)
         se (a < b+c) e (b <a+c) e (c <a+b) entao
           se (a=b) e (b=c) entao
             mens <- TEQ
           senao
            se (a=b) ou (b=c) ou (a=c) entao
             mens <- TI
            senao
             mens <- TEC
            fimse
           fimse
            senao
             mens <- NP
         fimse
         escreva("R:", mens )
fimalgoritmo

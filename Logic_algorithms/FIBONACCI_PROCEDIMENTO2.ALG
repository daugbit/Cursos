Algoritmo "semnome"
//  
//  

Var
  cont, C, T0, T1: Inteiro
  Procedimento ProximoFibonacci (var A, B: Inteiro)
  Var
  C: Inteiro
  Inicio
        C <- A + B
        Escreval (C)
        A <- B
        B <- C
  
  Fimprocedimento
  

Inicio
      T0 <- 0
      T1 <- 1
      Escreval ("Quantos números Fibonacci você quer ver? ")
      Leia (C)
      Escreval (T0)
      Escreval (T1)
      Para cont de 1 ate (C-2) faca
      ProximoFibonacci (T0, T1)
      Fimpara



Fimalgoritmo
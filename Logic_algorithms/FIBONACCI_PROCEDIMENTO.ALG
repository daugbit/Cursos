Algoritmo "fibonacci_1"


Var
N1, N2, N3, R, C: inteiro

Procedimento ProximoFibonacci (var A, B: Inteiro)
var
C: Inteiro
Inicio
      C <- A + B
      escreva (C)
      A <- B
      B <- C
Fimprocedimento

Inicio
      N1 <- 0
      N2 <- 1
      escreva (N1, N2)
      para C de 1 ate (20) faca
      ProximoFibonacci(N1,N2)
      fimpara
      
Fimalgoritmo
Algoritmo "fibonacci_1"


Var
N1, N2, N3, R, C: inteiro

Inicio
      escreva ("Quanto n�meros da sequ�ncia de Fibonacci voc� quer ver? ")
      leia (R)
      N1 <- 0
      N2 <- 1
      escreva (N1, N2)
      para C de 1 ate (R-2) faca
           N3 <- N1 + N2
           escreva (N3)
           N1 <- N2
           N2 <- N3
      fimpara


Fimalgoritmo
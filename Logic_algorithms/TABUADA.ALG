Algoritmo "tabuada"



Var
   n, r: inteiro
   c: caractere

Inicio

   repita
      escreva ("Informe o n�mero da tabuada: ")
      leia (r)
      n <- 1
      repita
         escreval (r, " x ", n, " = ", r*n)
         n <- n + 1
      ate (n > 10)
      escreva ("Deseja informar outro n�mero? [s/n]  ")
      leia (c)
      limpatela
   ate (c = "n")


Fimalgoritmo
Algoritmo "fatorial"



Var
   n, cont, f: inteiro
   
Inicio

      escreva ("Informe o n�mero: ")
      leia (n)
      cont <- n
      f <- 1
      repita
            f <- f * cont
            cont <- cont -1
      ate (cont < 1)
      escreva ("O fatorial de ", n, " � ", f)



Fimalgoritmo
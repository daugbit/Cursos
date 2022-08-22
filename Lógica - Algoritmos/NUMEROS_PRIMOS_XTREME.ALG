Algoritmo "numeros_primos_Xtreme"



Var
   cont1, cont2, NI, ContDiv, primo: inteiro

Inicio
      escreval ("--------------------------------------------")
      escreval ("   ANALISADOR DE NÚMEROS PRIMOS  ")
      escreval ("  Digite um número e descubra todos")
      escreval ("     os números primos até ele")
      escreval ("--------------------------------------------")

      cont2 <- 1
      primo <- 1
      escreva ("Informe o número: ")
      leia (NI)
      escreval ("--------------------------------------------")
      escreval ("Estes são os números primos até ", NI, ":")
      escreval (" ")
      
      repita
      cont1 <- 1
      ContDiv <- 0
            repita
                  se (primo % cont1 = 0) entao
                     ContDiv <- ContDiv + 1
                  fimse
                  cont1 <- cont1 + 1
            ate (cont1 > primo)
            se (ContDiv <= 2) entao
               escreval (primo)
            fimse
            primo <- primo + 1
            cont2 <- cont2 +1
      ate (cont2 > NI)


Fimalgoritmo
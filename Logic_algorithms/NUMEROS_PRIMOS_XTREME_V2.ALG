Algoritmo "numeros_primos_Xtreme"



Var
   cont1, NI, ContDiv, primo: inteiro


Inicio
   escreval ("--------------------------------------------")
   escreval ("   ANALISADOR DE N�MEROS PRIMOS  ")
   escreval ("  Digite um n�mero e descubra todos")
   escreval ("     os n�meros primos at� ele")
   escreval ("--------------------------------------------")

   primo <- 9
   escreva ("Informe o n�mero: ")
   leia (NI)
   escreval ("--------------------------------------------")
   escreval ("Estes s�o os n�meros primos at� ", NI, ":")
   escreval (" ")

   se (primo > 7) entao
      escreval (" 2")
      escreval (" 3")
      escreval (" 5")
      escreval (" 7")
      repita
         cont1 <- 1
         ContDiv <- 0
         se (primo%3<>0) e (primo%5<>0) e (primo%7<>0) entao
            repita
               se (primo % cont1 = 0) entao
                  ContDiv <- ContDiv + 1
               fimse
               cont1 <- cont1 + 2
            ate (cont1 > primo)
            se (ContDiv <= 2) entao
               escreval (primo)
            fimse
         fimse
         primo <- primo + 2
      ate (primo > NI)
   senao
      escreval (" 2")
      escreval (" 3")
      escreval (" 5")
      escreval (" 7")
   fimse


Fimalgoritmo
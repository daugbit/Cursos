Algoritmo "numeros_primos"



Var
   cont, num, ContDiv: inteiro

Inicio
      escreval ("---------------------------------")
      escreval ("  ANALISADOR DE NÚMEROS PRIMOS  ")
      escreval ("Digite um número e deescubra se")
      escreval ("ele é primo e quais são os seus")
      escreval ("denominadores possíveis")
      escreval ("---------------------------------")

      cont <- 1
      ContDiv <- 0
      escreva ("Informe o número: ")
      leia (num)
      escreval ("---------------------------------")
      repita
            se (num % cont = 0) entao
               escreval ("Divisível por ", cont)
               ContDiv <- ContDiv + 1
            fimse
            cont <- cont + 1
      ate (cont > num)
      escreval ("---------------------------------")
      se (ContDiv > 2) entao
         escreva (num, " NÃO é número primo.")
      senao
           escreva (num, " É número primo.")
      fimse



Fimalgoritmo
Algoritmo "numeros_primos"



Var
   cont, num, ContDiv: inteiro

Inicio
      escreval ("---------------------------------")
      escreval ("  ANALISADOR DE N�MEROS PRIMOS  ")
      escreval ("Digite um n�mero e deescubra se")
      escreval ("ele � primo e quais s�o os seus")
      escreval ("denominadores poss�veis")
      escreval ("---------------------------------")

      cont <- 1
      ContDiv <- 0
      escreva ("Informe o n�mero: ")
      leia (num)
      escreval ("---------------------------------")
      repita
            se (num % cont = 0) entao
               escreval ("Divis�vel por ", cont)
               ContDiv <- ContDiv + 1
            fimse
            cont <- cont + 1
      ate (cont > num)
      escreval ("---------------------------------")
      se (ContDiv > 2) entao
         escreva (num, " N�O � n�mero primo.")
      senao
           escreva (num, " � n�mero primo.")
      fimse



Fimalgoritmo
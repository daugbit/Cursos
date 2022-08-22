Algoritmo "enquanto_faca_-_contador_inteligente"

Var
   I, F, cont: inteiro

Inicio
   escreva ("Início: ")
   leia (I)
   escreva ("Fim: ")
   leia (F)
   escreval ("CONTANDO......")
   se (I < F) entao
      enquanto (I <= F) faca
         escreva (I, "...  ")
         I <- I + 1
      fimenquanto
   senao
      enquanto (I >= F) faca
         escreva (I, "...  ")
         I <- I - 1
      fimenquanto
   fimse

Fimalgoritmo
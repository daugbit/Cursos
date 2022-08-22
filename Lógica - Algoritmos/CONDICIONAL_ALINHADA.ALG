Algoritmo "condicional_alinhada"
// cálculo de IMC

Var
p, a, IMC: real


Inicio
escreval ("---------------------------------------")
escreval ("CALCULADORA DE ÍNDICE DE MASSA CORPORAL")
escreval ("---------------------------------------")
escreva ("Informe o seu peso (kg): ")
leia (p)
escreva ("Informe a sua altura (m): ")
leia (a)
IMC <- (p/a^2)
escreval ("O seu IMC é: ", IMC:3:1)
escreva ("Você está ")
se (IMC < 17) entao
   escreval ("MUITO ABAIXO DO PESO IDEAL")
senao
     se (IMC >= 17) e (IMC < 18.5) entao
        escreval ("ABAIXO DO PESO IDEAL")
     senao
          se (IMC >= 18.5) e (IMC < 25) entao
             escreval ("com o PESO IDEAL")
          senao
               se (IMC >= 25) e (IMC < 30) entao
                  escreval ("com SOBREPESO")
               senao
                    se (IMC >=30 ) e (IMC < 35) entao
                       escreval ("com OBESIDADE")
                    senao
                         se (IMC >= 35) e (IMC < 40) entao
                            escreval ("com OBESIDADE SEVERA")
                         senao
                              escreval ("com OBESIDADE MÓRBIDA")
                         fimse
                    fimse
               fimse
          fimse
     fimse
fimse


Fimalgoritmo
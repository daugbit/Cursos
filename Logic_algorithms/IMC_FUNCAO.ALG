Algoritmo "semnome"


Var
   M, A, indice: Real
   situacao: caractere

Funcao imc(massa, altura: real): real
Inicio
   Retorne massa / altura^2
FimFuncao

Funcao enquadramento(IMC2: real): caractere
Inicio
   Se (IMC2 <= 17) entao
      Retorne "abaixo do seu peso ideal"
   Senao
      Se (IMC2 > 17) e (IMC2 <= 25) entao
         Retorne "no seu peso ideal"
      Senao
         Se (IMC2 > 25) e (IMC2 <= 30) entao
            Retorne "com sobrepeso"
         Senao
            Se (IMC2 > 30) e (IMC2 <= 35) entao
               Retorne "com obesidade nível I"
            Senao
               Se (IMC2 > 35) e (IMC2 <= 40) entao
                  Retorne "com obesidade nível II"
               Senao
                  Retorne "com obesidade mórbida"
               FimSe
            FimSe
         FimSe
      FimSe
   FimSe
FimFuncao

Inicio
   Escreva("Informe seu peso (kg): ")
   Leia(M)
   Escreva("Informe a sua altura (m): ")
   Leia(A)
   indice <- imc(M, A)
   situacao <- enquadramento(indice)

   Escreval("--------------------------------")
   Escreval("Seu IMC é ", indice:5:2)
   Escreval("Você está ", situacao, ".")
   Escreval("--------------------------------")


Fimalgoritmo
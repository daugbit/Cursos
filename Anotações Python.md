# Anotações Python

---

## MÓDULOS

Importação de módulos se dá a partir de `import <módulo>`  
Importação de uma função única com `from <módulo> import <função>`  

* `math`: operações matemáticas básicas (sqrt, sin, cos, tan, radians, etc.)

* `datetime`: datas e horas
	* `datetime.date.today().year`: retorna o ano atual (registro do computador em uso)

* `random`: números e ordens aleatórias
	* `random.randint(x, y)`: retorna um número aleatório entre x e y
	* `random.shuffle(lista)`: retorna uma ordem aleatória a partir de uma lista definida
	* `random.choice(lista)`: dentre os itens de uma lista, escolhe um deles aleatoriamente
	
* `time`: recursos de tempo
	* `time.sleep(x)`: software aguarda por x segundos para continuar rodando
	* `localtime`: retorna a hora local em segundos
	* `strftime`: converte uma data/horário específicados (como pelo **localtime**) para uma string estruturada:  
		```
		strftime("%a, %d %b %Y %H:%M:%S", localtime())
		```
	Verificar a especificação de cada argumento em https://docs.python.org/3.8/library/time.html#module-time  

* `pygame`: recursos para jogos e multimídia
	ex:	execução de um arquivo mp3 local
	```
	pygame.mixer.init()
	pygame.init()
	pygame.mixer.music.load('<nome_arquivo_musica>')
	pygame.mixer.music.play()
	pygame.event.wait()
	```
	
* `emoji`: retorna emojis
	* `emoji.demojize('<código do emoji>', language='alias')` Obs: entre as aspas pode conter texto  

* `operator.itemgetter`: pode ser utilizado para ordenar um dicionário - `ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)`  

* `sys.exit()`: encerra o programa imediatamente.  

* `urllib`: funções relacionadas a URLs, como verificar se um site está online, p.e.:  
```
import urllib.request
import urllib.error
try:
	urllib.request.urlopen(<url_site>)
except urllib.error.URLError:
	print(f'\033[31mO site {name} não está acessível no momento.\033[m')
else:
	print(f'\033[32mO site {name} está acessível no momento.\033[m')
```

* `json`: módulo para salvar informações geradas pelos códigos em arquivos externos (ver **manipulação de arquivos** abaixo).  

* `itertools`: módulo para trabalhar com objetos iteráveis.  
	* `count()`: utilizada para gerar índices para outros objetos, como listas. A função **count()** pode ser personalizada com os parâmetros *start* e *step*: `contador = count(start=10, step=2)`;  
	* `combinations(<lista>, n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, sem importar a ordem;  
	* `permutations(<lista>, n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, considerando a ordem;  
	* `product(<lista>, repeat=n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, considerando a ordem e combinações de um mesmo elemento;  

---

## MANIPULAÇÃO DE STRINGS

* `f'string formatada com {variável}'`: string formatada com o valor de uma string.  
* `r'raw \string'`: retorna a string ignorando o caractere de escape.  
* `\n`: quebra de linha
* `\t`: tabulação da linha
* `end=''`: faz com quer não haja quebra de linha ao final do **print** atual, podendo-se informar algum(ns) caracteres entre as aspas para serem exibidos nesse final.  
* `sep=''`: usado para especificar como  valores dentro de um **print** devem ser separados.  
* Espaçamentos e alinhamentos:  
  * `{<var>:x}`: insere o valor da variável dentro de x espaços (o que for maior que var ficará com espaçamento em branco)  
  * `{<var>:^x}`: idem, centralizado
  * `{<var>:-^x}`: idem, com traços no lugar (ou qualquer outro caractere). Ex.: `-----var-----`  
  * `{<var>:>x}`: alinhado à direita
  * `{<var>:<x}`: alinhado à esquerda
  * `<objeto>.center(x, '*')`: alinha o objeto ao centro num espaçamento **x**, preenchido com o caractere '*' (pode ser ocultado caso sejam espaços).  
  * `<objeto>.ljust(x, '*')`: alinha o objeto à esquerda num espaçamento **x**, preenchido com o caractere '*' (pode ser ocultado caso sejam espaços).  
  * `<objeto>.rjust(x, '*')`: alinha o objeto à direita num espaçamento **x**, preenchido com o caractere '*' (pode ser ocultado caso sejam espaços).  
* `<objeto>.startswith('str')`: retorna um valor booleano ao verificar se a string do objeto inicia com a string especificada 'str'.  
* `<objeto>.endswith('str')`: retorna um valor booleano ao verificar se a string do objeto termina com a string especificada 'str'.  
* `len(<objeto>)`: mostra o comprimento de uma string
* `<objeto>.count(<trecho>)`: conta quantos trechos informados há dentro do objeto
* `<objeto>.lower()`: transforma a string toda em minúsculo
* `<objeto>.upper()`: transforma a string toda em maiúsculo
* `<objeto>.capitalize()`: apenas a primeira letra da string em maiúsculo
* `<objeto>.title()`: primeira letra de cada palavra da string em maiúsculo
* `<objeto>.replace(<trecho>, <trecho>)`: troca um trecho de uma string
* `<objeto>.strip()`: remove os espaços do início e final da string
	* `<objeto>.(l/r)strip()`: remove os espaços do início/final da string
	* `<objeto>.strip('str')`: ao invés de remover espaços no início/final, vai remover os caracteres da string especificada (a ordem não importa).  
* `''.join(<objetolista>)`: transforma uma lista de objetos em uma string única
	* `'-'.join(<objetolista>)`: adiciona '-' (ou qualquer outro caractere) entre cada objeto na string
* `<objeto>.find(<trecho>)`: informa a localização de um trecho numa string
* `<objeto>.split()`: separa uma string em uma lista de palavras
* `<objeto>[x:y:z]`: x - primeira posição da string a ser exibida | y - posição posterior à última a ser exibida | z - passo  
* `x, y, z = y, z, x`: faz a troca dos valores contidos em cada varíval, conforme a posição do lado oposto da igualdade, sem precisar de variável de apoio.  

---

## CORES 

`\033[<style;text;background>m`  

      
-- | none | bold | light | italic | underl | blinck | black | red | green | yellow | blue | purple | cian | white
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
style | 0 | 1 | 2 | 3 | 4 | 5 | -- | -- | -- | -- | -- | -- | -- | --
text | -- | -- | -- | -- | -- | -- | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 |
back | -- | -- | -- | -- | -- | -- | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |

---

## LISTAS

* `range(x, y, z)`: cria uma série com valores entre **x** e **y**, pulando **z** valores
 * `list(range(x, y, z))`: converte a série de valores em uma lista
* `list(str)`: pode ser usado para separar uma string por caracteres: `> 's', 't', 'r'` 
* `<lista>.insert(<posição>, <dado a ser inserido>)`: insere um dado na posição especificada da lista
* `<lista>.append(<dado a ser inserido>)`: insere um dado na próxima posição em branco de uma lista
* `del <lista>[x]`: deleta permanentemente o item na posição x da lista. Os itens à direita serão todos movidos 1 posição à esquerda
* `var = <lista>.pop(x)`: passa o valor da posição x da lista para a variável, deletando o item da lista
* `<lista>.remove('valor')`: exclui um valor da lista em qualquer posição (pode-se usar também uma variável que contenha esse valor)
* `<lista>.sort()`: ordena a lista por ordem crescente (se numérica) ou alfabética (se string)
* `<lista>.sort(reverse=True)`: idem, mas ao contrário
* `sorted(<lista>)`: retorna a lista ordenada, mas sem alterar a lista original
* `<lista>.reverse()`: inverte a ordem da lista
* `<lista>.count('valor')`: conta quantos valores específicos há dentro da lista
* `<lista>.index(x, y)`: retorna a posição do valor x na lista, a partir da posição y (y pode ser ignorado para buscas a partir do início)
* `min(<lista>)`: retorna o menor valor da lista
* `max(<lista>)`: retorna o maior valor da lista
* `sum(<lista>)`: retorna a soma dos valores da lista  
  É possível criar uma lista com um lanço dentro da mesma. Ex.:  
  `squares = [value ** 2 for value in range(1, 11)]`  
  * `copia_lista = lista[:]`: copia a lista inteira (ou uma fatia, especificando o início e final) para uma segunda lista
    * `copia_lista = lista`: conecta as duas listas. Adicionando valores em uma delas, vai para a outra também  
* `if <lista>:`: teste que retorna se uma lista está vazia (`False`) ou se contém ao menos um registro (`True`)  
* `if <objeto> in <lista>:`: testa se o objeto está dentro de uma lista  
Para copiar uma lista (a) para outra (b), deve-se utilizar `b = a[:]`. Ao utilizar o comando `b = a`, é criada uma ligação entre ambas e o que for alterado em uma refletirá na outra.  

### Desempacotamento de listas

Podemos fazer a extração total ou parcial de valores contidos em listas para variáveis simples.  
```
lista = ['valor1', 'valor2', 'valor3', 'valor4', 'valor5']

#1 cada variável simples recebe um valor da lista
n1, n2, n3, n4, n5 = lista

#2 as duas primeiras variáveis recebem os primeiros valores da lista e o restante é incluído na lista2
n1, n2, *lista2 = lista

#3 as variáveis simples recebem os três últimos valores da lista e o restante (primeiros valores) é incluído na lista3
*lista3, n1, n2, n3 = lista

#4 as duas primeiras variáveis recebem os primeiros valores da lista e o restante é ignorado
n1, n2, *_ = lista
```

É possível ainda desempacotar uma lista ao passá-la como argumento de uma função. Por exemplo:
```
lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')

>>> 1-2-3-4-5
```
Caso o argumento **sep** não seja informado, por padrão o espaço será utilizado como separador.


---

## TUPLAS

Semelhantes às listas, mas não são alteráveis. Usa-se `()` ao invés de `[]`. Porém, pode-se sobreescrever a variável inteira.  
As mesmas funções/comandos das listas são aplicáveis às tuplas (exceto alterações de conteúdo da tupla).  
Tuplas podem ser compostas de tipos primitivos diferentes. Ex.: `pessoa = ('Douglas', 27, 'M', 90.5)`
Ex.:  
```
colors = ('black', 'white', 'yellow')
print(colors[1])
```
Retornaria: `white`  
  
---

## DICIONÁRIOS

Semelhantes às listas e às tuplas, mas são identificados por `{}` e os índices dos dados/valores não precisam ser numéricos.  
`<dicionario> = {'chave': valor, 'chave': 'str', ...}`  
Ex.: `dados = {'name': 'Douglas', 'age': 27, 'gender': male}`
* `<dicionário>.values()`: retorna os valores registrados dentro de cada chave.
* `<dicionário>. keys()`: retorna as as chaves existentes dentro do dicionário
* `<dicionário>.items()`: retorna chaves e valores do dicionário  
Exemplo de laço com dicionário:  
	```
	for i, j in dicionário.items():
		print(f'O {i} é {j}')
	
	>>> O valor é chave
	```
* `<lista>.append(<dicionário>.copy())`: copiar um dicionário para dentro de uma lista.  
* `del <dicionário>['<chave>']`: deleta a chave e o respectivo valor do dicionário.  
* `<dicionário>.get('key', x)`: retorna o valor da chave 'key' caso ela exista, ou x caso essa chave não exista.  
* `<dicionário>.setdefault('key', 'value')`: determina um valor padrão para a chave 'key', caso um valor não seja informado.  
* `<dicionário1>.update(<dicionário2>)`: concatena o dicionário 2 no dicionário 1 (o operador **+** não funciona para dicionários).  

---

## SETS (CONJUNTOS)

É uma variável que armazena uma série de valores. Também é identificada por **{}**, sendo que não há o par chave-valor (apenas valor), sem qualquer ordem definida.  
`var = {1, 2, 3, 4, 5}` ou `var = set()`
**os conjuntos NÃO aceitam valores duplicados**. Útil para remover valores duplicados de uma lista.

* `<set>.add(value)`: adição de um valor ao conjunto.  
* `<set>.discard(value)`: exclusão de um valor do conjunto.  
* `<set>.update(value)`: itera sobre o valor, adicionando cada caractere como um valor separado ({'v', 'a', 'l', 'u', 'e'}).  
* `s3 = s1 | s2`: a função **union (|)** é utilizada para unir dois conjuntos.  
* `s3 = s1 & s`: a função **intersection (&)** é utilizada para criar um conjunto que contenha os elementos que estejam presentes em ambos os outros conjuntos.  
* `s3 = s1 - s2`: a função **diference** retorna para a variável s3 o conjunto de valores que estão no conjunto da esquerda, mas não no da direita.  
* `s3 = s1 ^ s2`: a função **symetric_difference** retorna os valores dos dois conjuntos que NÃO estejam em ambos ao mesmo tempo.  

---

## LIST COMPREHENSIONS

Forma de iterar sobre uma lista/tupla através de apenas uma linha de comando.  

Em uma iteração de simples de 'cópia' de uma lista, por exemplo:
```
lista = [1, 2, 3, 4, 5]

lista2 = [var for var in lista]
print(lista2)

>>> [1, 2, 3, 4, 5]
```

É possível aninhar um **for** adicional para executar uma outra operação, como criar coordenadas, por exemplo:
```
var1 = [0, 1, 2,]

var2 = [[v1, v2] for v1 in var1 for v2 in range(3)]
print(var2)

>>> [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

```
ou para manipular os valores de tuplas/listas (no caso abaixo, inverter os valores e depois converter em dicionário):
```
tupla = (('chave1', 'valor1'), ('chave2', 'valor2'), ('chave3', 'valor3'))

var = [(x, y) for x, y in tupla]
var = dict(var)
print(var)

>>> {'valor1': 'chave1', 'valor2': 'chave2', 'valor3': 'chave3'}
```

Podemos filtrar os valores da lista utilizando **if** (inclusive mais de 1):
```
lista = list(range(20))

pares = [num for num in lista if num % 2 == 0]
print(pares)

>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```
```
lista = list(range(20))

pares = [num for num in lista if num % 2 == 0 if num % 5 != 0 if num % 4 != 0]
print(pares)

>>> [2, 6, 14, 18]
```

Para utilização de operadores ternários **if/else**:
```
lista = list(range(10))

nums = [v if v % 3 == 0 else 'dif' for v in lista]
print(nums)

>>> [0, 'dif', 'dif', 3, 'dif', 'dif', 6, 'dif', 'dif', 9]
```
aninhando mais de uma condição:
```
lista = list(range(10))

nums = [v if v % 3 == 0 and v < 9 else 'dif' for v in lista]
print(nums)

>>> [0, 'dif', 'dif', 3, 'dif', 'dif', 6, 'dif', 'dif', 'dif']
```

Também é possível tratar um valor da lista original e depois aplicar um filtro. No exemplo, caso o número seja diferente de 5 ele permanecerá o mesmo - mudando para 500 se for 5. Posteriormente aplicamos um filtro para apenas números ímpares:  
```
lista = list(range(10))

nums = [v if v != 5 else 500 for v in lista if v % 2 != 0]
print(nums)

>>> [1, 3, 500, 7, 9]
```

Pode-se aninhar laços de repetição juntamente com as condicionais, tomando-se o cuidado com a ordem desses componentes. No exmeplo abaixo, primeiramente definimos os dados que devem ser considerados (primeiro **if**), então quais dados devem ser gerados (expressões **for**) e depois quais desses valores devem de fato aparecer (segundo **if**):
```
matriz = [
    (x, y)
    if y != 2 else (x, y * 100)
    for x in range(1, 4)
    for y in range(1, 5)
    if x != 3
]
print(matriz)

>>> [(1, 1), (1, 200), (1, 3), (1, 4), (2, 1), (2, 200), (2, 3), (2, 4)]
```

Por fim, pode-se ainda iterar sobre uma string através do índice dela:
```
string = '012345678901234567890123456789'

new_string = [string[index:index + 10] for index in range(0, len(string), 10)]
print(new_string)

>>> ['0123456789', '0123456789', '0123456789']

newer_string = '.'.join([string[index:index + 10] for index in range(0, len(string), 10)])
print(newer_string)

>>> 0123456789.0123456789.0123456789
```

---

## DICTIONARY COMPREHENSION

Semelhante à list comprehenison, com as mesmas funções e comandos, mas com as particularidades de um dicionário - par chave-valor.
```
lista = [['valor1', 1], ['valor2', 2], ['valor3', 3]]

dicionario = {chave: valor for chave, valor in lista}
print(dicionario)

>>> {'valor1': 1, 'valor2': 2, 'valor3': 3}
```

É possível criar um dicionário ou um conjunto com a função **range**:
```
dicionario = {valor for valor in range(5)}
print(dicionario)

>>> {0, 1, 2, 3, 4}
```
```
dicionario = {f'chave{valor}': valor for valor in range(5)}
print(dicionario)

>>> {'chave0': 0, 'chave1': 1, 'chave2': 2, 'chave3': 3, 'chave4': 4}
```

---

## LAÇOS DE REPETIÇÃO

* `for <v> in <lista>`: passa cada item da **lista**, passa o valor da item para a **v** e executa os comandos dentro do laço  
  * `for <i>, <v> in enumerate(<lista>)`: puxa tanto o valor como o índice do item na lista
* `break`: interrempe o laço sem executar os comandos subsequentes que estão dentro do mesmo.  
  * Pode-se iniciar o laço com `while True`  
* `continue`: retorna imediatamente para o início do laço, realizando novamente o teste da condição.  

Pode-se utilizar **else** nos laços também. O bloco contido nele será executado apenas se a condição do laço for falsa.  
 
---

## GERADORES, ITERADORES E ITERÁVEIS

* Em Python, são iteráveis as strings, listas, dicionários e tuplas - números não são;  
* Quando utilizamos um laço **for**, ele transforma o nosso objeto em um **iterador**, para que possamos iterar sobre ele;  
	* Podemos transformar um objeto em um iterador manualmente, através da função `iter(<objeto>)`;  

Quando trabalhamos com objetos com muitas informações - como listas, por exemplo - podemos utilizar um **gerador**, o qual só retorna o valor que precisamos quando demandado, economizando consideravelmente a memória do computador. Para isso, podemos utilizar **yield** ou list comprehension:  
```
def generator():
    for i in range(1000):
        yield i
```
Na list comprehension, utiliza-se **()** ao invés de **[]**:
```
lista = (x for x in range(1000))
print(next(lista))

>>> 0
```

Podemos ver a diferença de memória utilizada entre uma lista comum e um gerador abaixo:  
```
import sys

lista1 = [x for x in range(1000)]
lista2 = (x for x in range(10))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))

>>> 9016
>>> 112
```

---

## ZIP e ZIP_LONGEST

Para combinarmos duas listas de forma ordenada, podemos utilizar as funções **zip()** (built-in) e **zip_longest()** (necessário importar do módulo *itertools*). No exemplo abaixo, interligar as cidades e seus respectivos estados, que estão em listas distintas.  
```
cities = ['Lajeado', 'Chapecó', 'Londrina', 'Sorocaba', 'Duque de Caxias', 'Ouro Preto', 'Salvador']
states = ['RS', 'SC', 'PR', 'SP', 'RJ', 'MG']

uf_cities = zip(states, cities)
for state, city in uf_cities:
    print(f'{city}/{state}')

>>>
Lajeado/RS
Chapecó/SC
Londrina/PR
Sorocaba/SP
Duque de Caxias/RJ
Ouro Preto/MG
```
A função **zip()** cria um objeto iterador. Logo, se apenas mandássemos exibílo, o retorno seria algo como `<zip object at 0x7fe3a75937c0>`.  

É possível verificar que a última cidade (Salvador) não foi incorporada, pois a quantidade de valores dessa lista é superior. Para resolver isso, podemos utilizar a função **zip_longest**:  
```
from itertools import zip_longest

cities = ['Lajeado', 'Chapecó', 'Londrina', 'Sorocaba', 'Duque de Caxias', 'Ouro Preto', 'Salvador']
states = ['RS', 'SC', 'PR', 'SP', 'RJ', 'MG']

uf_cities = zip_longest(states, cities, fillvalue='Estado')
print(list(uf_cities))

>>> [('RS', 'Lajeado'), ('SC', 'Chapecó'), ('PR', 'Londrina'), ('SP', 'Sorocaba'), ('RJ', 'Duque de Caxias'), ('MG', 'Ouro Preto'), ('Estado', 'Salvador')]
```

Podemos utilizar a função **count()** (também do módulo *itertools*) para criar um índice para essa lista composta. Deve-se cuidar para, nesse caso, utilizar apenas **zip**, pois a função **count()**, sendo um iterador, acarretará em um loop infinito no **zip_ongest**:  
```
from itertools import count

cities = ['Lajeado', 'Chapecó', 'Londrina', 'Sorocaba', 'Duque de Caxias', 'Ouro Preto']
states = ['RS', 'SC', 'PR', 'SP', 'RJ', 'MG']

index = count()
uf_cities = zip(index, states, cities)
for index, state, city in uf_cities:
    print(f'{index}: {city}/{state}')

>>>
0: Lajeado/RS
1: Chapecó/SC
2: Londrina/PR
3: Sorocaba/SP
4: Duque de Caxias/RJ
5: Ouro Preto/MG
```

---

## CONDICIONAIS

* `in`: permite verificar se um valor está numa lista, p.e.: `if chosed_color in beauty_colors:`  
* `not in`: permite verificar se um valor **não** está numa lista, p.e.: `if chosed_color not in ugly_colors:`  
* `if <lista>:`: teste que retorna se uma lista está vazia (`False`) ou se contém ao menos um registro (`True`)  
* `if <objeto> in <lista>:`: testa se o objeto está dentro de uma lista

### Operações ternárias

Uma condição pode ser expressada com apenas uma linha, através de uma operação ternária:
```
<operação_se_condição1> if <condição1> else <operação_se_não_condição1>
```
Da mesma forma, pode-se dar um comando com o operador **or** que faz o teste booleano das variáveis e utiliza a primeira que for verdadeira:
```
name = input('Digite o seu nome: ')  # usuário deixa em branco
print(name or 'Você não digitou nada')

>>> 'Você não digitou nada'
```
ou:
```
a = False
b = None
c = {}
d = []
e = ''
f = 'nome'
g = 15

var = a or b or c or d or e or f

# a variável receberia o valor de f, que é a primeira com valor True.
```
  
---

## FUNÇÕES

Define-se a função (rotina) através da estrutura:  
```
def <função>():
	<comandos da função>

<função>()
```
Para função com parâmetro personalizado, atribui-se dentro de **()**:
```
def <função>(msg)
	<comandos da função>
	
<função>(<parâmetros personalização>)
```
Pode-se fazer o empacotamento dos parâmetros utilizando-se **(*)**. Para uma função que some um número indeterminado de valores, p.e.:
```
def <função>(*args)
	s = 0
	para args in values:
		s += num

<função>(1, 2, 3, 4)
<função>(4, 5)
...
```
* **kwargs** (keyword arguments): são os argumentos nomeados passados para a função, e é identificado com 2 asteriscos **(* *)**. Por exemplo:
```
def funcao(*args, **kwargs):
	print(args)
	print(kwargs['nome'])
	
funcao(1, 2, 3, 4, nome='José', idade='50')

>>> (1, 2, 3, 4)
>>> José
```
Idealmente, deveria-se utilizar `nome = kwargs.get('nome')`, pois caso o argumento 'nome' não exista, esse último comando retorna apenas 'None' ao invés de um erro.  

* Caso o parâmetro seja uma lista, não é necessário utilizar **(*)**, pois o Python já a considera com tamanho variável.  
* Pode-se inserir um argumento opcional, definindo qual valor deve receber caso o usuário opte por não utilizá-lo:  
```
def função(a, b, c=0)
```
* `global <var>`: torna o escopo da variável global.  
* `return <var>`: retorna o resultado da operação dentro da função para o programa principal.  


### Expressões lambda (anônimas)
São funções simplificadas (com poucos comandos) escritas em apenas 1 linha de código, quando é necessário passar uma função por parâmetro para outra função ou método, por exemplo.  
```
a = lambda x, y: x * y
print(a(2, 3))

>>> 6
```
Uma aplicação prática seria a ordenação de uma lista com sublistas, na qual deve ser informado por qual valor a ordenação deve ser realizada:  
```
lista = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5]]
lista.sort(key=lambda item: item[0])
lista.sort(key=lambda item: item[1], reverse=True)
```


### Help e docstrings
* Para obtenção de ajuda com alguma função no Python, utilizar `help(<função>)`.  
* Para inserção de docstring em uma função, inserir o texto de ajuda entre **"""** logo após a defginição da função:  
```
def função():
	"""
	Esta é uma explicação da função.
	Aqui podem ser dadas dicas.
	Sempre entre 3x"".
	"""
	<início dos comandos das funções>
```


---

## ERROS E EXCEÇÕES

* `try`: caso haja algum erro/exceção dentro desse bloco, o programa não irá retornar o erro.  
* `except`: serão executados os comandos desse bloco caso tenha havido falha no bloco **try**.  
* `else`: serão executados os comandos desse bloco caso **não** tenha havido falha no bloco **try**.  
* `finally`: este bloco será executado independentemenhte de o bloco **try** ter tido falha ou não.  

A estrutura pode conter vários **except**, especificando-se o que deve ser executado conforme o erro/exceção retornado pelo sistema:  
```
try:
	n = int(input('Digite um número: '))
except (ValueError, TypeError):
	print('Há um problema com os valores digitados.')
except ZeroDivisionError:
	print('Não é possível fazer divisão por zero (0).')
....
```

A causa ou o tipo de erro/exceção podem ser exibidos através da estrutura:  
```
except Exception as <var>:
	print(f'O erro encontrado foi {<var>.__cause__}') # pode ser também {<var>.__class__}
```

### Placeholders

* `pass` ou `...`: placeholders utilizados em partes do código que ainda estão incompletas, fazendo com que o interpretador passe por esse ponto ignorando eventuais erros. Idelamente deve ser incluído um comentário especificando o que será feito nessa parte do código.
```
if True:
	#A inserir o código para caso o teste seja verdadeiro
	pass
else:
	print('not OK')
```

---
## MANIPULAÇÃO DE ARQUIVOS

* `<var> = open(name, 'rt')`: joga para a variável o arquivo aberto 'name'.	'r' = read	't' = text
	* `'wt+'`: parâmetro para criação do arquivo. '**+**' irá criá-lo.	'w' = write	't' = text
	* `'at'`: 'a' = append. Serve para preparar o arquivo para uma adição no mesmo
		* executado o comando acima, deve-se executar `<var>.write(dados)` para gravação dos dados no arquivo
* `<var>.close()`: fecha o arquivo jogado para dentro da variável


### Bloco with

Uma forma de abrir e ler o conteúdo de um arquivo sem precisar fechá-lo (o Python decide quando fazer isso):
```
with open('arquivo.txt') as file_object:
    contents = file_object.read()

```

Passamos o conteúdo de **file_object** para a variável **contents** pois, do contrário, o conteúdo do arquivo só ficará disponível em **file_object** dentro do bloco **with**.
Para passa cada linha do arquivo para uma lista, podemos usar a seguinte estrutura:
```
with open('arquivo.txt') as file_object:
    lista = file_object.readlines()
```

O comando **open('arquivo.txt')** só abrirá o arquivo se este estiver localizado no mesmo diretório do arquivo de Python em execução.  
Quando o arquivo a ser aberto estiver em um sub-diretório dentro do diretório onde está o arquivo Python, pod-se utilizar um path de arquivo relativo:
```
with open('sub_directory/arquivo.txt') as file_object:
    contents = file_object.read()
```

Quando o arquivo a ser aberto estiver em um diretório totalmente diferente, devemos utilizar um path de arquivo absoluto:
```
with open('/home/douglas/documents/sub_directory/arquivo.txt') as file_object:
    contents = file_object.read()
```

* A fim de encurtar o argumento em **open()**, pode-se armazenar o path em uma variável e utilizar esta última como argumento do comando.


### JSON

O JSON é um módulo para salvar informações geradas pelos códigos em arquivos externos (.json), que podem ser posteriormente recuperadas e lidas pelo software.  

* Para gravação, utiliza-se `json.dump(valor, arquivo)`:
```
lista = [1, 2, 3]
with open('arquivo.json') as file_object:
    json.dump(lista, file_object)
```

* Para leitura, utiliza-se `json.load(arquivo)`:
```
with open('arquivo.json') as file_object:
    json.load(file_object)
    print(lista)

```

---
## CLASSES

* Quando escrevemos uma classe, definimos o comportamento geral que toda uma categoria de objetos pode ter. Quando criamos objetos individuais a partir da classe, cada objeto será automaticamente equipado com o comportamento geral; então você poderá dar a cada objeto as características únicas que desejar.   
* Uma classe sempre deve ser nomeada com a primeira letra maiúscula.  
* Para criação de uma classe, usar a seguinte estrutura:  
```
class Classe():
	def __init__(self, <var1>, <var2>,...)
		self.var1 = var1
		self.var2 = var2
		...
	
	def método(self):
	<comandos>
```

Para inserção de um objeto na classe (criação de instância):  
```
<objeto> = Classe('int', 'str',...)
```

Para acessar um atributo de uma das instâncias:
```
<objeto>.<var>
```
Para executar um método em determinada instância da classe:
```
<objeto>.método()
```
Pode-se especificar um valor default para um atributo (no corpo do método \__init__), fazendo com que não seja necessário atribuir um parâmetro na chamada do método. Para atribuição de um outro valor posteriormente:
```
self.<objeto> = valor
```
Para incrementar o valor do atributo, basta utilizar **+=** no comando acima.  

É possível modificar o valor de um atributo utilizando-se um método dedicado a isso:
```
def update_parameter(self, value)
	self.object = value
	
<objeto>.update_parameter(valor)
```
Pode-se criar uma classe-filha com os atributos da classe-pai mais os próprios, utilizando a estrutura abaixo e método **super()**:
```
class ClassePai():
	def __init__(self, 'atributo1', 'atributo2',...)
	...
	
class ClasseFilha(ClassePai):
	def __init__(self, 'atributo1', 'atributo2',...)
	super().__init__('atributo1', 'atributo2', 'atributo3'...)
	<comandos>
```
* Podemos sobreescrever um atributo da classe-pai nomeando um atributo da classe-filha com o mesmo nome. Assim, as instâncias criadas a partir da classe-filha utilizarão o parâmetro do atributo inserido nela.  








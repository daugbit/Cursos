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
	* `count()`: utilizada para gerar índices para outros objetos, como listas. Ao contrário da função *range()*, a *count* não tem um fim determinado. A função **count()** pode ser personalizada com os parâmetros *start* e *step*: `contador = count(start=10, step=2)`;  
	* `combinations(<lista>, n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, sem importar a ordem;  
	* `permutations(<lista>, n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, considerando a ordem;  
	* `product(<lista>, repeat=n)`: utilizado para criar todas as combinações possíveis de *n* elementos de uma lista, considerando a ordem e combinações de um mesmo elemento. Também é possível separar os elementos da lista em sublistas, atentando-se para a necessidade de desempacotar a lista principal ao executar a função: `product(*lista)`;  
	* `<objeto> = groupby(<lista>, ordenação)`: agrupa os valores de uma lista a partir de uma ordenação especificada - a qual pode ser especificada a partir de uma expressão *lambda*;  
	* `l1, l2, l3 = tee(l0)`: faz cópia do iterador **l0** para outras variáveis, fazendo com que os valores contidos nele possam ser iterados mais de uma vez;  


### pathlib
O módulo pathlib é uma biblioteca incorporada do Python que fornece uma maneira fácil e orientada a objetos para trabalhar com caminhos de arquivo e diretório. Com o módulo pathlib, é possível criar, manipular e acessar caminhos de arquivos e diretórios usando objetos de caminho (Path objects), que representam um caminho absoluto ou relativo em um sistema de arquivos.
```
from pathlib import Path

path = Path('/path/to/file')		# Criando um objeto Path

if path.exists():			# Verificando se um arquivo existe
    print('O arquivo existe')

print(path.name)			# Obtendo o nome do arquivo

print(path.parent)			# Obtendo o diretório pai

print(path.absolute())			# Obtendo o caminho absoluto

for file in Path('/path/to/directory').iterdir():	# Listando arquivos em um diretório
    print(file)
```
```
from pathlib import Path

path = Path('/path/to/file.txt')	# Criando um objeto Path para um arquivo existente

print(path.exists())  			# retorna True
path.touch() 				# Cria o arquivo
print(path.name)  			# Obtendo o nome do arquivo: 'file.txt'
print(path.parent)			# Obtendo o diretório pai: '/path/to'
for file in path.iterdir():		# Listando todos os arquivos no diretório
    if file.is_file():
        print(file.name)
path.mkdir()				# Criando o diretório
path.write_text('xxx')			# Escreve algo no arquivo criado
with path.open('a+') as file:		# Escreve algo no arquivo criado (modo append)
	file.write('lorem ipsum\n')
	file.write('dolor sit amet\n')

```

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
* `isinstance(<objeto>, <tipo_primitivo>)`: retorna um valor booleano para o objeto e o tipo primitivo especificado. O tipo pode ser uma tupla com 2 tipos.    
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


### Desempacotamento de listas (também aplicável a tuplas)

Desempacotamento de dados, também conhecido como "unpacking", é uma técnica em Python que permite atribuir valores a várias variáveis ​​de uma só vez. Isso é especialmente útil quando se trabalha com sequências como listas, tuplas e dicionários, mas também pode ser usado com outras estruturas de dados que suportam a operação de indexação.  
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
* `var = <dicionario>.pop('key)`: remove o par chave-valor da "key" especificada e joga para a variável **var**
* `var = <dicionario>.popitem()`: remove o último par chave-valor e joga para a variável **var**
* `<dicionário>.get('key', x)`: retorna o valor da chave 'key' caso ela exista, ou x caso essa chave não exista.  
* `<dicionário>.setdefault('key', 'value')`: determina um valor padrão para a chave 'key', caso um valor não seja informado.  
* `<dicionário1>.update(<dicionário2>)`: concatena o dicionário 2 no dicionário 1 (o operador **+** não funciona para dicionários). Esta função também pode ser utilizada para adicionar novas chaves do dicionário e para converter tuplas/listas para pares chaves-valor e incluílos no dicionário.  
  * A junção de 2 dicionários pode ser feita através da expressão `<dicionário3> = {**<dicionário1>, **<dicionário2>}`  
* `copy.deppcopy<dicionario>`: o módulo **copy** faz uma cópia completa de um dicionário para um novo, uma vez que a o método **copy** copia apenas o dados imutáveis para o novo dicionário, enquanto linka dados mutáveis ao dicionário original (shallow copy).
  * A estrutura `dic1 = dic2` fará a conexão entre ambas, logo, o que for alterada em uma refletirá na outra.    


### Desempacotamento de dicionários

Utiliza a mesma lógica do desempacotamento de listas e tuplas, porém, ao invés de utilizar o asterisco (*), utiliza dois asteriscos (**):  
```
def minha_funcao(a, b):
    print(a, b)

meu_dicionario = {'a': 1, 'b': 2}
minha_funcao(**meu_dicionario)
```

---


## SETS (CONJUNTOS)

É uma variável que armazena uma série de valores. Também é identificada por **{}**, sendo que não há o par chave-valor (apenas valor), sem qualquer ordem definida.  
`var = {1, 2, 3, 4, 5}` ou `var = set()`
**os conjuntos NÃO aceitam valores duplicados**. Útil para remover valores duplicados de uma lista.

* `<set>.add(value)`: adição de um valor ao conjunto.  
* `<set>.discard(value)`: exclusão de um valor do conjunto.  
* `<set>.update(value)`: itera sobre o valor, adicionando cada caractere como um valor separado ({'v', 'a', 'l', 'u', 'e'}).  
* `<set>.clear()`: limpa o conjunto, deixando-o vazio
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
* `nonglobal <var>`: quando temos uma função interna (função dentro de outra função), e há uma variável criada na "função mãe", utiliza-se **nonglobal** a fim de que o Python utilize a variável já existente.  
* `return <var>`: retorna o resultado da operação dentro da função para o programa principal.  


### Funções lambda (anônimas)
Funções lambda são funções anônimas em Python que podem ter qualquer número de argumentos, mas apenas uma expressão como corpo de função. Elas são úteis para criar funções simples e de uso único, sem a necessidade de definir uma função completa.
A sintaxe básica para criar uma função lambda é:
```
lambda argumentos : expressão
```

Uma aplicação prática seria a ordenação de uma lista com sublistas, na qual deve ser informado por qual valor a ordenação deve ser realizada:  
```
lista = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5]]
lista.sort(key=lambda item: item[0])
lista.sort(key=lambda item: item[1], reverse=True)
```

Você pode chamar a função lambda da mesma forma que uma função normal:
```
resultado = produto(2, 3)
print(resultado)  # 6
```

As funções lambda são frequentemente usadas como argumentos de funções de ordem superior (como map(), filter() e reduce()), onde uma função é necessária como argumento. Por exemplo, a seguinte função lambda é usada para filtrar os números pares de uma lista:
```
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x : x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]
```


### Função map
Retorna um iterador que aplica a expressão (lambda) ou função definida para cada item do objeto iterável.  
```
var = map(<expressão/função>, objeto)
```

### Função filter
Semelhante à função map(), porém retornando **True** ou **False**. Logo, a nova variável será compostas apenas com os valores do objeto original que cumprirem com a condicional expressa.  
```
var = filter(<expressão/função>, objeto)
```

### Função reduce
Funciona como um acumulador, devendo ser estruturado da forma abaixo (o módulo *functools* precisa ser importado):
```
from functools import reduce

var = reduce(lambda <acumulador>, <valor>: <valor> + <acumulador>, <lista>, <valor_inicial_acumulador>)
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

## Higher order functions
High order functions são funções que recebem uma função ou mais como argumento, retornando outra função. Isso permite a composição de funções, ou seja, ter funções pequenas que compõem outras funções maiores. Funções que são chamadas dentro de outra são chamadas callback functions, pois são “called back” (“chamadas de volta” em uma tradução livre) dentro da função onde estão compostas.  
```
def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))
```

### Closures
Uma closure ocorre quando uma função é declarada dentro do corpo de outra, e a função interior referencia variáveis locais da função exterior. Em tempo de execução, quando a função exterior é executada, então uma closure é formada, que consiste do código da função interior e referências para quaisquer variáveis no escopo da função exterior que a closure necessita.  
Essa estrutura é útil quando queremos adiar a execução de uma função (a interna), pois a falta de algum parâmetro que será passado apenas posteriormente ocasionaria 
```
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
```

Outra forma de adiar a execução de uma função seria a utilização da função anônima lambda:
```
print('Comandos: listar, desfazer e refazer')
tarefa = input('Digite uma tarefa ou comando: ')

comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    
comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']

comando()
```

### Variáveis livres e non local
Em uma estrutura de funções dentro de outras funções, variável livre é aquela que é declarada no corpo da função externa pode ser acessada e alterada a partir de qualquer das funções internas, desde que definida como **nonlocal**:  
```
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
```

### Funções decoradoras e Decoradores
Decorar = Adicionar / Remover/ Restringir / Alterar. Funções decoradoras são funções que decoram outras funções. Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.  
Decoradores são elementos que modificam a execução de uma função, como para que seja executada uma outra função antes desta, por exemplo.  
Exemplo de função decoradora:
```
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Decorando...')        
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('douglas')
print(invertida)
```
Um decorador é identificado como **@decorador** e é declarado acima da função. Utilizando-se um decorador, o corpo do código principal acima fica mais simplificada:  
```
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Decorando...')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('douglas')
print(invertida)
```

### Funções recursivas
Funções que podem se chamar de volta. Úteis p/ dividir problemas grandes em partes menores.  
```
# Sequência Fibonacci

def recursiva(end=0, v1=0, v2=1):
    print(v1)
    v1 += v2
    v2, v1 = v1, v2
    if v1 > end:
        return None
    return recursiva(end, v1, v2)

recursiva(10000)

```
O Python tem um limite de segurança para recursão, tendo em vista que cada uma delas gera nova instância no *call stack*. Caso seja muito necessário utilizar acima desse limite, pode-se utilizar `sys.setrecursionlimit(<limite_desejado>)` do módulo **sys** (não recomendado, pois o excesso de instâncias gera sobrecarga na memória do computador).  

### Positional-only arguments
Permite especificar argumentos que só podem ser passados como argumentos posicionais, ou seja, não podem ser passados como argumentos nomeados. Com os argumentos positional-only, você pode definir argumentos que só podem ser passados na posição correta na chamada da função, sem precisar se preocupar com o nome do argumento. Isso torna o código mais claro e menos suscetível a erros. 
Para definir um argumento positional-only, você usa a sintaxe de barra (/) antes do nome do argumento na definição da função. Por exemplo:
```
def soma(a, b, /):
    return a + b
```
Nesse exemplo, o argumento / indica que todos os argumentos antes da barra são posicionais, e não podem ser passados como argumentos nomeados. Então, para chamar a função soma(), você deve passar os argumentos a e b na ordem correta:
```
resultado = soma(2, 3)
print(resultado)  # 5
```

### Keyword-only arguments
Permite especificar argumentos que só podem ser passados como argumentos nomeados, ou seja, não podem ser passados como argumentos posicionais.
Para definir um argumento keyword-only, você usa a sintaxe de asterisco duplo (**) antes do nome do argumento na definição da função. Por exemplo:
```
def enviar_email(destinatario, mensagem, *, cc=None, bcc=None):
    # lógica de envio de email
    pass

enviar_email("fulano@example.com", "Olá!", cc="ciclano@example.com", bcc="beltrano@example.com")
```
Nesse exemplo, os argumentos cc e bcc só podem ser passados como argumentos nomeados, e não podem ser posicionais. Ou seja, você deve usar a sintaxe de nome do argumento ao chamar a função.
Vale ressaltar que os argumentos keyword-only só podem ser definidos depois de todos os argumentos posicionais, e que você pode definir argumentos opcionais e posicionais antes dos argumentos keyword-only. No exemplo abaixo, os argumentos cc e bcc são opcionais e posicionais, enquanto o argumento assunto é obrigatório e keyword-only:
```
def enviar_email(destinatario, mensagem, cc=None, bcc=None, *, assunto=None):
    # lógica de envio de email
    pass
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

Para armazenar a exceção, a fim de utilizá-la posteriormente (para um log, por exemplo), utiliza-se o comando **raise**:
```
def divisao(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        raise


try:
    print(divisao(2, 0))
except ZeroDivisionError as error:
    print(error)

>>> division by zero
```
ou:
```
def divisao(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('o divisor não pode ser zero.')
    return n1 / n2


try:
    print(divisao(2, 0))
except ZeroDivisionError as error:
    print(f'Log: {error}')
    
>>> Log: o divisor não pode ser zero. 
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

O módulo json em Python é usado para trabalhar com dados JSON (JavaScript Object Notation). Existem duas funções principais para codificar (conversão de objeto Python em uma string JSON) dados em Python para JSON, que são dump() e dumps().
A diferença entre as duas funções é que dump() grava os dados diretamente em um arquivo, enquanto dumps() retorna uma string JSON.
O método dump() é usado para gravar dados JSON em um arquivo. Ele requer dois argumentos, o primeiro é o objeto Python que você deseja serializar e o segundo é o objeto de arquivo para gravar. Por exemplo:

```
import json

dados = {"nome": "João", "idade": 30}
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)
```

O método dumps() é usado para converter um objeto Python em uma string JSON. Ele requer apenas um argumento, o objeto Python que você deseja serializar. Por exemplo:
```
import json

dados = {"nome": "João", "idade": 30}
json_serializado = json.dumps(dados)
```

**dumps()** é útil quando você precisa enviar dados JSON pela rede ou salvá-los em um banco de dados, por exemplo. Já dump() é útil quando você precisa gravar dados JSON em um arquivo.

Assim como dump() e dumps(), a diferença entre load() e loads() no módulo json em Python também é que um é usado para carregar dados JSON a partir de um arquivo e o outro é usado para carregar dados JSON de uma string.
A função load() é usada para ler dados JSON de um arquivo e analisá-los em um objeto Python. Ela requer um argumento, o objeto de arquivo para ler. Por exemplo:
```
import json

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)  # {'nome': 'João', 'idade': 30}
```
A função loads() é usada para converter uma string JSON em um objeto Python. Ela requer apenas um argumento, a string JSON para analisar. Por exemplo:
```
import json

json_serializado = '{"nome": "João", "idade": 30}'
dados = json.loads(json_serializado)

print(dados)  # {'nome': 'João', 'idade': 30}
```
**loads()** é útil quando você recebe dados JSON como uma string, por exemplo, quando faz uma solicitação HTTP para uma API. Já load() é útil quando você precisa ler dados JSON de um arquivo local.


---
## CLASSES

Classes em Python são estruturas que permitem definir novos tipos de objetos. Uma classe é uma espécie de modelo ou molde que define as características e comportamentos que os objetos daquela classe devem ter.  
As classes em Python seguem a orientação a objetos e permitem que você crie objetos que possuam atributos e métodos. Atributos são as características ou propriedades do objeto, enquanto que métodos são as funções ou comportamentos que o objeto pode executar.  
Quando escrevemos uma classe, definimos o comportamento geral que toda uma categoria de objetos pode ter. Quando criamos objetos individuais a partir da classe, cada objeto será automaticamente equipado com o comportamento geral; então você poderá dar a cada objeto as características únicas que desejar.   
Uma classe sempre deve ser nomeada com a primeira letra maiúscula.  
Para criação de uma classe, usar a seguinte estrutura:  
```
class Classe():
	def __init__(self, <atributo1>, <atributo2>,...)
		self.atributo1 = atributo1
		self.atributo2 = atributo2
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



### Métodos de classe
Métodos de classe em Python são métodos que são definidos dentro da classe, mas que não dependem de uma instância específica da classe. Em outras palavras, eles podem ser chamados diretamente na classe, sem a necessidade de criar um objeto da classe antes.  
Para definir um método de classe em Python, basta usar o decorador @classmethod antes da definição do método. Esse decorador indica que o método é um método de classe e não um método de instância.  
```
class Pessoa:
    total_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

    @classmethod
    def total(cls):
        return cls.total_pessoas
```
Nesse exemplo, temos a classe Pessoa, que tem um atributo de classe total_pessoas que guarda o número total de instâncias criadas da classe, e um método de classe chamado total() que retorna o valor desse atributo.  
Os métodos de classe são úteis quando precisamos criar métodos que realizam alguma operação na classe em si, em vez de em instâncias específicas da classe. Alguns exemplos de uso incluem criar métodos de fábrica para criar instâncias da classe com determinadas configurações, criar métodos de validação que verificam se os dados da classe estão corretos, ou criar métodos utilitários que realizam operações gerais na classe.  

### Métodos estáticos
Já um **método estático** é como se fosse uma função normal, não relacionada à classe, mas que é definida dentro da classe por questão de organização. Ele é precedido pelo decorador **@staticmethod** e não tem acesso aos parâmetros da classe e das instâncias, logo, não recebe *self* e nem *cls*:  
```
class MyClass:
	@staticmethod
	def function(<var>, <var>)
		<comandos>
```
Os métodos estáticos são úteis quando precisamos criar métodos que realizam uma operação independente do estado da instância ou da classe, ou que não precisam de acesso aos atributos de classe ou de instância. Alguns exemplos de uso incluem criar funções utilitárias que realizam operações gerais, criar métodos auxiliares que não dependem do estado da instância ou da classe, ou criar métodos de validação que não dependem do estado da instância ou da classe.  

### Getters e setters
Os *getters* e os *setters* servem como manipuladores dos atributos das instâncias de uma classe, que podem verificar se um dos dados encontra-se da forma desejada e, não estando, o manipulam da forma desejada. Isso tudo através de um código em separado, fazendo com que a estrutura principal da classe não fique poluída com tais comandos.  
Outra aplicação para esses métodos especiais é quando se encapsula os atributos de uma classe, ou seja, ao se definir o acesso como *privado*. Neste caso, só é necessário o método **getter**.  

O **getter** é o componente que irá fazer a "captura" da variável de dentro do método, fazendo com que a verificação seja executada antes da atribuição de valor a ela.  
O **setter** é aquele que realizará as operações de verificação e manipulação do valor, jogando-o por fim à variável.  
```
class People:
    current_year = datetime.today().year

    def __init__(self, name, age, function, hiring_year):
        self.name = name
        self.age = age
        self.function = function
        self.employed_time = self.employed_time(hiring_year)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, str):
            value = int(value)
        self._age = value

    @classmethod
    def employed_time(cls, hiring_year):
        employed_time = cls.current_year - hiring_year
        return employed_time


employee1 = People('Mark', '45', 'Manager', 2009)
employee2 = People('John', 23, "Seller", 2020)

print(employee1.__dict__)
print(employee2.__dict__)


>>> {'name': 'Mark', '_age': 45, 'function': 'Manager', 'employed_time': 13}
>>> {'name': 'John', '_age': 23, 'function': 'Seller', 'employed_time': 2}
```

* Se há um atributo da classe, todas as instâncias receberão o valor desse atributo. Quando se atribui um valor para um atributo de mesmo nome para uma das instâncias da classe, apenas essa instância terá esse valor. Porém, não é o atributo da classe que é alterado, mas sim é criado um novo atributo para a instância em particular.  


### Associação de classes

É quando se configura duas ou mais classes a fim de que essas trabalhem em conjunto. Na *associação*, porém, as classes continuam podendo trabalhar individualmente quando necessário.  
```
class Car:
    def __init__(self, maker, model):
        self.__maker = maker
        self.__model = model
        self.__fuel = None

    @property
    def maker(self):
        return self.__maker

    @property
    def model(self):
        return self.model

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel


    def descricao(self):
        print(f'O veículo {self.__maker} {self.__model} utiliza o combustível {self.fuel.fuel_type}.')


class Fuel:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type
        

car1 = Car('Tesla', 'Model S')
car2 = Car('Porshe', 'Cayenne')

fuel1 = Fuel('gasolina')
fuel2 = Fuel('eletricidade')

wheel1 = Wheel('18"')
wheel2 = Wheel('15"')

car1.fuel = fuel2
car2.fuel = fuel1

car1.descricao()
car2.descricao()

>>> O veículo Tesla Model S utiliza o combustível eletricidade.
>>> O veículo Porshe Cayenne utiliza o combustível gasolina.
```

### Agregação de classes

É quando utilizamos uma instância de uma classe como atributo de outra classe. Logo, a classe necessita que esta segunda classe exista para que o seu atributo funcione adequadamente.  
No exemplo abaixo, utilizamos uma instância do CarrinhoCompras para adicionar um produto (instância da classe Produto). Assim, a classe CarrinhoCompras precisa da classe Produto para conseguir incluir itens no atributo *self.carrinho*.  

```
class CarrinhoCompras:
    def __init__(self):
        self.carrinho = []

    def add_produto(self, produto):
        self.carrinho.append(produto)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
        
carrinho = CarrinhoCompras()

p1 = Produto('Relógio', 199.5)
p2 = Produto('Camiseta', 120.99)

carrinho.add_produto(p1)
carrinho.add_produto(p2)
```


### Composição de classes

Na composição, a conexão entre duas classes é feita instanciando a segunda classe a partir de um método da primeira classe. Assim, caso a instância da primeira classe seja excluída, a instância da segunda classe criada a partir dela também será deletada.  

```
class Cliente:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.enderecos = []

    def include_address(self, city, state):
        self.enderecos.append(Endereco(city, state))


class Endereco:
    def __init__(self, city, state):
        self.city = city
        self.state = state


c1 = Cliente('Marcos', 23)
c1.include_address('Lajeado', 'RS')
```


### Herança de classes

Na herança simples podemos montar uma 'árvore' de classes, de forma que haja uma hierarquia entre elas. Os atributos e métodos da classe-mãe são automaticamente aplicados à(s) classe(s)-filha(s), sendo que estas podem ter atributos e métodos particulares.

```
class MembroEscola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(MembroEscola):
    def estudar(self):
        print(f'O aluno {self.nome} está estudando.')


class Professor(MembroEscola):
    def dar_aula(self):
        print(f'O professor {self.nome} está dando aula.')


class Diretor(MembroEscola):
    def dar_bronca(self):
        print(f'O diretor {self.nome} está dando bronca.')
        
a1 = Aluno('Caroline', 23)
p1 = Professor('Marlon', 45)
d1 = Diretor('Jorge', 62)

a1.estudar()
p1.dar_aula()
d1.dar_bronca()
```

* Podemos sobreescrever um atributo da classe-mãe nomeando um atributo da classe-filha com o mesmo nome. Assim, as instâncias criadas a partir da classe-filha utilizarão o valor do atributo inserido nela.  
```
class CarrinhoCompras:
    name = 'Nome do carrinho'


class Produto:
    name = 'Nome do produto'


p1 = Produto()
print(p1.name)

>>>Nome do produto
```

* Quando sobreescrevemos um método (ou em outros casos), podemos ainda chamar o método **super()**, que irá chamar o método especificado da classe-mãe. Caso a classe da qual se queira sobreescrever o método seja de níveis superiores à mãe (ancestral), deve-se utilizar o nome dela no lugar de *super()*.
* Pode-se ainda criar um novo método construtor **__init__** para a subclasse, reaproveitando-se os atributos da super-classe e criando novos.  

```
class MembroEscola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Membro {self.nome} está falando.')


class Aluno(MembroEscola):
    def falar(self):
        print(f'Aluno {self.nome} está falando.')


class AlunoPrimario(Aluno):
    def __init__(self, nome, sobrenome, idade):
        MembroEscola.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        MembroEscola.falar(self)
        Aluno.falar(self)
        print(f'Agora o aluno primário {self.nome} está falando.')
        

ap1 = AlunoPrimario('Cadu', 'Freitas', 5)
ap1.falar()

>>>
Membro Cadu está falando.
Aluno Cadu está falando.
Agora o aluno primário Cadu está falando.
```
No exemplo acima, ao invés de `MembroEscola.falar(self)`, também é possível especificar o método de qual super classe que queremos utilizar através do próprio método **super()**: `super(MembroEscola, self).falar()`.  

Utiliza-se o *method resolution order* (**Classe.mro** ou o atributo **\__mro\__**) para saber qual caminho de resolução dos métodos de uma árvore de classes o Python está considerando. Para o mesmo exemplo de cima:  
```
print(AlunoPrimario.mro())
print(AlunoPrimario.__mro__)

>>> [<class '__main__.AlunoPrimario'>, <class '__main__.Aluno'>, <class '__main__.MembroEscola'>, <class 'object'>]
>>> (<class '__main__.AlunoPrimario'>, <class '__main__.Aluno'>, <class '__main__.MembroEscola'>, <class 'object'>)
```

Uma classe pode ter heranças múltiplas, ou seja, herdar mais de uma classe. A ancestralidade é definida na definição da classe:  
```
class Smartphone(Electronic, LogCenter):
```

No caso de ser chamado algum método na classe acima que esteja nas duas classes-mãe, geralmente o Python executará o método da classe que estiver definida primeiro dentro dos **()**. Caso o código seja muito complexo, pode-se utilizar o **mro** a fim de descobrir o caminho de herança que o Python está considerando.  


### Mixins
* Em programação orientada a objetos, um mixin é uma classe que define um conjunto de métodos e atributos que podem ser adicionados a outras classes sem exigir herança direta dessas classes.  
* Os mixins geralmente não são projetados para serem usados como classes independentes, mas sim para serem combinados com outras classes para fornecer funcionalidades adicionais. Isso pode ser útil quando queremos adicionar comportamento comum a várias classes diferentes sem criar hierarquias de herança complexas.  
* Em Python, os mixins são geralmente definidos como classes que contêm métodos e atributos que podem ser adicionados a outras classes usando herança múltipla.  
* Por exemplo, podemos criar um mixin LoggableMixin que define um método log() para registrar mensagens de log. Podemos então adicionar esse mixin a várias classes diferentes, para que essas classes também tenham o método log() disponível.  
```
class LoggableMixin:
    def log(self, message):
        print(f"{self.__class__.__name__}: {message}")
        
class MyClass(LoggableMixin):
    def my_method(self):
        self.log("executing my_method")
```
Neste exemplo, a classe MyClass herda do mixin LoggableMixin. Isso permite que a classe MyClass use o método log() definido em LoggableMixin.  
Ao usar mixins, é importante ter cuidado para evitar conflitos de nomes entre os métodos e atributos definidos nas classes e mixins. Uma boa prática é usar um prefixo no nome dos métodos e atributos definidos no mixin, como mixin_method() ou mixin_attribute. Isso ajuda a evitar conflitos com os nomes de métodos e atributos definidos nas classes que usam o mixin.  


### Abstração e classes abstratas
* Abstração é um conceito importante em programação orientada a objetos que envolve a criação de classes abstratas que definem um conjunto de métodos ou atributos que devem ser implementados por outras classes que herdam dessa classe abstrata.  
* O objetivo da abstração é permitir que classes com características semelhantes sejam agrupadas em uma hierarquia de classes, com uma classe abstrata atuando como uma classe base que define o comportamento geral das subclasses.  
* Em Python, é possível criar classes abstratas usando o módulo abc e a classe ABC (Abstract Base Class). Uma classe abstrata é uma classe que não pode ser instanciada diretamente e que contém pelo menos um método abstrato, que é um método que deve ser implementado por qualquer classe que herda da classe abstrata.  
```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

class Gato(Animal):
    def comer(self):
        print("O gato está comendo.")

    def dormir(self):
        print("O gato está dormindo.")
```
Nesse exemplo, a classe Animal é uma classe abstrata que define dois métodos abstratos: comer() e dormir(). Qualquer classe que herda de Animal deve implementar esses dois métodos. A classe Gato herda de Animal e implementa os métodos comer() e dormir().  

É possível usar métodos abstratos em conjunto com outros decoradores em Python, mas é importante lembrar que a ordem em que os decoradores são aplicados pode afetar o comportamento do código. Para usar um método abstrato com outro decorador, basta aplicar o decorador antes/depois do decorador @abstractmethod. Em geral, é uma boa prática colocar o decorador @abstractmethod no início do método, logo acima do cabeçalho do método.  
```
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name

    @property
    # @abstractmethod
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    # @property
    # def name(self):
    #     return self._name

    @AbstractFoo.name.setter        # Ao não declarar a @property na classe atual,
    def name(self, name):           # deve-se especificar o nome classe abstrata no @setter.
        self._name = name


foo = Foo('Bar')
print(foo.name)
foo.name = 'Arroz'
print(foo.name)
```

### Polimorfismo












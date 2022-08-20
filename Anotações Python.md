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
  

---

## MANIPULAÇÃO DE TEXTOS

* `\n`: quebra de linha

* `\t`: tabulação da linha 

* `len(<objeto>)`: mostra o comprimento de uma string

* `<objeto>.count(<trecho>)`: conta quantos trechos informados há dentro do objeto

* `<objeto>.lower()`: transforma a string toda em minúsculo

* `<objeto>.upper()`: transforma a string toda em maiúsculo

* `<objeto>.capitalize()`: apenas a primeira letra da string em maiúsculo

* `<objeto>.title()`: primeira letra de cada palavra da string em maiúsculo

* `<objeto>.replace(<trecho>, <trecho>)`: troca um trecho de uma string

* `<objeto>.strip()`: remove os espaços do início e final da string
	`* <objeto>.(l/r)strip()`: remove os espaços do início/final da string
	
* `''.join(<objetolista>)`: transforma uma lista de objetos em uma string única
	* `'-'.join(<objetolista>)`: adiciona '-' (ou qualquer outro caractere) entre cada objeto na string

* `<objeto>.find(<trecho>)`: informa a localização de um trecho numa string

* `<objeto>.split()`: separa uma string em uma lista de palavras

* `<objeto>[x:y:z]`: x - primeira posição da string a ser exibida | y - posição posterior à última a ser exibida | z - passo  
    

---

## LISTAS

* `<lista>.insert(<posição>, <dado a ser inserido>)`: insere um dado na posição especificada da lista
* `<lista>.append(<dado a ser inserido>)`: insere um dado na próxima posição em branco de uma lista
* `del <lista>[x]`: deleta permanentemente o item na posição x da lista
* `var = <lista>.pop(x)`: passa o valor da posição x da lista para a variável, deletando o item da lista
* `<lista>.remove('valor')`: exclui um valor da lista em qualquer posição (pode-se usar também uma variável que contenha esse valor)
* `<lista>.sort()`: ordena a lista por ordem crescente (se numérica) ou alfabética (se string)
* `<lista>.sort(inverse=True)`: idem, mas ao contrário
* `<lista>.sorted()`: retorna a lista ordenada, mas sem alterar a lista original
* `<lista>.reverse()`: inverte a ordem da lista  
  

---

## LAÇOS

* `for var in lista`: passa cada item da *lista*, passa o valor da item para a *variável* e executa os comandos dentro do laço

  
---

## CORES 

`\033[<style;text;background>m`  
style | | text | background
:---: | :---: | :---: | :---:
none | 0 | | 
bold | 1 | |
light | 2 | |
italicized | 3 | |
underlined | 4 | | 
blink | 5 | | 
 -- | black | 30 | 40
 -- | red | 31 | 41
 -- | green | 32 | 42
 -- | yellow | 33 | 43
 -- | blue | 34 | 44
 -- | purple | 35 | 45
 -- | cian | 36 | 46
 -- | white | 37 | 47

	* __style__: 		0-none		1-bold		2-light	3-italicized	4-underlined	5-blink  
	* __text__: 		30-black	31-red		32-green	33-yellow	34-blue	35-purple	36-cian	37-white  
	* __background__:	40-black	41-red		42-green	43-yellow	44-blue	45-purple	46-cian	47-white  


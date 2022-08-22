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
* Espaçamentos e alinhamentos:  
  * `{<var>:x}`: insere o valor da variável dentro de x espaços (o que for maior que var ficará com espaçamento em branco)  
  * `{<var>:^x}`: idem, centralizado
  * `{<var>:-^x}`: idem, com traços no lugar (ou qualquer outro caractere). Ex.: `-----var-----`  
  * `{<var>:>x}`: alinhado à direita
  * `{<var>:<x}`: alinhado à esquerda
* `len(<objeto>)`: mostra o comprimento de uma string
* `<objeto>.count(<trecho>)`: conta quantos trechos informados há dentro do objeto
* `<objeto>.lower()`: transforma a string toda em minúsculo
* `<objeto>.upper()`: transforma a string toda em maiúsculo
* `<objeto>.capitalize()`: apenas a primeira letra da string em maiúsculo
* `<objeto>.title()`: primeira letra de cada palavra da string em maiúsculo
* `<objeto>.replace(<trecho>, <trecho>)`: troca um trecho de uma string
* `<objeto>.strip()`: remove os espaços do início e final da string
	* `<objeto>.(l/r)strip()`: remove os espaços do início/final da string
* `''.join(<objetolista>)`: transforma uma lista de objetos em uma string única
	* `'-'.join(<objetolista>)`: adiciona '-' (ou qualquer outro caractere) entre cada objeto na string
* `<objeto>.find(<trecho>)`: informa a localização de um trecho numa string
* `<objeto>.split()`: separa uma string em uma lista de palavras
* `<objeto>[x:y:z]`: x - primeira posição da string a ser exibida | y - posição posterior à última a ser exibida | z - passo  
    

---

## LISTAS

* `range(x, y, z)`: cria uma série com valores entre **x** e **y**, pulando **z** valores
  * `list(range(x, y, z))`: converte a série de valores em uma lista
* `<lista>.insert(<posição>, <dado a ser inserido>)`: insere um dado na posição especificada da lista
* `<lista>.append(<dado a ser inserido>)`: insere um dado na próxima posição em branco de uma lista
* `del <lista>[x]`: deleta permanentemente o item na posição x da lista
* `var = <lista>.pop(x)`: passa o valor da posição x da lista para a variável, deletando o item da lista
* `<lista>.remove('valor')`: exclui um valor da lista em qualquer posição (pode-se usar também uma variável que contenha esse valor)
* `<lista>.sort()`: ordena a lista por ordem crescente (se numérica) ou alfabética (se string)
* `<lista>.sort(inverse=True)`: idem, mas ao contrário
* `<lista>.sorted()`: retorna a lista ordenada, mas sem alterar a lista original
* `<lista>.reverse()`: inverte a ordem da lista  
* `min(<lista>)`: retorna o menor valor da lista
* `max(<lista>)`: retorna o maior valor da lista
* `sum(<lista>)`: retorna a soma dos valores da lista  
  É possível criar uma lista com um lanço dentro da mesma. Ex.:  
  `squares = [value ** 2 for value in range(1, 11)]`  
  * `copia_lista = lista[:]`: copia a lista inteira (ou uma fatia, especificando o início e final) para uma segunda lista
    * `copia_lista = lista`: conecta as duas listas. Adicionando valores em uma delas, vai para a outra também  
* `if <lista>:`: teste que retorna se uma lista está vazia (`False`) ou se contém ao menos um registro (`True`)  
* `if <objeto> in <lista>:`: testa se o objeto está dentro de uma lista  
  
---

### TUPLAS

Semelhantes às listas, mas não são alteráveis. Usa-se `()` ao invés de `[]`. Porém, pode-se sobreescrever a variável inteira.  
Ex.:  
```
colors = ('black', 'white', 'yellow')
print(colors[1])
```
Retornaria: `white`



---

## LAÇOS DE REPETIÇÃO

* `for var in lista`: passa cada item da *lista*, passa o valor da item para a *variável* e executa os comandos dentro do laço
* `break`: interrempe o laço sem executar os comandos subsequentes que estão dentro do mesmo.  
  * Pode-se iniciar o laço com `while True`  
  

---

## CONDICIONAIS

* `in`: permite verificar se um valor está numa lista, p.e.: `if chosed_color in beauty_colors:`  
* `not in`: permite verificar se um valor **não** está numa lista, p.e.: `if chosed_color not in ugly_colors:`  
* `if <lista>:`: teste que retorna se uma lista está vazia (`False`) ou se contém ao menos um registro (`True`)  
* `if <objeto> in <lista>:`: testa se o objeto está dentro de uma lista
  
---

## CORES 

`\033[<style;text;background>m`  

      
-- | none | bold | light | italic | underln | blick | black | red | green | yellow | blue | purple | cian | white
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
style | 0 | 1 | 2 | 3 | 4 | 5 | -- | -- | -- | -- | -- | -- | -- | --
text | -- | -- | -- | -- | -- | -- | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 |
back | -- | -- | -- | -- | -- | -- | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 |

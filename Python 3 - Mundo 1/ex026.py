phrase = str(input('Digite uma frase: ')).strip().upper()
print(f'''A frase contêm {phrase.upper().count("A")} letra(s) A
A primeira letra A está na posição {phrase.find("A") + 1}
A última letra A está na posição {phrase.rfind("A") + 1}''')

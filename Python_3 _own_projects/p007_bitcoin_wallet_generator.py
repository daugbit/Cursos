<<<<<<< Updated upstream
import os
import hashlib
import random
from bip39 import mnemonic_to_bytes

# ler mnemônicos do arquivo de texto
with open("mnemonics.txt", "r") as arquivo:
    mnemonicos = arquivo.read().splitlines()

# escolher um mnemônico aleatório da lista
mnemonico = random.choice(mnemonicos)

# converter o mnemônico para a chave base correspondente
chave_base = mnemonic_to_bytes(mnemonico)

# adicionar prefixo à chave base
prefixo = b"\x80"
chave_com_prefixo = prefixo + chave_base

# adicionar sufixo de checksum à chave com prefixo
primeiro_hash = hashlib.sha256(chave_com_prefixo).digest()
segundo_hash = hashlib.sha256(primeiro_hash).digest()
sufixo_checksum = segundo_hash[:4]
chave_completa = chave_com_prefixo + sufixo_checksum

# converter a chave completa para Base58
base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
base58 = ""
valor_decimal = int.from_bytes(chave_completa, byteorder="big")
while valor_decimal > 0:
    valor_decimal, remainder = divmod(valor_decimal, 58)
    base58 = base58_chars[remainder] + base58

num_nulos = len(chave_base) - len(chave_base.lstrip(b"\0"))
base58 = "1" * num_nulos + base58
chave_privada = base58

# imprimir a chave privada e o mnemônico correspondente
print("Chave privada: ", chave_privada)
print("Mnemônico: ", mnemonico)
=======
import bip39
>>>>>>> Stashed changes

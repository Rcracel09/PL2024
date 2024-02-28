import re
import os

# Abrir o ficheiro e ler
file = open("input.txt", "r")
input = file.read()  

# Colocar todas as letras em minusculo
input = input.lower()

# Dividir o input em tokens
preparedList = re.findall(r'(on|off|-?[0-9]+|=)', input)

# Variável que guarda as somas parciais
total = 0

# Flag que verifica o se está on ou off
flag = False

# Iterar sobre a lista e fazer as contas
for i in range(len(preparedList)):
    if preparedList[i] == 'on':
        flag = True
    elif preparedList[i] == 'off':
        flag = False
    elif preparedList[i] == '=':
        print(f"Soma no token numero {i}: {total}")
        total = 0  
    elif flag:
        total += int(preparedList[i])       
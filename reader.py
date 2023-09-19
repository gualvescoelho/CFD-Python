#Falta organizar coordenadas, para pegar os valores 
#Procurar a coluna desejada, ja é possivel encontrar
listLinha = []
listCoord = []

dados = 'a'
dados_ant = 'a'
countLinhas = False

with open('U-1.txt', 'r') as arquivo_binario:
    while dados:
        dados = arquivo_binario.readline()

        if(dados and dados_ant == '\n'):
            countLinhas = True

        if(dados != '\n'):
            if countLinhas == True:
                linha = dados[:-2].rsplit(' ')
                listLinha.append(linha)
            else:
                coord = dados[:-2].rsplit(' ')
                listCoord.append(coord)
            
        dados_ant = dados

i = 0

for i in range(len(listLinha)):
    listLinha[i] = [valor for valor in listLinha[i] if valor != '']
i = 0
for lista in listLinha:
    # Verifique se o valor na primeira posição da lista é igual ao valor procurado
    if lista[0] == '0.022':
        print(f"Valor encontrado na primeira posição da lista ")
        break  # Saia do loop se encontrar o valor
    i+=1

print(i)

# print(listLinha[21+2+1])

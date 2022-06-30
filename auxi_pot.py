#SE O PREÇO ESTIVER CAINDO COM BASE NOS ULTIMOS 3 DIAS, É PARA PRINTAR
#QUE A RECOMENDAÇÃO É DE COMPRA , JA QUE ESTA CAINDO , SE FOR DE ALTA
#PRINTE O CONTRARIO

#PARA ISSO, VOU LER O ARQUIVO XLSX E TRABALHAR COM MATRIZES 

import requests

print("=======================")
print("----------DAI----------")
print("---ASSISTENTE POTATO---","\nv1.1.7 - beta",
      "\n1-Recomendações diárias","\n2-Previsão de preços")
print("=======================")

##############
link = "https://commodities-api.com/api/latest?access_key=3rae4tnomm2ar7b4533e7op4wwlx78jl7uxhi9ecvf0x73x08w28w55qpn96"

resposta = requests.get(link)
preco = resposta.json()

#VOU TESTAR PRIMEIRO COM ESSES DOIS

café = preco["data"]["rates"]["COFFEE"] * 4.6656
petroleo = preco["data"]["rates"]["BRENTOIL"] * 12832

print(café, petroleo)

##############

while True:
    quest = input("O que deseja?: ")

    #DEVE SER BASEADO PELOS ULTIMOS 3 DIAS
    if quest == "1":
        print("RECOMENDAÇÃO ATIVADA")

    elif quest == "2":
        print("PREVISÃO ATIVADA")

    elif quest == "sair":
        break

    else:
        print("Não entendi")


'''
OS IF'S:

if café <= café * 0.99:
            print("Recomendação: Compra")
        else:
            print("Recomendação: Venda")
        print("-------------------")

if petroleo <= petroleo * 0.99:
            print("Recomendação: Compra")
        else:
            print("Recomendação: Venda")
        print("-------------------")


'''

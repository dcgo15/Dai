import requests


#CRIAR OPÇÃO DOLAR/REAL

print("----------DAI----------")
print("---ASSISTENTE POTATO---","\nv1.1.7 - beta",
      "\n1-Recomendações diárias","\n2-Previsão de preços")

##############
link = "https://commodities-api.com/api/latest?access_key=3rae4tnomm2ar7b4533e7op4wwlx78jl7uxhi9ecvf0x73x08w28w55qpn96"

resposta = requests.get(link)
preco = resposta.json()


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

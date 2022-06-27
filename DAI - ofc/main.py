'''
QUERO MANDAR MSG
EMAIL
REALIZAR OPERAÇÔES
FAZER TAREFAS
'''

import pywhatkit as whatsapp
import smtplib
from email.message import EmailMessage

# APP DE ASSISTENTE PESSOAL
while True:
    
    print("---------- DAI ----------")
    print("v1.0.0","| Sua assistente pessoal")

    nome = input("Qual o seu nome?: ")

    if nome == "Daniel G":
        print("Olá, Meu querido Daniel")
        input("Como você está?:")

    elif nome == "sair":
        break 
    else:
        print("Olá")

    funcs = ["Mandar msg", "Mandar email", "Pesquisar", "Realizar operações"
             , "Fazer tarefas"]

    #### FAZ PARTE DA FUNÇÃO
    '''def dai():'''

    print("Posso realizar várias coisas pra você")
    print(funcs)
    quest = input("O que você quer que eu realize?: ")


    ####### MANDAR MSG
    if quest == "0":
        number = input("Digite seu numero: ")
        msg = input("Digite sua mensagem: ")
        hora = input("Digite a hora: ")
        minu = input("Digite os minutos: ")

        whatsapp.sendwhatmsg(number, msg, 14, 58)
        break

    if quest == "1":
        with open(textfile) as fp:
            mensagem = EmailMessage()
            mensagem.set_content(fp.read())

        meu = input("Seu email: ")
        seu = input("Email do destinatario: ")

        mensagem["Subject"] = f"O conteudo é {textfile}"
        mensagem["From"] = meu
        mensagem["To"] = seu

        s = smtplib.SMTP("localhost")
        s.send_message(mensagem)
        s.quit()
        
    ##################

    ### OPERAÇAO ###
    if quest == "3":
        while True:
            oper = input("Digite o sinal desejado: ")

            if oper == "+":
                x = int(input("Digite o 1 numero: "))
                y = int(input("Digite o 2 numero: "))

                results = x + y
                print(results)

            elif oper == "-":
                x1 = int(input("Digite o 1 numero: "))
                y2 = int(input("Digite o 2 numero: "))

                results2 = x1 - y2
                print(results2)

            elif oper == "*":
                x = int(input("Digite o 1 numero: "))
                y = int(input("Digite o 2 numero: "))

                results = x * y
                print(results)

            elif oper == "/":
                x = int(input("Digite o 1 numero: "))
                y = int(input("Digite o 2 numero: "))

                results = x / y
                print(results)

            elif oper == "sair":
                break

            else:
                print("Não entendi : (")
            

        

    ####

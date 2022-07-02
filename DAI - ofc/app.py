from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty,NumericProperty,BooleanProperty
from gtts import gTTS
import speech_recognition as sr
import os
import datetime
import requests
from playsound import playsound
import wikipedia
from hunspell import Hunspell

#############
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#############

'''
EU QUERO QUE ELA PESQUISE NO WIKIPEDIA:

- frase que tem que ser oq eu falo , um comando
- pesquisa que tem que ser meu segundo comando

ENTÃO OK , SE EU JUNTAR 2 STRINGS ELAS OBRIGATORIAMENTE DEVEM FICAR JUNTAS
'''


arq_kv = '''
<Telas>:
    Inicio:
        name: "inicio"
    Ajuda:
        name: "ajuda"
    Tutorial:
        name: "tuto"
    
    
<Inicio>:
    orientation: "vertical"

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fundo.jpg"

    ActionBar:
        pos_hint: {"top": 1}
        background_color: 1, 1, 1, 0

        ActionView:
            ActionPrevious:
                title: "DAI - v1.4.1"
                app_icon: ''
                with_previous: False

            ActionButton:
                text: "Ajuda"
                on_release: app.root.current = "ajuda"

            ActionButton:
                text: "help"
                icon: "question.png"
                on_release: app.root.current = "tuto"
                

    GridLayout:
        id: "layout"
        cols: 1
        spacing: 30
        padding: [80, 120]

        Button:
            background_normal: "voice.png"
            background_down: "voice.png"
            border: 0, 0, 0, 0
            size_hint: .8, 1
            on_release: root.clicar()

        Label:
            id: fale
            text: "FALE ALGO"

        Label:
            text: "Maze technologies Inc"

        
<Ajuda>:
    orientation: "vertical"

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'fundo.jpg'

    ActionBar:
        pos_hint: {'top':1}
        background_color: 1, 1, 1, 0
            
        ActionView:
            ActionPrevious:
                title: "Help - Contatos"
                app_icon: ''
                on_release: app.root.current = "inicio"


    GridLayout:
        id: "ajuda"
        cols: 2
        spacing: 30
        padding: [20, 40]

        Label:
            text: "Telefone:"

        Label:
            text: "+55 (75) 98224-3100"

        Label:
            text: "Email:"

        Label:
            text: "softmaze6@gmail.com"

        Label:
            text: "Email alternativo:"

        Label:
            text: "danielcerqueira2346@gmail.com"
                
<Tutorial>:
    orientation: "vertical"

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'fundo.jpg'

    ActionBar:
        pos_hint: {'top':1}
        background_color: 1, 1, 1, 0
            
        ActionView:
            ActionPrevious:
                title: "Tutorial"
                app_icon: ''
                on_release: app.root.current = "inicio"

    GridLayout:
        id: "tuto"
        cols: 1
        spacing: 30
        padding: [20, 40]

        Label:
            text: "Clique no microfone para falar"

        Label:
            text: "Consulte ajuda no canto superior"

        Label:
            text: "No botão de interrogação , você verá um tutorial"

            
    
'''

class Telas(ScreenManager):
    pass

class Inicio(Screen):


    tts = gTTS("Olá ... Daniel", lang="pt-br")

    tts.save("ola.mp3")
    playsound("ola.mp3")

    def clicar(self):

        mic = sr.Recognizer()

        with sr.Microphone() as source:

            mic.adjust_for_ambient_noise(source)

            print("Diga alguma coisa: ")

            audio = mic.listen(source)

        try:

            frase = mic.recognize_google(audio, language="pt-BR")

            print("Você disse: ", frase)

        except sr.UnkownValueError:
            print("Não entendi")

        ###########################
        #################LISTAKKKKK
        dic = Hunspell('Portuguese(Brazilian)', hunspell_data_dir = r'C:\Users\WIN7\AppData\Local\Programs\Python\Python38-32\Scripts\Interfaces Graficas Py\DAI - ofc\Dicionarios')
        ###########################

        if frase == "DAE":
            s = "Sim?"

            sim = gTTS(S, lang="pt-br")
            sim.save("sim.mp3")
            playsound("sim.mp3")

        elif frase == "as horas":
            h = "Consultando horario ... Daniel"
            fala = gTTS(h, lang="pt-br")
            fala.save("fala.mp3")
            playsound("fala.mp3")
            
            print(datetime.datetime.now())


        elif frase == "tempo":
            c = "Consultando o tempo ... Daniel"

            fala2 = gTTS(c, lang="pt-br")
            fala2.save("fala2.mp3")
            playsound("fala2.mp3")

            link = "https://api.hgbrasil.com/weather?woeid=455860"

            resposta = requests.get(link)
            content = resposta.json()

            tempo = content["results"]["temp"]
            print(tempo, "C em Feira de Santana")
            
        
        elif frase == "Abrir Google":

            g = "Abrindo google ... Daniel"

            fala3 = gTTS(g, lang="pt-br")
            fala3.save("fala3.mp3")
            playsound("fala3.mp3")

            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")


        elif frase == "Abrir calculadora":
            ca = "Abrindo calculadora ... Daniel"

            fala4 = gTTS(ca, lang="pt-br")
            fala4.save("fala4.mp3")
            playsound("fala4.mp3")

            os.startfile("C:\Windows\System32\calc.exe")

        elif frase == "Abrir comando":
            co = "Abrindo comando ... Daniel"

            fala5 = gTTS(co, lang="pt-br")
            fala5.save("fala5.mp3")
            playsound("fala5.mp3")

            os.startfile("C:\Windows\System32\cmd.exe")

        elif dic.spell(frase) == True:
            pesqui = "Ok, pesquisando ... Daniel"

            fala6 = gTTS(pesqui, lang="pt-br")
            fala6.save("fala6.mp3")
            playsound("fala6.mp3")

            wikipedia.set_lang("pt")
            pesq = wikipedia.summary(frase)
            print(pesq)


        

        else:
            dese = "Não entendi ... Daniel . Poderia repetir?"

            de = gTTS(dese, lang="pt-br")
            de.save("desen.mp3")
            playsound("desen.mp3")


        return frase

        
        
   

class Ajuda(Screen):
    pass

class Tutorial(Screen):
    pass

Builder.load_string(arq_kv)

class DAI(App):
    def build(self):
        return Telas()

DAI().run()

########################
# O TESTE FOI UM SUCESSO
########################

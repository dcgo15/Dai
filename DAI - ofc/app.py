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

#############
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#############


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
                title: "DAI - v1.1.2"
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


        #TENHO QUE USAR VOZES PARA RESPONDER

        if frase == "horas":
            print("OK, MODO: CONSULTAR HORARIO ATIVADO")

            print(datetime.datetime.now())

        elif frase == "tempo":
            print("OK, MODO: CLIMA ATIVADO")

            link = "https://api.hgbrasil.com/weather?woeid=455860"

            resposta = requests.get(link)
            content = resposta.json()

            tempo = content["results"]["temp"]
            print(tempo, "C")

            

        elif frase == "Google":
            #PESQUISAR GLOBALIZAÇÃO
            print("OK, MODO: PESQUISAR ATIVADO")

            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

            

        elif frase == "calcular":
            print("OK, MODO: CALCULAR ATIVADO")

            os.startfile("C:\Windows\System32\calc.exe")
        

        else:
            print("NÃO ENTENDI")


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

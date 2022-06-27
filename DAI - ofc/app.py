from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

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
                title: "DAI"
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
        padding: [80, 40]

        Label:
            text: ""

        Button:
            text: "Clique aqui"
            size_hint: .2, 1

        Label:
            text: "Fale"

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
    pass

class Ajuda(Screen):
    pass

class Tutorial(Screen):
    pass

Builder.load_string(arq_kv)

class DAI(App):
    def build(self):
        return Telas()

DAI().run()

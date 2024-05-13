from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = get_color_from_hex('#ffffff')
Window.size = (900,500)

class Myapp(App):
    def build(self):

        layout = FloatLayout()
        imagem = AsyncImage(source="https://cdn-icons-png.flaticon.com/512/9187/9187604.png",pos=(450,450),size_hint=(0.2,0.2))
    
        texto1 = Label(text="Estudante: ",size=(100,30),pos=(-150,100),color=get_color_from_hex('#0077b6'))

        texto2 = Label(text="'Nome do Aluno'", size=(100, 30),pos=(0,100),color=get_color_from_hex('#0077b6'))

        texto3 = Label(text="Série: ",size=(100, 30),pos=(-170,50),color=get_color_from_hex('#0077b6'))

        texto4 = Label(text="'Série do Aluno'",size=(100, 30),pos=(0,50),color=get_color_from_hex ('#0077b6'))

        texto5 = Label(text= "Disponibilidade: ",size= (100, 30),color=get_color_from_hex("#0077b6"),pos=(-130,0))


        botao = Button(size_hint=(0.4, 0.08),pos=(350,150),text= "Liberar Aluno",background_color=get_color_from_hex('#0077b6'))
        
        layout.add_widget(imagem)
        layout.add_widget(texto1)
        layout.add_widget(texto2)
        layout.add_widget(texto3)
        layout.add_widget(texto4)
        layout.add_widget(texto5)
        layout.add_widget(botao)

        return layout
Myapp().run()

# Aqui vai ser convertido o texto para voz
# Instale o gtts (pip install gtts)
import flet as ft
from gtts import gTTS
import pygame

#tts = gTTS('Oi, Eu sou a Jarvina', lang='pt-br')
#tts.save('audios/hello.mp3')
# Primeiro teste feito com a biblioteca gtts

# Uma pequenha função que cria uma saudação
#def receba_um_ola():
#    nome_variavel = input("Digite o seu nome")
#    resultado_da_função = gTTS('Olá '+nome_variavel+', prazer em conhecelo', lang='pt-br')
#    resultado_da_função.save('audios/saudação.mp3')
#receba_um_ola()

# Pequeno programa com interface grafica com o flet

def index(run):

    def enviar_nome(exec):
         audio = gTTS('Olá '+campo_nome+', seja bem vindo ao sistema!', lang='pt-br')
         audio.save('audio_executavel.mp3')
    def ouvir_audio(exec2):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer_music.load('audio_executavel.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()

        page.update()

    main_text = ft.Text("Olá! Bem vindo ao programa")
    campo_nome = ft.TextField(label="Escreva seu nome no campo:")
    send_name = ft.ElevatedButton("Enviar", on_click=enviar_nome)

    run.add(main_text)

ft.app(target=index, view=ft.WEB_BROWSER, port=8000)
# Aqui vai ser convertido o texto para voz
# Instale o gtts (pip install gtts)
from gtts import gTTS
from playsound import playsound


#tts = gTTS('Oi, Eu sou a Jarvina', lang='pt-br')
#tts.save('audios/hello.mp3')
# Primeiro teste feito com a biblioteca gtts

# Uma pequenha função que cria uma saudação
def receba_um_ola():
    nome_variavel = input("Digite o seu nome")
    resultado_da_função = gTTS('Olá '+nome_variavel+', prazer em conhecelo', lang='pt-br')
    resultado_da_função.save('audios/saudação.mp3')
    playsound('audios/saudação.mp3')
#receba_um_ola()

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/bem_vindoo.mp3')
    playsound('audios/bem_vindoo.mp3')

cria_audio('Oi, eu sou a Jarvina')

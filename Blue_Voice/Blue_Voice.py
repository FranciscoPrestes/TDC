#Script: Blue_Slack
#Version: 1.0.0
#Author: Fernanda Paulino Leite
#Date: 25/04/2022

import os
from jproperties import Properties
import json
import speech_recognition as sr # importando biblioteca de reconhecimento de voz
import pyttsx3
import LibsBot.SmartBot as bt
import LibsBot.Upbd as up
import time as tm

speak=pyttsx3.init('sapi5') # setando biblioteca pra windows
voices = speak.getProperty('voices') # criando objeto emissor de voz
speak.setProperty('voice', voices[0].id)
 

def Speak(text):
    speak.say(text)
    speak.runAndWait()

cwd=os.getcwd()
configs=Properties()
with open(cwd + '\config.properties','rb') as read_prop:
    configs.load(read_prop)
    prop_view=configs.items()
    for item in prop_view:
        if item[0]=='caminho_repositorio':
            caminho_repositorio=item[1].data
        if item[0]=='caminho_clone':
            caminho_clone=item[1].data 

print('Trained robot')
# cria o objeto app com o token do bot
reconhecedor=sr.Recognizer()
with sr.Microphone() as microfone: # acessando microfone do computador    
    reconhecedor.adjust_for_ambient_noise(microfone) #ajustando o microfone para o ruído ambiente
    cont=1
    continua=0
    Speak('olá , em que posso ajudar?')
    while True:
        try:
            audio=reconhecedor.listen(microfone)
            frase=reconhecedor.recognize_google(audio, language="pt-BR")
            print('reconhecendo')
            print(frase)
            resposta=bt.bot_response(frase)
            complemento=resposta[1]
            Speak(resposta[0])
            continua=1
            if complemento=='1':
                resposta=up.PushGit(caminho_repositorio,caminho_clone)
                complemento=''
                Speak(resposta)
            elif complemento=='2':
                audio=reconhecedor.listen(microfone)
                banco=reconhecedor.recognize_google(audio, language="pt-BR")
                print(banco)
                Speak('ok, preparando a subida')
                print('Baixando repositório')
                caminho=up.PullGit(caminho_repositorio,caminho_clone)
                banco=banco.replace(' ','_')
                script=banco  + '.sql'
                print('Executando script de criação')
                up.ApplyScript(caminho,script,banco)
                Speak('Banco implantado. Em que mais posso ajudar?')
                complemento=''
            elif complemento=='3':
                complemento='' 
                break
            
        except:
            print('')
                

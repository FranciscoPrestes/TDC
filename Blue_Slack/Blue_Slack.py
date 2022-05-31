#Script: Blue_Slack
#Version: 1.0.0
#Author: Fernanda Paulino Leite
#Date: 25/04/2022

#bibliotecas
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import LibsBot.SmartBot as bt


# cria o objeto app com o token do bot
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.message("")

#Trata mensagens recebidas e retorna resposta
def message_hello(message, client):
    #recebe a frase vinda do slack
    frase=message['text']
    #passa a frase para a biblioteca que vai avaliar a similaridade
    resposta=bt.bot_response(frase)
    #retorna a resposta para a thread do slack onde foi feita a pergunta
    result=client.chat_postMessage(channel=message['channel'],text=resposta,thread_ts=message['ts'])

            
# Inicia o app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

    
    
    

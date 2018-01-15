import json
import requests

from bot import app
from bot import manager

from flask import request

from bot.modules.tables import User
from bot.modules.dialogs import Dialog
from bot.modules.toolbox import ToolBox

FB_SITE_TOKEN, FB_VERIFY_TOKEN = ToolBox.load_config()

class Bot():
    '''
        Classe do bot
    '''

    @app.route('/', methods = [ 'GET' , 'POST' ])
    def hook():
        '''
            Método que faz o tratamento das requisições/envios
        '''
        
        if request.method == 'POST':
            '''
                Adicione os tratamentos das mensagens enviadas de seu bot aqui
            '''

            pass

        elif request.method == 'GET':
            '''
                Adicione os tratamento das mensagens recebidas de seu bot aqui
            '''

            pass
    
        return 'No reply'

bot = Bot()
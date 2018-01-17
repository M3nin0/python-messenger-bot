import requests

from bot.modules.toolbox import ToolBox

FB_SITE_TOKEN, FB_VERIFY_TOKEN = ToolBox.load_config()

class Dialog(object):
    '''
        Classe de diálogos
    '''

    @staticmethod
    def send_payload(payload):
        '''
            Método para envio de payloads. Este método permite enviar payloads que ainda não tem métodos

            :param payload: str (Dicionário com as informações para envio)
                - Exemplo:
                    { 'recipient' : { 'id' : user_id }, 'message' :  'texto legal' }
                - Este pode ser um payload gerado pelos método:
                    - send_buttons();
                    - send_media_attached();
                    - send_message().

            :return void
        '''

        requests.post(
            'https://graph.facebook.com/v2.6/me/messages/?access_token=' + FB_SITE_TOKEN,
            json = payload
        )

    @staticmethod
    def send_message(text, user_id):
        '''
            Método para enviar mensagens simples.

            :param text: str (Texto a ser enviado)
            :return void
        '''

        payload = {
                'recipient' : {
                        'id' : user_id
                    },
                'message' : {
                        'text': text
                    }
                }

        Dialog.send_payload(payload)


    @staticmethod
    def send_config(payload):
        '''
            Método para envio de payloads de configuração

            :param payload: str (Dicionário com as informações)
                - Exemplo:
                    { 'get_started' : { 'payload' : 'text' } }
                - Este método pode ser usado com os seguintes métodos existentes:
                    - send_greeting();
                    - send_get_started().

            :return void
        '''

        requests.post(
                'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=' + FB_SITE_TOKEN,
                json = payload
            )


    @staticmethod
    def send_greeting(text_default, locale, text_for_locale):
        '''
            Método que prepara o payload de greeting
            
            :param text_default: str (Texto default para todos os locales)
            :param local: str (Especifica um locale)
            :param text_for_locale: str (Especifica o texto que 
                                        será usado no locale definido)
            
            :return dict
        '''
        
        payload = {'greeting': [
                        {'locale': 'default',
                        'text': text_default } , {
                        'locale': locale,
                        'text': text_for_locale
                        }]}

        Dialog.send_config(payload)


    @staticmethod
    def send_get_started(text):
        '''
            Método para enviar o get_started

            :param text: str (Texto que será usado no get_started)
            
            :return dict 
        '''
        
        payload = { 'get_started' : {  'payload' : text  } }

        Dialog.send_config(payload)


    @staticmethod
    def send_buttons(buttons, text, user_id):
        '''
            Método para enviar botões

            :param buttons: list (Coleção do tipo Botão)
                Exemplo:
                    [ {'type' : 'postback', 'title' : 'Button title', 'payload' : 'text'} ]
            :param text: str (Texto que será exibido junto aos botões)
            :param user_id: str (id do usuário que receberá a mensagem)

            :return dict
        '''

        _buttons = []

        # Criando os dicionários dos botões
        for button in buttons:
            _buttons.append(
                    {'type': button.type_button,
                     'title': button.title,
                     'payload': button.payload_text})

        payload = { 'recipient' : { 'id' : user_id },
                    'message'   : { 'attachment' : {
                     'type' : 'template',
                     'payload': {
                      'template_type' : 'button',
                      'text' : text,
                      'buttons' : _buttons[0:]
                     } } } }

        Dialog.send_payload(payload)    
    
    @staticmethod
    def send_media_attached(typem, user_id, media_id):
        '''
            Método para fazer o envio de medias (Videos, images)
            Envia uma media por vez

            :param typem: str (Tipo da media)
                Exemplo:
                    - image;
                    - video.
            :param user_id: str (id do usuário que irá receber)
            :param image_id: str (id do attach no facebook)

            :return dict
        '''

        return { 'recipient' : { 'id' : user_id }, 
                'message' : { 'attachment' : {
                    'type': typem,
                    'payload': { 'attachment_id' : media_id }
                } } }


    @staticmethod
    def send_persistent_simple_menu(menu_itens):
        '''
            Método para fazer o envio de menu persistentes

            :param menu_itens: list (Coleção de opções para o menu)
            :return void
        '''
        _menu_itens = []

        for item in menu_itens:
            _menu_itens.append(
                    {'title': item.title,
                     'type': item.item_type,
                     'payload': item.payload
                     }
                )

        payload = {
                  "persistent_menu":[
                    {
                      "locale":"default",
                      "composer_input_disabled": "true",
                      "call_to_actions":[
                    {
                        "title":"Conta legal",
                        "type":"nested",
                        "call_to_actions": _menu_itens[0:]
                        } ] } ] }

        Dialog.send_config(payload)


    @staticmethod
    def get_fb_date(user_id):
        '''
            Método que coleta informações do usuário através do user_id

            :param user_id: str (id do usuário)
            :param fb_site_token: str (Token da API do Facebook)

            :return list
        '''

        r = requests.get(
            'https://graph.facebook.com/v2.6/' + str(user_id) 
                                               + '?access_token=' +  FB_SITE_TOKEN
        )

        _infos = r.json()
        
        return [ _infos['first_name' ] , _infos[ 'last_name' ] , _infos[ 'gender' ] ]

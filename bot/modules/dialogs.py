class Dialog():
    '''
        Classe de diálogos
    '''


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
        
        return {'greeting': [
                        {'locale': 'default',
                        'text': text_default } , {
                        'locale': locale,
                        'text': text_for_locale
                        }]}


    @staticmethod
    def send_get_started(text):
        '''
            Método para enviar o get_started

            :param text: str (Texto que será usado no get_started)
            
            :return dict 
        '''
        
        return { 'get_started' : {  'payload' : text  } }


    @staticmethod
    def send_buttons(buttons, text, user_id):
        '''
            Método para enviar botões

            :param buttons: list (Template dos botões que serão usados)
                Exemplo:
                    [ {'type' : 'postback', 'title' : 'Button title', 'payload' : 'text'} ]
            :param text: str (Texto que será exibido junto aos botões)
            :param user_id: str (id do usuário que receberá a mensagem)

            :return dict
        '''

        return { 'recipient' : { 'id' : user_id },
                 'message'   : { 'attachment' : {
                     'type' : 'template',
                     'payload': {
                      'template_type' : 'button',
                      'text' : text,
                      'buttons' : buttons
                     } } } }
    
    
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
        
class Button():
    '''
        Classe que representa o componente de botão. O botão criado
        por esta classe pode ser dos tipos:
                - Botão de postback (Já testado)
    '''
    
    def __init__(self, type_button, title, payload_text):
        '''
            Método inicializador da classe.

            :param type_button: str
            :param title: str
            :param payload_text: str
        '''
        self.type_button = type_button
        self.title = title
        self.payload_text = payload_text

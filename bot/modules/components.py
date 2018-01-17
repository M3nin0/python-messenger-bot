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

class MenuItem():
    '''
        Classe que reprenta componente de menu simples
    '''

    def __init__(self, title, item_type, payload):
        '''
            Método inicializador da classe.

            :param title: str (Título da opção)
            :param item_type: str (Tipo do item)
            :param payload: str (Conteúdo que será gerado ao item ser selecionado)
        '''
        self.title = title
        self.item_type = item_type
        self.payload = payload

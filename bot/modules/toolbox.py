import json

class ToolBox(object):
    '''
        Classe que métodos úteis ao funcionamento do bot
    '''

    
    @staticmethod
    def load_config():
        '''
            Método que carrega as informações do arquivos de configuração

            :return list
        '''

        with open('bot/config/config.json') as temp_json:
            try:
                data = json.load(temp_json)
                return [ data['tokens']['fb_site_token' ] , data['tokens']['fb_verify_token'] ]
            except BaseException as e:
                print(e)
                return [ -1, -1 ]
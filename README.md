# Python Messenger Bot - Template

Template para bots do Facebook

## Estrutura 

Esta template foi criada utilizando os principios do Flask, desta forma há um meneger, que cuidará da execução de todos os módulos, de forma simples e rápida.

## Armazenamento de dados 

Para armazenar os dados dos usuário que utilizaram o bot, há o SQLite que faz o armazenamento das informações básicas do usuário (Nome, sobrenome, gênero, id).

## Implementando bot com a template

Para realizar a implementação é bastante simples, será necessário utilizar o <code>ngrok</code>, nele será aberto um servidor na porta **5000**.

No Linux, após baixar o ngrok, o comando a ser executado é mostrado abaixo:

```shell
chmod +x ngrok
./ngrok http 5000
```

Configure também um virtualenv, para que você não tenha problemas com dependências, para isso faça:
* Linux
```shell
# Cria o virtualenv
virtualenv venv
# Ativa
source venv/bin/activate
# Instala dependências
pip install -r requirements.txt

# Caso queira sair do virtualenv use:
deactivate
```

OBS: O comando **virtualenv** pode variar de acordo com sua configuração de path.


Agora configure o arquivo <code>config.json</code> com suas tokens, o arquivo fica parecido com o exemplo abaixo:

```python
{

  "tokens": {

    "fb_site_token": "Token da página",

    "fb_verify_token": "Token de verificação usado pelo Facebook"

  }

}
```

OBS: Lembre-se, a chave de verificação deve ser posta no **webhook** da página, no Facebook.

Após realizar estas configurações, basta inserir seus controles de fluxo no arquivo <code>chat.py</code> e pronto sua aplicação estará funcionando!

### Exemplo de implementação

Um exemplo de implementação feita com a template é o [Beauty BOT](https://github.com/M3nin0/python-messenger-bot)

## Métodos

Os métodos já criados e disponíveis para uso são:

 - [X] send_greeting;
    - Método que prepara o payload de greeting.
 - [X] send_get_started;
    - Método para enviar o get_started.
 - [X] send_buttons;
    - Método para enviar botões.
 - [X] send_media_attached;
    - Método para fazer o envio de medias (Videos, images).
 - [X] send_payload;
    - Método para envio de payloads.
        - Este envia payloads já programados, mas pode fazer envio de qualquer payload (Chat) que for necessário.
 - [X] get_fb_date;
    - Método que coleta informações do usuário através do user_id.
 - [X] send_config;
    - Método para envio de payloads de configuração.
-  [X] send_message;
    - Método para fazer envio de mensagens simples.
<<<<<<< HEAD
-  [X] send_persistent_simple_menu;
    - Método para fazer o envio de menu persistente.
=======
    
## Sobre

Bot criado utilizando:
* Flask;
* SQLAlchemy;
* Requests.
>>>>>>> 48699260757d1191586cb246e29216239cc95747

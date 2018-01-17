# Python Messenger Bot - Template

Template para bots do Facebook

## Estrutura 

Esta template foi criada utilizando os principios do Flask, desta forma há um meneger, que cuidará da execução de todos os módulos, de forma simples e rápida.

## Armazenamento de dados 

Para armazenar os dados dos usuário que utilizaram o bot, há o SQLite que faz o armazenamento das informações básicas do usuário (Nome, sobrenome, gênero, id).

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
-  [X] send_persistent_simple_menu;
    - Método para fazer o envio de menu persistente.
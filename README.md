# Selenium

Script em Python para **enviar mensagens automaticamente pelo WhatsApp
Web** usando Selenium.

Criado para facilitar o envio do **link de grupos para
alunos/interessados**, sem precisar salvar contatos ou copiar e colar
mensagens.

------------------------------------------------------------------------

## 📋 Pré-requisitos

-   Python (**estou usando a versão 3.9, não testei com versões anteriores**)
-   Chrome (**Navegador**)
-   Selenium

Instalação:

``` bash
pip install selenium
```

------------------------------------------------------------------------

## ▶️ Como usar

1.  Edite a lista:

``` python
numeros = [
    "5582999999999",
    "5582998888888"
]
```

2.  Edite a mensagem:

``` python
mensagem = "Olá! Aqui está o link do grupo: https://chat.whatsapp.com/SEULINK"
```

3.  Execute:

``` bash
python whatAuto.py
```

4.  Faça login no WhatsApp Web\
5. Pressione Enter no mesmo terminal em que você rodou o script.

------------------------------------------------------------------------

## ⚙️ Funcionamento

Para cada número: 1. Abre a conversa 2. Insere a mensagem 3. Envia 4.
Aguarda 5. Repete

------------------------------------------------------------------------

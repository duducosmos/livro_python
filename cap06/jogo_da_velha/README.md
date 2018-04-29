# Instalação

O curse já vem pré instalado nos sistemas unix e linux, porém não é um módulo nativo no window.
Para rodar o jogo da velha no Windows é preciso instalar o modulo. 
A instalação do módulo vai depender da versão do Python instalado na sua máquina, 32bits ou amd64.

Os arquivos para instalar o curse no Windows estão disponíveis em: http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

Para instalar a versão para o Python 32 bits use o comando

```
pip install curses-2.2-cp36-cp36m-win32.whl
```

Para versões 64 bit

```
pip install curses-2.2cp36-cp36m-win_amd64.whl
```

Alternativamente pode-se tentar o comando:

```
python -m pip install curses-2.2cp36-cp36m-win_amd64.whl
```
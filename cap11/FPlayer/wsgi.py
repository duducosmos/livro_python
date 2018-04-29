import sys
activate_this = "/home/eduardo/MEGAsync/MeusLivros/Livro_1_python/codigosLivro/env/bin/activate_this.py"

execfile(activate_this, dict(__file__=activate_this))

PROJECT_DIR = "/home/eduardo/MEGAsync/MeusLivros/Livro_1_python/codigosLivro/PorCapitulo/cap11/FPlayer"

sys.path.append(PROJECT_DIR)

from fplayer import app as application

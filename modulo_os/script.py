import os
import shutil
from pathlib import Path

#cria o path caso não exista
if not os.path.exists('aula1'):
	os.mkdir('aula1')

#abre o path aula1
os.chdir('aula1')

#cria o arquivo xpto em aula1
Path('xpto.txt').touch()

#copia o arquivo xpto para cpto1
shutil.copy('xpto.txt', 'xpto1.txt')
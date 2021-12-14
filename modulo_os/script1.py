import os
from pathlib import Path
import shutil

#criando diretório
if not os.path.exists('arquivos_live'):
	os.mkdir('arquivos_live')

#abrindo o diretório
os.chdir('arquivos_live')
for p in range(9):
	#criando os arquivos
	if not os.path.exists(f'live_{p}.txt'):
		Path(f'live_{p}.txt').touch()

#apagando os arquivos que o indice seja menor que 5
for arquivo in os.listdir():
	if int(arquivo.split('_')[1].split('.')[0]) < 5:
		#print(arquivo)
		os.remove(arquivo)

#renomeando os arquivos restantes
for k, arquivo in enumerate(os.listdir()):
	shutil.move(arquivo, f'live_{k}.txt')

#listando os arquivos do diretório
print(os.listdir())
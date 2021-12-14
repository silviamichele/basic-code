import os
import shutil
from pathlib import Path

if not os.path.exists('arquivos_live'):
	os.mkdir('arquivos_live')

os.chdir('arquivos_live')
for x in range(1, 11):
	if not os.path.exists(f'pasta_{x}'):
		os.mkdir(f'pasta_{x}')
		
		Path(os.path.join(f'pasta_{x}', 'arquivo_1.txt')).touch()
		Path(os.path.join(f'pasta_{x}', 'arquivo_2.txt')).touch()

for val in os.walk('.'):
	print(val)

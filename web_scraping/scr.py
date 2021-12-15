from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
#módulos uteis: urllib.request, urllib.parse, e url

#abrindo o arquivo html => request - response
try:
	html = urlopen("http://pythonscraping.com/pages/page1.html")
	#mostrando o conteudo do arquivo
	#print(html.read())
	#passando o arquivo para o beautiful soup
	obj = BeautifulSoup(html.read(), 'html.parser')
	#obtendo o valor do titulo do arquivo
	# print('titulo da página\n', obj.title)
	# print('titulo do texto\n', obj.h1)
	# print('div com texto\n', obj.div)
	#print(obj.find('silvia'))
	print(obj.title)
	try:
		print(obj.a)
	except AttributeError as e:
		print(e)
	if obj.a == None:
		print('essa tag não existe')

except HTTPError as e:
	print(e)

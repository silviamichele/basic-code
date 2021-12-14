teste = open("primeiro.txt", 'r')

with teste:
	print(teste.read())
	#teste.write("\n tentando ler 2")

teste.close()
print(teste.closed)
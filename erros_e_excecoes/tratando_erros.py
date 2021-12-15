#escolha sua exeção e seja feliz: https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions

#caso o valor digitado pelo usuário seja diferente 
#de um número inteiro o código lança uma exeção
try:
	num = int(input("digite um número: "))
	if num > 15:
		#lança uma exeção 
		raise Exception('spam', 'eggs')
	print(num)

except ValueError as erro:
	#exeção por valor inválido
	print(erro)

except Exception as excp:
	#exeção definida pelo programador
	print(excp)
	print(excp.args)
	#args descrevem a excepção
finally:

	#trecho da doc: Em aplicação do mundo real, a cláusula finally é útil para
	# liberar recursos externos (como arquivos ou conexões de 
	#rede), independentemente do uso do recurso ter sido bem sucedido ou não.
	print("sempre cai aqui")
"""
como passar argumentos na função: 

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
        -- Positional only

chamando a funções:

f(val1, val2, val3 or pos_or_kwd=val3, kdw=val4)


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

"""


def tipoNumero(numero):
	print("aqui")
	match numero:
		case 100:
			return "igua a 100"
		case 50:
			return "menor que 100"
	return "algum numero aleatorio"


def conferirLista(valor, lista = []):
	lista.append(valor)
	return lista

#expressão lambda
calc30 = lambda c: c * 0.3

#valor = int(input("digita um numero: "))

#usando match pela primeira vezzz
#print(tipoNumero(valor))

#entendendo argumentos pre-definidos, a 
#lista acrescenta o numero 5, e não 

#print(conferirLista(valor))
#print(conferirLista(5))

def testarDocumentacao():
	"""
		documentacao 1
	"""

#print(testarDocumentacao.__doc__)



#stop in 5.3

def uniao(a, b):
	"""
	elemnetos que estão em a ou b ou ambos
	"""
	a = set(a)
	b = set(b)
	return a | b

def intersection(a, b):
	"""
	elementos que estão em b e a
	"""
	a = set(a)
	b = set(b)
	return a & b

def diferenca(a, b):
	"""
	elementos que estão em a - elementos que estão em b, 
	ex.: 
		a = {1, 2, 4*}
		b = {3, 4*, 9}
		a - b = {1, 2}
	"""
	a = set(a)
	b = set(b)
	return a - b

def complemento(a, b):
	"""
	elementos em a ou b mas não em ambos	
	"""
	a = set(a)
	print(a)
	b = set(b)
	print(b)
	return a ^ b

#print(complemento.__doc__)
#print(uniao.__doc__)

#print(uniao([1, 2, 2, 3], [2, 3, 5]))

"""
	dicionarios = {}
	"chave":"valor"
	list(dicionario)
	[output] = ["chave1", "chave2", ...]
	sorted(dicionarios)
	[output] = ['a', 'b', ...]

"""
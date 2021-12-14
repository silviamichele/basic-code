#author : silvia michele
#e-mail : silvia.teles.br@gmail.com
import json

def returnJSON():
	dic = {}
	with open('contacts.json', 'r+') as json_arquivo_ler:
		dic = json.load(json_arquivo_ler)
	json_arquivo_ler.close()
	return dic


while True:
	option = input("\na - abrir contatos\ns - sair\nn - novo contato\ne - editar contato\ndigite a opcao escolhida: ")
	
	if option == 's':
		break

	elif option == 'a':
		dic = returnJSON();
		for k, v in dic.items():
			print(f"\n{k}\nnome: {v['nome']}\nsobrenome: {v['sobrenome']}\nnumero: {v['numero']}\n{'-'*10}")

	elif option == 'n':
		dic = returnJSON()
		with open('contacts.json', 'w') as json_arquivo:
			nome = input("nome: ")
			sobrenome = input("sobrenome: ")
			numero = input("numero: ")
			dic[f"{sobrenome.upper()}, {nome}"] = {
				"nome": nome,
				"sobrenome": sobrenome,
				"numero": numero
			}
			json.dump(dic, json_arquivo)
		json_arquivo.close()

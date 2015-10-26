'''Validaciones
	De rfc
	curp
	url
	correo
	ip
	BARRETO AVILES EZEQUIEL ADRIAN

'''
import os

def validar_RFC():
	os.system('clear')
	os.system('cls')
	rfc = raw_input("Escriba su RFC:  ")
	if len(rfc) >= 10 and len(rfc) <= 13:
		if rfc[:4].isdigit():
			print "Ocurrio un error"
		else:
			if rfc[4:6].isdigit():
				if rfc[6:8].isdigit():
					if int(rfc[6]) < 2 :
						print "RFC Validado con exito"
						menu()
						return
	print "Su RFC no es valido, Vuelva a intentarlo"
	menu()
	return

def validar_CURP():
	os.system('clear')
	os.system('cls')
	curp = raw_input("Escriba su CURP:  ")
	curp.upper()
	if len(curp) == 18:
		if curp[:4].isalpha():
			if curp[4:10].isdigit() and int(curp[6:8]) < 13 and int(curp[8:10]) < 32:
				if curp[10:16].isalpha() and curp[10] == 'H' or curp[10] == 'M' :
					if curp[16:18].isdigit():
						print "CURP validado con exito "
						menu()
						return
	print "Su CURP no es valido, Vuelva a intentarlo"
	menu()
	return

def validar_URL():
	os.system('clear')
	os.system('cls')
	url = raw_input("Escriba su URL:  ")
	lista = url.split(".")
	if url[0:11] == "http://www.":
		if len(lista) > 2 and len(lista) < 4:
			print "URl validada con exito"
			menu()
			return
	print"Su URL no es valida, Vuelva a intentarlo"
	menu()
	return

def validar_Correo():
	os.system('clear')
	os.system('cls')
	correo = raw_input("Escriba su Correo:  ")
	if (correo.find("@") != -1 and correo.find(".") != + -1):
		print "Su correo fue validado con exito"
		menu()
		return
	print "Su Correo no es valido, vuelva a intentarlo"
	menu()
	return

def validar_IP():
	os.system('clear')
	os.system('cls')
	ip = raw_input("Escriba su IP:  ")
	#xxx.xxx.xxx.xxx
	lista = ip.split(".")
	if len(lista) == 4:
		 if lista[0] != "" or lista[1] != "" or lista[2] != "" or lista[3] != "":
		 	if lista[0].isdigit() and lista[1].isdigit() and lista[2].isdigit() and lista[3].isdigit():
				if int(lista[0]) < 256 and int(lista[1]) < 256 and int(lista[2]) < 256 and int(lista[3]) < 256:
					print "Su IP, fue validada con exito"
					menu()
					return
	print "Su IP no es valida, vuelva a intentarlo"
	menu()
	return

def menu():
	print
	print "Practica 2"
	print "Validacion de RFC / CURP / URL / Correo / IP"
	print "Menu :"
	print "1. RFC"
	print "2. CURP"
	print "3. URL"
	print "4. Correo"
	print "5. IP"
	print "Presione cualquier otra tecla para salir"
	tipo = {'1':validar_RFC,
			'2':validar_CURP,
			'3':validar_URL,
			'4':validar_Correo,
			'5':validar_IP}
	valor = raw_input()
	try:
		resultado = tipo[valor]()
	except:
		print "Adios"
	return

print
menu()

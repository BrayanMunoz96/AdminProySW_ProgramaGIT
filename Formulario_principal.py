def main():
	print("Formulario para nuevos usuarios")
	
	#Preguntas
	nombre = input("Ingrese su nombre completo")
	edad = input("Ingresa también tu edad ")
	helado = input("Cual es tu sabor de helado favorito?")

	print("Procesando...")
	
	#Respuestas
	print("Tu nombre es ", nombre)
	print("\n")
	print("Tienes {} años\n".format(edad))
	print("Tu sabor de helado favorito es ", helado)
	print("\n")

main()

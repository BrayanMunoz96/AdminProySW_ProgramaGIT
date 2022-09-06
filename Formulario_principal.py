def main():
	print("Formulario para nuevos usuarios")
	
	#Preguntas
	nombre = input("Ingrese su nombre completo")
	edad = input("Ingresa también tu edad ")
	helado = input("Cual es tu sabor de helado favorito?")
	pelicula = input("¿Cual es tu pelicula favorita?")
	color = input("Cual es tu color favorito?")
	canción = input("Cuál es tu canción favorita?")
	serie = input("Cuál es tu serie de TV favorita?")

	print("-------------Procesando--------------")
	
	#Respuestas
	print("Tu nombre es ", nombre)
	print("\n")
	print("Tienes {} años\n".format(edad))
	print("Tu sabor de helado favorito es ", helado)
	print("\n")
	print ("Mi pelicula favorita es ", pelicula)
	print("\n")
	print("Mi color favorito es ", color)
	print("\n")
	print("Mi canción favorita es ", canción)
	print("\n")
	print("Mi serie de TV favorita es ", serie)
	print("\n")
	

main()

"""
·Primer proyecto personal. (13/02/2019)
Pesarme, sacar promedio, registro, funciones varias de programa.
"""
yes = ["yes", "y", "YES", "Y", "Yes", "yEs", "yeS", "yES", "YEs", ""]

def menu(): #Inicio del programa.
	print("""
			Fitness_Proyect.py Menu:

			-----------------------------------------------------
													
			[1]: New Log 				
			[2]: Previous Logs 			
			[3]: Restart Log
			[4]: Exit 
													
			-----------------------------------------------------

		""")

while True:

	menu() 

	while True: #Elegir opción del menú. Sólo 1, 2, 3 o 4.
		
		try:
			choice = int(input("Please enter option 1, 2, 3, or 4: "))
			if choice > 4 or choice < 1:
				raise ValueError
			break

		except ValueError:
			print("Invalid input. Try again, please.")

	if choice == 1: #Opción "New Log".

		while True: #Veces pesadas, fecha, y confirmación.
			try:
				times_weighed = int(input("How many times did you weigh yourself? (10 Max): "))
				if times_weighed > 10:
					raise ValueError

			except ValueError:
				print("Enter a whole number between 1-10, try again.")
				continue

			date = input("Enter today's date (DD/MM): ")
			confirm = input("%d times, @%s, is that correct? [Yes: Confirm / Anything Else: Decline]: " % (times_weighed, date))

			if confirm in yes:
				break

		counter = 1 #Inicia en 1.
		total_weight = 0 #Inicia en 0.
		while (counter != times_weighed + 1): #Sacar promedio. Sólo admitir números.
			try:
				accumulated = float(input("Enter weight #%d: " % (counter)))
				if (type(accumulated) is not float) or accumulated < 0:
					raise ValueError
			except ValueError:
				print("Only positive numbers accepted, try again.")
				continue

			counter += 1
			total_weight += accumulated
			
		average = total_weight / times_weighed

		with open("Log.txt", "a+") as Log: #Abrir y agregar información al archivo.
			Log.write("\n\n%.1f kg (%s)\n\n" % (average, date) + "-" * 20)

		print("New log succesfully added.")

	if choice == 2: #Opción "Previous Logs".

		with open("Log.txt", "r") as log: #Muestra el log completo.
				print("\n" + log.read() + "\n")

		total_logs = 0
		with open("Log.txt", "r") as log: #Muestra el número de logs.

			for line in log:
				words = line.split()
				for i in words:
					if i == "kg":
						total_logs += 1
			
		print("_" * 20 + "\n\nYou have entered a total of %s log/s!" % (total_logs))

	if choice == 3: #Borrar todo el progreso.

		restart = input("Do you really wanna lose all progress? [Yes: Confirm / Anything Else: Decline]: ")
		if restart in yes:

			with open("Log.txt", "w") as log:
				log.write("""_________________________

Fitness_Proyect.py 

#List of records.
Format:

Weight kilograms (DD/MM)
--------------------""")
			print("Progress erased.")
		else:
			print("Great.")

	if choice == 4:
		break

	print("")
	exit = input("Finished, do you want to exit the program? [Yes: Confirm / Anything Else: Decline]: ")
		
	if exit not in yes: #Reiniciar el programa.
		continue
	if exit in yes: #Cerrar programa.
		break
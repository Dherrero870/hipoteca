total_clases =float (input("Introduzca el número de clases totales:"))
clases_asistidas = float (input("Introduzca el número de clases a las que ha asistido:"))
nota = float (input("Introduzca su nota sobre 100:"))
asistencia = clases_asistidas / total_clases * 100
if asistencia >= 80 and nota >= 70:
    print ("Ha aprobado")
else:
    print("Ha suspendido")
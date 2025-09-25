nombre = "Daniel Buitrago"
edad = 52
altura = 1.75
pregunta = "¿Eres estudiante?"
pregunta2 = "¿Tienes sueño ahora mismo?"
R2 = "si"
validacion = "si"


#edad actual
print("Mi edad actual es:", edad)
#en dias
print("Mi edad en dias es:", edad * 365)


#edad en 5 años
print("mi edad en 5 años es", edad + 5)

mitad_altura = altura / 2




respuesta = input(pregunta + " (Sí/No): ")
respuesta2 = input(pregunta2 + " (Sí/No): ")


if validacion == respuesta.lower() :
    print("Sí es estudiante")
else:
    print("No es estudiante")

if R2 == respuesta2.lower() :
    print("Tiene sueño")
else:
    print("No tiene sueño")


print("¿Eres mayor de edad?")

if edad >=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("Tu altura es mayor a 1.75 cm?")
if altura >= 1.75:
    print("Es mas alto, mide arriba de los 1.75 cm")
else:
    print("Es mas bajo, mide abajo de los 1.75 cm")

print("Eres estudiante y no tienes sueño?")
if respuesta.lower() == "si" and respuesta2.lower() == "no":
    print("Eres estudiante y no tienes sueño")
elif respuesta.lower()=="no" and respuesta2.lower()=="si":
    print("No eres estudiante y tienes sueño")
elif respuesta.lower()=="no" and respuesta2.lower()=="no":
    print("No eres estudiante y no tienes sueño")
elif respuesta.lower()=="si" and respuesta2.lower()=="si":
    print("Eres estudiante y si tienes sueño ")

print("Tu edad es mayor a 20 o tu altura es menor a 1.60?")
if edad>20 or altura<1.60:
    print("Tu edad es mayor a 20 o tu altura es menor a 1.60")
else:
    print("Tu edad no es mayor a 20 y tu altura no es menor a 1.60")

nom = "niko"
print(nom=="niko")
""" Es true ya que a pesar de que no se este haciendo una comprativa con condicionales, se usa el operador,
de comparacion o de igualdad de python que es == """
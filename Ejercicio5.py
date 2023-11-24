n = int(input("Introduce el número de asignaturas: "))
asignaturas = {}
for i in range(n):
    asignatura = input("Introduce el nombre de la asignatura: ")
    nota = int(input("Introduce la nota que has sacado en la asignatura: "))
    if nota >= 90:
        letra = 'A'
    elif nota >= 80:
        letra = 'B'
    elif nota >= 70:
        letra = 'C'
    elif nota >= 60:
        letra = 'D'
    else:
        letra = 'F'
    asignaturas[asignatura] = letra

for asignatura, letra in asignaturas.items():
    print(f"En la asignatura {asignatura} has sacado un {letra}.")

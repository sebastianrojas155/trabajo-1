hemoglobina = float(input("Ingrese el nivel de hemoglobina (g/dL): "))
genero = int(input("Ingrese el género (1 = Hombre, 2 = Mujer): "))

if genero == 1:  # Hombre
    if hemoglobina < 12.2:
        print("Baja")
    elif hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")
elif genero == 2:  # Mujer
    if hemoglobina < 12.6:
        print("Baja")
    elif hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")
else:
    print("No es posible generar la alerta")
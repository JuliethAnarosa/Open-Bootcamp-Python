peso = input("¿cuanto pesas?\n")
altura = input("¿cuanto mides?\n")
imc = round(float(peso)/float(altura)**2,2)
print("tu indice de masa corporal es de " + str(imc))

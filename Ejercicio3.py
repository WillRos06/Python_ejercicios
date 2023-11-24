print("Bienvenido a Café Delicioso!")
tipo_sandwich = input("¿Deseas un sándwich frío o caliente? ")

if tipo_sandwich.lower() == "frío":
    print("Ingredientes para sándwiches fríos: Lechuga y tomates, atún, pavo.")
    ingrediente = input("Por favor, selecciona un ingrediente: ")
    print(f"Has seleccionado un sándwich frío con {ingrediente}.")
elif tipo_sandwich.lower() == "caliente":
    print("Ingredientes para sándwiches calientes: Pollo, queso cheddar, champiñones.")
    ingrediente = input("Por favor, selecciona un ingrediente: ")
    print(f"Has seleccionado un sándwich caliente con {ingrediente}.")
else:
    print("Lo siento, no entendí tu elección. Por favor, intenta de nuevo.")
# Solicita al usuario que introduzca el balance inicial
P = float(input("Por favor, introduce tu balance inicial: "))

# Tasa de interés
r = 0.055

# Número de años
t = 3

# Calcula e imprime el balance al final de cada año
for i in range(1, t + 1):
    A = P * (1 + r) ** i
    print(f"Al final del año {i}, tu balance sería: ${A:.2f}")
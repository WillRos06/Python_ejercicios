def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def es_poderoso(n):
    for i in range(2, n + 1):
        if es_primo(i) and n % i == 0:
            if n % (i**2) != 0:
                return False
    return True

numero = int(input("Introduce un número: "))
if es_poderoso(numero):
    print(f"El número {numero} es poderoso.")
else:
    print(f"El número {numero} no es poderoso.")

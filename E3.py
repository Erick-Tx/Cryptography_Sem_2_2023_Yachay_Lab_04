import random

# Algoritmo extendido de Euclides
def extended_euclidean_algorithm(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

# Función para generar un número primo aleatorio
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Función para verificar si un número es primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función para generar claves RSA
def generate_rsa_keys():
    p = int(input("Ingresa un número primo (p): "))
    q = int(input("Ingresa otro número primo (q): "))
    e = int(input("Ingresa el exponente público (e): "))

    N = p * q
    phi_N = (p - 1) * (q - 1)

    gcd, d, _ = extended_euclidean_algorithm(e, phi_N)

    if gcd != 1:
        print("Los valores de e y phi(N) no son primos entre sí. Por favor, elige un valor diferente para e.")
        return

    # Asegurarse de que d sea positivo
    d = d % phi_N

    print("Clave Pública (e, N): ({}, {})".format(e, N))
    print("Clave Privada (d, N): ({}, {})".format(d, N))

# Programa principal
if __name__ == "__main__":
    generate_rsa_keys()
